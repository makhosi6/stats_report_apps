FROM python:3.12
WORKDIR /app
RUN pip install Flask==3.1.0
RUN pip install SQLAlchemy==3.1.2
COPY . .
CMD ["python", "app.py"]