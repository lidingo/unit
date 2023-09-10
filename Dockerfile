FROM unit:1.31.0-python3.11

COPY ./*.pem  /docker-entrypoint.d/
COPY ./*.json /docker-entrypoint.d/
COPY ./*.sh   /docker-entrypoint.d/

WORKDIR /www
COPY *.py /www/

EXPOSE 8080
