[![Korean](https://img.shields.io/badge/README-Korean-blue?style=for-the-badge)](README.ko.md)

# Data Pipeline using DartAPI
A data pipeline using DartAPI, Kafka Confluent Cloud, Spark on Dataproc, Bigquery

## Table of Contents
- [Description](#description)
- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [dbt](#dbt)
  
## Description <a id="description"></a>
This project use DartAPI to explore varioous asepects of companies listed on Korea Market. A kafka producer produce topics to kafka cluster using DartAPI. Received topics are consumed and batch processed by Dataproc Spark cluster, which will transform json shaped topics to structured dataframes. After the transformation, the dataframes will be loaded into bigquery warehouse and analyzed using dbt. The whole process will be orchestrated using Airflow Scheduler on GKE.<br>
This project is still ongoing, and additional features not described below will be added soon.

## Prerequisites <a id="prerequisites"></a>
- A GCP account
- A Kafka Confluent Cloud account
- Dataproc Spark Cluster
- Bigquery
- dbt-core
- Airflow on GKE cluster
- Cloud Function

## Architecture <a id="architecture"></a>

## dbt <a id="dbt"></a>
This project use dbt to analyze data in bigquery warehouse. Click this [link](https://github.com/dragonhail/dart_dbt).
