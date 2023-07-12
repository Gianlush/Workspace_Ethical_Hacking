# docker build -t unical-unsecure-mail . && docker run -p 5000:5000 -p 8025:8025 unical-unsecure-mail

FROM ubuntu:22.04

RUN apt-get update && apt-get install python3 python3-pip openssh-server -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

ARG FLAG=ETH{uns3cur3_s4n171z4710n_uns3cur3_m41l}
RUN echo ${FLAG} > /flag.txt
RUN chmod 777 /flag.txt


RUN useradd -m admin && echo "admin:admin" | chpasswd
RUN adduser --disabled-password --gecos "" user
RUN chown user:user /usr/sbin/sshd

COPY . .

CMD service ssh start && flask run