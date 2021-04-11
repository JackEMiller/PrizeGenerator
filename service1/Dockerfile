FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install Flask-SQLAlchemy
EXPOSE 5000
ENV DATABASE_URI=${DATABASE_URI}
ENTRYPOINT ["python", "app.py"]