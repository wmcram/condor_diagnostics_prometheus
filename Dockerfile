FROM python:3.7-slim

RUN pip install flask

WORKDIR /metrics

CMD ["python", "serve.py"]