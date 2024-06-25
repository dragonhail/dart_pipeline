# 기반이 될 이미지 선택 (예: Python 3.8)
FROM python:3.12.4

# 작업 디렉토리 설정
WORKDIR /app

# Copy the requirements file into the container at /app
#COPY kafka_producer/requirements.txt ./
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
#COPY kafka_producer/ ./
COPY . .

# 스크립트 실행
CMD ["python", "produce.py"]
