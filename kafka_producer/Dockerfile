# 기반이 될 이미지 선택 (예: Python 3.8)
FROM python:3.12.4

# 작업 디렉토리 설정
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libfreetype6-dev \
    libpng-dev \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

# Python 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 스크립트 실행
CMD ["python", "produce.py"]
