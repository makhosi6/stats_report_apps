FROM python:3.12
WORKDIR /app
RUN pip install Flask==3.1.0
RUN pip install SQLAlchemy==2.0.38
RUN pip install Flask-SQLAlchemy==3.1.1
RUN pip install pymysql
RUN pip install mysql-connector-python
COPY . .
CMD ["python", "run.py"]