FROM python:3.9-buster
ENV LISTEN_PORT=5000
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]