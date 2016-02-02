FROM debian:latest

MAINTAINER iorch <j.martinezortega@gmail.com>

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    g++ \
    ca-certificates \
    python \
    python-dev \
    libmysqlclient-dev \
    python3 \
    python3-dev \
    python3-setuptools \
    liblapack-dev \
    libopenblas-dev \
    python-scipy \
    libatlas-base-dev \
    gfortran \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    beanstalkd \
    python3-tk \
    wget \
    unzip \
    git

RUN wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate && \
    python get-pip.py

# Add source
ADD . /root/prospera_digital_webhooks

RUN cd /root/prospera_digital_webhooks &&\
  pip install -r requirements.txt &&\
  cd ..

RUN python3 get-pip.py && \
    pip3 install -U setuptools &&\
    pip3 install requests &&\
    pip3 install pystalkd &&\
    pip3 install -Iv protobuf==3.0.0-alpha-1 && \
    pip3 install git+https://github.com/tgalal/yowsup@master

RUN git clone https://github.com/EliasKotlyar/yowsup-queue.git

# Default port
EXPOSE 5001

# Start the classifier service by default
CMD ["/root/prospera_digital_webhooks/start.sh"]
