# 기반이 될 이미지 선택 (예: Python 3.8)
FROM python:3.12.4

# 작업 디렉토리 설정
WORKDIR /app

COPY requirements.txt .

# Python 패키지 설치
RUN pip install -r requirements.txt

# 필요한 파일들을 이미지로 복사 (예시로 client.properties, api_url.py, requirements.txt 추가)
COPY . .

# 스크립트 실행
CMD ["python", "produce.py"]
