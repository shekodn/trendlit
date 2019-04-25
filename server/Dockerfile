FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  python \
  apache2

COPY index.html /var/www/html/index.html

RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/

COPY test.py /usr/lib/cgi-bin
RUN chmod 755 /usr/lib/cgi-bin/test.py

# By default start up apache in the foreground, override with /bin/bash for interative.
CMD ["/usr/sbin/apache2ctl", "-D",  "FOREGROUND"]
