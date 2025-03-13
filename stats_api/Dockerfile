FROM python:3.12

RUN apt-get update && apt-get install -y nginx supervisor

WORKDIR /app

RUN pip install Flask==3.1.0
RUN pip install SQLAlchemy==2.0.38
RUN pip install Flask-SQLAlchemy==3.1.1
RUN pip install pymysql
RUN pip install gunicorn
RUN pip install pyjwt
RUN pip install pillow
RUN pip install mysql-connector-python

COPY nginx.conf /etc/nginx/nginx.conf

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY . .

EXPOSE 5001

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]