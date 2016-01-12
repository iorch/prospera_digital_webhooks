FROM debian:latest

MAINTAINER iorch <j.martinezortega@gmail.com>

RUN apt-get update -y && \
    apt-get install -y python \
    python-dev \
    libmysqlclient-dev \
    liblapack-dev \
    libopenblas-dev \
    python-scipy \
    libatlas-base-dev \
    gfortran \
    wget

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    pip install -U setuptools

# Add source
ADD . /root/prospera_digital_webhooks

RUN cd /root/prospera_digital_webhooks &&\
  pip install -r requirements.txt

# Default port
EXPOSE 5001

# Start the classifier service by default
CMD ["/root/prospera_digital_webhooks/start.sh"]
