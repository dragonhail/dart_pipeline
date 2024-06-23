[![한국어](https://img.shields.io/badge/README-%ED%95%9C%EA%B5%AD%EC%96%B4-blue?style=for-the-badge)](README.ko.md)

# DartAPI를 활용한 데이터 파이프라인
DartAPI, Kafka Confluent Cloud, Dataproc Spark, BigQuery를 이용한 데이터 파이프라인 구축

## 목차
- [프로젝트 설명](#프로젝트-설명)
- [전제 조건](#전제-조건)
- [아키텍처](#아키텍처)
- [dbt](#dbt)
  
## 프로젝트 설명 <a id="프로젝트-설명"></a>
이 프로젝트는 DartAPI를 사용하여 한국 시장에 상장된 기업들의 다양한 측면을 탐색합니다. Kafka 프로듀서를 통해 DartAPI 데이터를 Kafka 클러스터에 전송합니다. 생성된 주제는 Dataproc Spark 클러스터에서 consume하고 배치 처리 후, JSON 형태의 비정형 데이터를 정형 데이터프레임으로 변환합니다. 변환된 데이터프레임은 BigQuery 데이터 웨어하우스에 로드되어 dbt를 사용하여 분석됩니다. 전체 프로세스는 GKE에서 Airflow 스케줄러로 조정됩니다.<br>
프로젝트는 현재 진행 중이며, 아래에 설명되지 않은 기능들은 곧 추가될 예정입니다.

## 전제 조건 <a id="전제-조건"></a>
- GCP 계정
- Kafka Confluent Cloud 계정
- Dataproc Spark 클러스터
- BigQuery
- dbt-core
- GKE 클러스터에서 Airflow
- Cloud Function

## 아키텍처 <a id="아키텍처"></a>
![아키텍처 이미지](img.png)

## dbt <a id="dbt"></a>
이 프로젝트는 BigQuery 데이터 웨어하우스에서 데이터를 분석하기 위해 dbt를 사용합니다. [링크](https://github.com/dragonhail/dart_dbt)를 클릭하여 자세한 정보를 확인하세요.