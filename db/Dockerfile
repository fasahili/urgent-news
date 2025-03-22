FROM postgres:latest
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_DB=newsDB
COPY init.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
