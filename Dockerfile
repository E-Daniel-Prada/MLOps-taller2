FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ls -R /app

ENV PYTHONPATH=/app

EXPOSE 8888 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8989"]