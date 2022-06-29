FROM python:3.7-alpine

WORKDIR /app/

RUN mkdir /app/logs/

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

RUN ["python", "mqtt_sub.py", "--conf", "sub_conf.json"]


