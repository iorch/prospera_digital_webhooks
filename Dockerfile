FROM mxabierto/python

MAINTAINER iorch <j.martinezortega@gmail.com>

# Install dependencies
RUN \
  apt-get update && \
  apt-get install -y \
  git &&\
  rm -rf /var/lib/apt/lists/*

# Add source
ADD . /root/prospera_digital_webhooks

# Default port
EXPOSE 5001

# Start the classifier service by default
CMD ["/root/prospera_digital_webhooks/start.sh"]