FROM python:3.14-slim

WORKDIR /app

# Install system dependencies
# build-essential for compiling extensions
# libgl1 and libglib2.0-0 for opencv-python (used by docling -> rapidocr)
# RUN apt-get update \
#     && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .

RUN pip install --no-cache-dir uv

# RUN pip install --no-cache-dir -r requirements.txt
RUN uv sync

COPY src/ src/

# Create logs directory
RUN mkdir -p logs

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

