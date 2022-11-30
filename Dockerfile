FROM python:3.10.8-alpine
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
