FROM python:3.12
WORKDIR /app
RUN pip install Flask==3.1.0
RUN pip install SQLAlchemy==2.0.38
COPY . .
CMD ["python", "run.py"]