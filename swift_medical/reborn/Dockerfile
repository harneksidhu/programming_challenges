# Basic flask container

FROM alpine:3.7

ADD requirements.txt /home/app/
WORKDIR /home/app/


RUN apk add --no-cache gcc python3 python3-dev musl-dev libffi libffi-dev postgresql-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install -r requirements.txt

ADD . /home/app/
WORKDIR /home/app/

EXPOSE 8000

#ENTRYPOINT ["gunicorn","--bind","0.0.0.0:8000","wsgi:app"]
#ENTRYPOINT ["gunicorn","-w","2","-b","0.0.0.0:8000","manage:app"]
ENTRYPOINT ["python3","-u", "manage.py", "run"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
