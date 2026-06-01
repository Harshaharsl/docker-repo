FROM python:3.12

WORKDIR /app

COPY h.py .

CMD ["python", "h.py"]
