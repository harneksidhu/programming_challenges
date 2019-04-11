# Basic flask container

FROM alpine:3.7

ADD requirements.txt /home/app/
WORKDIR /home/app/


RUN apk add --no-cache gcc python3 python3-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install -r requirements.txt

ADD . /home/app/
WORKDIR /home/app/
RUN python3 manage.py create_db

EXPOSE 5000

ENTRYPOINT ["python3","-u", "manage.py", "run"]
