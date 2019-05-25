FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  apache2 \
  python3-pip python3-dev \
  python3.7 \
  build-essential \
  python3.7 \
  wget

RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/

COPY . /usr/lib/cgi-bin

WORKDIR /usr/lib/cgi-bin

COPY server/index.html /var/www/html/index.html

RUN pip3 install -r requirements.txt

COPY server/*.py /usr/lib/cgi-bin/

RUN chmod 755 /usr/lib/cgi-bin/server.py

# By default start up apache in the foreground, override with /bin/bash for iterative.
CMD ["/usr/sbin/apache2ctl", "-D",  "FOREGROUND"]

# In order to BUILD and use an argument you need to include ARG NAME
# in your Dockerfile, otherwise the build args are not used.
# Reference: https://github.com/moby/moby/issues/18205#issuecomment-267401902
ARG RELEASE
