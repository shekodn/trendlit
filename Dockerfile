FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  apache2 \
  python3-pip python3-dev \
  python3.7 \
  build-essential \
  python3.7 \
  wget
  # sudo add-apt-repository ppa:deadsnakes/ppa


  # python3-dev \
  # && cd /usr/local/bin \
  # && ln -s /usr/bin/python3 python \
  # && pip3 install --upgrade pip

# WORKDIR /tmp
# RUN wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
# RUN tar -xf Python-3.7.2.tar.xz
# RUN cd Python-3.7.2
# # RUN ./configure --enable-optimizations
# RUN make -j 1
# RUN make altinstall

COPY server/index.html /var/www/html/index.html

RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/

COPY server/test.py /usr/lib/cgi-bin
RUN chmod 755 /usr/lib/cgi-bin/test.py

COPY . /usr/lib/cgi-bin
RUN chmod 755 /usr/lib/cgi-bin/main.py

WORKDIR /usr/lib/cgi-bin

# By default start up apache in the foreground, override with /bin/bash for interative.
CMD ["/usr/sbin/apache2ctl", "-D",  "FOREGROUND"]
