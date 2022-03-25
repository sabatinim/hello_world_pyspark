FROM ubuntu:22.04 AS base

RUN apt-get update && \
    apt-get install -y default-jdk scala wget vim software-properties-common python3 python3-pip curl unzip libpq-dev build-essential libssl-dev libffi-dev python3-dev&& \
    apt-get clean

FROM base

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./jobs /code/jobs
ENV PYSPARK_PYTHON=python3