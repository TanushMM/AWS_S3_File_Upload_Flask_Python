FROM python:3.9-slim

WORKDIR /

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /application/

EXPOSE 5000 

CMD ["python3", "app.py"]
