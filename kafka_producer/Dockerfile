# 기반이 될 이미지 선택 (예: Python 3.8)
FROM python:3.12.4-alpine

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일들을 이미지로 복사 (예시로 client.properties, api_url.py, requirements.txt 추가)
COPY . .

# Python 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 스크립트 실행
CMD ["python", "produce.py"]
