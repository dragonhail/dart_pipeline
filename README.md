[![Korean](https://img.shields.io/badge/README-Korean-blue?style=for-the-badge)](README.ko.md)

# Data Pipeline using DartAPI
A data pipeline using DartAPI, Kafka Confluent Cloud, Spark on Dataproc, Bigquery

## Table of Contents
- [Prerequisites](#prerequisites)
- [Kafka Confluent Cloud](#kafkaconfluent)
- [Spark](#spark)
- [Bigquery](#bigquery)
- [dbt](#dbt)

## Prerequisites  <a id="prerequisites"></a>

- A GCP account
- A Kafka Confluent Cloud account
- Dataproc Spark Cluster
- Bigquery
- dbt-core

## Kafka Confluent Cloud <a id="kafkaconfluent"></a>

Create topic using confluent-cloud commands.
```bash
confluent kafka topic create <topic name> --cluster <cluster name>
```

## Spark <a id="spark"></a>
- You need to add --packages option to register kafka connector.
```bash
spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark-processing.py 
```

## Bigquery <a id="bigquery"></a>
```bash
git clone https://github.com/your/repository.git
cd repository
npm install
```
## dbt <a id="dbt"></a>

This project use dbt to analyze data in bigquery warehouse. Click this [link](https://github.com/dragonhail/dart_dbt).
