FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
# build-essential for compiling extensions
# libgl1-mesa-glx and libglib2.0-0 for potential image processing dependencies (cv2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

# Create logs directory
RUN mkdir -p logs

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

