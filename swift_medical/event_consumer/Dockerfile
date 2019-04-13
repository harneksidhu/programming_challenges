FROM alpine:3.7

WORKDIR /home/app/

RUN apk add --no-cache gcc python3 python3-dev g++ make bash && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

RUN wget https://github.com/edenhill/librdkafka/archive/v1.0.0.tar.gz && \
    tar -xvf v1.0.0.tar.gz

WORKDIR /home/app/librdkafka-1.0.0

RUN ./configure && \
    make && \
    make install

ADD requirements.txt /home/app/

WORKDIR /home/app/

RUN pip3 install -r requirements.txt

ADD ./app /home/app/

ENTRYPOINT ["python3","-u", "app.py"]
