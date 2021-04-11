FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install Flask-SQLAlchemy
EXPOSE 5000
ENV DATABASEURI=${DATABASEURI}
ENTRYPOINT ["python", "app.py"]