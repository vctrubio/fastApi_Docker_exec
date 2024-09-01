FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Define environment variable for Uvicorn logs (optional)
ENV LOG_LEVEL=info

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
