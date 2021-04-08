FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5003
ENTRYPOINT ["python", "app.py"]