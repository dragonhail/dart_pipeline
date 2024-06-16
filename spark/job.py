from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, explode, alias
from schema import *

spark = SparkSession.builder \
    .appName("Dart to Kafka to Spark") \
    .getOrCreate()

def create_batch(spark, topic, schema):
    df = spark.read \
      .format("kafka") \
      .option("kafka.bootstrap.servers", "pkc-gq2xn.asia-northeast3.gcp.confluent.cloud:9092") \
      .option("subscribe", topic) \
      .option("kafka.security.protocol", "SASL_SSL") \
      .option("kafka.sasl.jaas.config", "org.apache.kafka.common.security.plain.PlainLoginModule required username='RLP6RKHULZ4DSMWI' password='9Pwrkxqd28qoHWgRjQuTIdLRMCI5+/eGxSgX780BVcPysNlJprfuW6it7H01dk1B';") \
      .option("kafka.sasl.mechanism", "PLAIN") \
      .option("startingOffsets", "earliest") \
      .option("failOnDataLoss", "true") \
      .load() #DF load

    # Assuming the JSON array is in the "value" column as a string
    # Parse the JSON array using the defined schema
    parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("parsed_value"))

    # Explode the array to get individual records
    exploded_df = parsed_df.select(explode(col("parsed_value")).alias("record")).select("record.*")

    write_stream =  exploded_df.write \
      .format("bigquery") \
      .option("temporaryGcsBucket", f"gs://dh_pipeline_2/checkpoints/{topic}") \
      .option("table", f"gleaming-plate-422507-e9.dataset_dart_samsung.{topic}") \
      .mode("overwrite")
    return write_stream
topics = {}
for topic in topics:
    create_batch(spark, topic, schema_set[topic])