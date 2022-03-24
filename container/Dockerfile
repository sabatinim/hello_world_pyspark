FROM openjdk:11.0.4-slim-buster

RUN apt update  \
 && apt -y install --no-install-recommends python3 python3-pip python3-setuptools \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
RUN ln -s /usr/bin/python3 /usr/bin/python