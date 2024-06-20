from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, explode, regexp_replace
from dotenv import load_dotenv
import os
from schema import *

load_dotenv()

spark = SparkSession.builder \
    .appName("Dart to Kafka to Spark") \
    .getOrCreate()

kafka_server = os.getenv('SERVER')
kafka_username = os.getenv('KAFKA_USERNAME')
kafka_password = os.getenv('KAFKA_PASSWORD')

# Kafka Config
kafka_bootstrap_servers = kafka_server
kafka_security_protocol = "SASL_SSL"
kafka_sasl_jaas_config = f"org.apache.kafka.common.security.plain.PlainLoginModule required username='{kafka_username}' password='{kafka_password}';"
kafka_sasl_mechanism = "PLAIN"

topics = [
    'cond_cap_sec_bal', 'exec_comp_stat', 'corp_bond_bal', 'short_bond_bal', \
    'com_paper_bal', 'debt_sec_perf', 'dir_aud_comp_gm', 'dir_aud_comp_type', \
    'total_shares', 'non_audit_contr', 'out_dir_stat', 'new_cap_sec_bal', \
    'cap_inc_dec_stat', 'dividend_info', 'treasury_stock', 'major_shareholder', \
    'major_share_chg', 'minority_share', 'exec_status', 'emp_status', \
    'indv_dir_aud_comp', 'all_dir_aud_comp', 'top5_exec_comp', 'other_corp_inv', 'single_corp_fin'
    ]

# 토픽별 필드 변환 정보 정의
field_transformations = {
    'all_dir_aud_comp': ['mendng_totamt' ,'jan_avrg_mendng_am'],
    'major_shareholder': ['bsis_posesn_stock_co', 'trmend_posesn_stock_co'],
    'minority_share': ['shrholdr_co', 'shrholdr_tot_co', 'shrholdr_rate', 'hold_stock_co', 'stock_tot_co'],
    'comp_paper_bal': ['de10_below', 'de10_excess_de30_below', 'de30_excess_de90_below', 'de90_excess_de180_below', 'de180_excess_yy1_below', 'yy1_excess_yy2_below', 'yy2_excess_yy3_below', 'yy3_excess', 'sm'],
    'corp_bond_bal': ['yy1_below', 'yy1_excess_yy2_below', 'yy2_excess_yy3_below', 'yy3_excess_yy4_below', 'yy4_excess_yy5_below', 'yy5_excess_yy10_below', 'yy10_excess', 'sm'],
    'cap_inc_dec_stat': []
}

def create_batch(spark, topic, schema, transform_fields):
    df = spark.read \
      .format("kafka") \
      .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
      .option("subscribe", topic) \
      .option("kafka.security.protocol", kafka_security_protocol) \
      .option("kafka.sasl.jaas.config", kafka_sasl_jaas_config) \
      .option("kafka.sasl.mechanism", kafka_sasl_mechanism) \
      .option("startingOffsets", "earliest") \
      .option("failOnDataLoss", "true") \
      .load() #DF load

    # Assuming the JSON array is in the "value" column as a string
    # Parse the JSON array using the defined schema
    parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("parsed_value"))

    # Explode the array to get individual records
    exploded_df = parsed_df.select(explode(col("parsed_value")).alias("record")).select("record.*")

    # 특정 필드의 쉼표 제거 및 문자열을 정수로 변환
    transformed_df = exploded_df
    for field in transform_fields:
        transformed_df = transformed_df.withColumn(field, regexp_replace(col(field), ",", "").cast("int"))
    
    write_stream =  transformed_df.write \
      .format("bigquery") \
      .option("temporaryGcsBucket", f"gs://dh_pipeline_2/checkpoints/{topic}") \
      .option("table", f"gleaming-plate-422507-e9.dataset_dart_samsung.{topic}") \
      .mode("append")
    
    return write_stream

for topic in topics:
    schema = schema_set[topic]
    transform_fields = field_transformations.get(topic, [])
    create_batch(spark, topic, schema, transform_fields).save()