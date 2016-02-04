FROM debian:latest

MAINTAINER iorch <j.martinezortega@gmail.com>

RUN apt-get update -y && \
    apt-get install -y python3 \
    python3-dev \
    python3-setuptools \
    wget \
    git \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    beanstalkd \
    python3-tk

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    pip install -U setuptools

RUN pip install pystalkd

RUN pip install -Iv protobuf==3.0.0-alpha-1

RUN pip install git+https://github.com/tgalal/yowsup@master

RUN git clone https://github.com/EliasKotlyar/yowsup-queue.git

ADD start.sh .

CMD ["/start.sh"]
