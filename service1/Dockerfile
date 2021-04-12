FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install Flask-SQLAlchemy
ENV DATABASE_URI=$DATABASE_URI
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]