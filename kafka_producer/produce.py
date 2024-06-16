import requests
import json
import time
from datetime import datetime
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer
from api_url import *

def read_config():
  # reads the client configuration from client.properties
  # and returns it as a key-value map
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config

# producer and consumer code here
config = read_config()

# Kafka Producer 생성
producer = Producer(config)

# API 호출 함수
def call_api(url, params):
    response = requests.get(url, params=params)
    result = response.json().get('list', [])
    if response.status_code == 200:
        return result

# Kafka로 데이터 전송
def produce_to_kafka(topic, data):
    producer.produce(topic, value=json.dumps(data))
    producer.flush()
    print("Finished Producing")

# API 호출 및 데이터 Kafka로 전송
def main():
    dart_api_key = 'e4b249b5d47019872ca796f46fa6370ff2384df3'
    years = ['2019', '2020', '2021', '2022', '2023']  # 데이터 수집할 연도 리스트
    corp_list = ['00126380', ] # 삼성전자의 corp_code
    reprt_code = '11013' # 11011: 1분기보고서, 11012: 반기보고서, 11013: 3분기보고서, 11014: 사업보고서
    for corp_code in corp_list:
        for year in years:
            for topic, url in annual_repo.items():
                params = {
                'crtfc_key': dart_api_key,
                'corp_code': corp_code,
                'bsns_year': year,
                'reprt_code': reprt_code
                }

                # OpenDART API 호출
                data = call_api(url, params)
                if data:
                    print(f"API 호출 성공: {topic} - {year} - {reprt_code}")
                    produce_to_kafka(topic, data) # Kafka로 데이터 전송
                else:
                    print(f"API 호출 실패: {topic} - {year} - {reprt_code}")
main()