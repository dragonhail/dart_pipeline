# DartAPI를 활용한 데이터 파이프라인
DartAPI, Kafka Confluent Cloud, Dataproc Spark, BigQuery를 이용한 데이터 파이프라인 구축

# 기능
* Open DartAPI를 사용하여 한국 증시에 상장된 기업들의 정보를 불러와 정리. 
* Kafka 프로듀서를 통해 DartAPI 데이터를 Kafka 클러스터 토픽에 전송
* 토픽은 Dataproc Spark 클러스터에서 consume하고 배치 처리 후, JSON 형태의 비정형 데이터를 정형 데이터프레임으로 변환
* 변환된 데이터프레임은 BigQuery 데이터 웨어하우스에 로드, dbt 적용
* Airflow on GKE 사용

## 아키텍처 <a id="아키텍처"></a>
![아키텍처 이미지](img.png)

## 문제점
* 카프카 필요성 의문
  * api 별 kafka 토픽 생성 비효율성
* api 자체의 데이터 결함
* airflow on gke 작동 안함 issue