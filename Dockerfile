FROM python:3.8
RUN apt-get update && apt-get install -y lsb-release
RUN echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
       wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y poppler-utils awscli && \
    apt-get install -y libpq-dev git gcc postgresql-12 postgresql-client-12 postgresql-client-common python3-psycopg2

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get remove -y build-essential && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache

CMD ["/app/docker/start.sh"]

EXPOSE 8000
