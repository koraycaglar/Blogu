FROM python:3.9.2

WORKDIR /app

COPY logprod.py /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "logprod.py"]
