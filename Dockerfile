FROM docker.io/yuba/python3-oracle-pg-pandas

MAINTAINER TimWells 

COPY ./build /home/build
COPY ./src /home/src
COPY ./db.sqlite3 /home/db.sqlite3

WORKDIR /home/src

RUN apt-get install libaio1

RUN pip install -i https://pypi.douban.com/simple/ -r ../build/requirements.txt

RUN python manage.py collectstatic

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD gunicorn -c gun.py findtofix.wsgi:application