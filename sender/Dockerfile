FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY sender_app.py /app/sender_app.py

CMD ["uvicorn", "sender_app:app", "--host", "0.0.0.0", "--port", "8000"]
