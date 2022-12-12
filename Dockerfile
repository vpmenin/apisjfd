FROM mysql:8.0.31

COPY ./db/ /docker-entrypoint-initdb.d/