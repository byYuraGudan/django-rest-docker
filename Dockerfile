FROM python:3.8

RUN apt-get update -y
RUN apt-get -y install postgresql-client default-libmysqlclient-dev unixodbc-dev

WORKDIR /web

COPY requirements.txt /web/requirements.txt
RUN pip install -r requirements.txt

COPY . /web
EXPOSE 8001

CMD ['python manage.py migrate']
