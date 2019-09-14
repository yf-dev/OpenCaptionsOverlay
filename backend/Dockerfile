FROM python:3.7.4-buster

RUN apt-get update && apt-get -y install \
    libpq-dev \
    pipenv && \
    apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*

RUN pip install virtualenv

COPY flask/Pipfile /var/www/flask/Pipfile
COPY flask/Pipfile.lock /var/www/flask/Pipfile.lock
WORKDIR /var/www/flask
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80
EXPOSE 443

CMD ["gunicorn", "--worker-class", "eventlet", "-w", "1", "-b", "0.0.0.0:80", "--forwarded-allow-ips", "*", "app:app"]
