FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY receiver_app.py /app/receiver_app.py

CMD ["uvicorn", "receiver_app:app", "--host", "0.0.0.0", "--port", "8000"]
