FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements/backend.in

CMD ["python", "spaceship/main.py"]

