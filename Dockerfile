FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi

COPY main.py .

EXPOSE 80
CMD ["fastapi", "run", "main.py", "--port", "80" ]
