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
    'total_shares', 'out_dir_stat',
    'dividend_info','major_shareholder', \
     'minority_share', 'emp_status', \
     'top5_exec_comp'
    ]

# 토픽별 필드 변환 정보 정의
field_transformations = {
    #'all_dir_aud_comp': ['mendng_totamt' ,'jan_avrg_mendng_am'],
    #'major_shareholder': ['bsis_posesn_stock_co', 'trmend_posesn_stock_co'],
    #'minority_share': ['shrholdr_co', 'shrholdr_tot_co', 'shrholdr_rate', 'hold_stock_co', 'stock_tot_co'],
    #'comp_paper_bal': ['de10_below', 'de10_excess_de30_below', 'de30_excess_de90_below', 'de90_excess_de180_below', 'de180_excess_yy1_below', 'yy1_excess_yy2_below', 'yy2_excess_yy3_below', 'yy3_excess', 'sm'],
    #'corp_bond_bal': ['yy1_below', 'yy1_excess_yy2_below', 'yy2_excess_yy3_below', 'yy3_excess_yy4_below', 'yy4_excess_yy5_below', 'yy5_excess_yy10_below', 'yy10_excess', 'sm'],
    'total_shares': ["isu_stock_totqy", "now_to_isu_stock_totqy", "now_to_dcrs_stock_totqy", "redc", "profit_incnr", "rdmstk_repy", "etc", "istc_totqy", "tesstk_co", "distb_stock_co"], #주식의총수현황
    'out_dir_stat': ['drctr_co', 'otcmp_drctr_co', 'apnt', 'rlsofc', 'mdstrm_resig'], #사외이사
    'dividened_info': ['thstrm', 'frmtrm', 'lwfr'], #배당금정보
    'major_shareholder': ['bsis_posesn_stock_co', 'bsis_posesn_stock_qota_rt', 'trmend_posesn_stock_co', 'trmend_posesn_stock_qota_rt'], #최대주주현황
    'minority_share': ['shrholdr_co', 'shrholdr_tot_co', 'hold_stock_co', 'stock_tot_co'], #소액주주현황
    'emp_status': ['cnttk_co', 'cnttk_abacpt_labrr_co', 'sm', 'avrg_cnwk_sdytrn', 'fyer_salary_totamt', 'jan_salary_am'], #직원현황
    'top5_exec_comp': ['mendng_totamt', 'mendng_totamt_ct_incls_mendng'] #개인별 보수지급 금액(5억이상 상위5인) 
}

field_with_percetage = {
    'minority_share': ['shrholdr_rate', 'hold_stock_rate']
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

for topic in topics:
    schema = schema_set[topic]
    transform_fields = field_transformations.get(topic, [])
    create_batch(spark, topic, schema, transform_fields).save()