# Flask File Upload Application

This project is a simple web application built with Flask that allows users to upload files. The uploaded files are stored in an AWS S3 bucket, and users can download their files or delete them if needed. The application can containerized usign Docker and can be deployed on AWS Elastic Container Service.

## Features

- **File Upload:** Upload files directly from your browser.
- **File Download:** Download the uploaded file.
- **File Deletion:** Delete the uploaded file.
- **AWS S3 Integration:** Securely stores files in an AWS S3 bucket.
- **Dockerization:** The application can be Dockerized for easy deployment and scalability.

## Running it in your local machine [Linux] 
### Make sure you have the following installed 
- Docker Engine, if not install using `sudo apt install docker.io -y`
### Steps to run it locally
- clone the repository using `https://github.com/TanushMM/AWS_S3_File_Upload_Flask_Python.git` for HTTPS and `git@github.com:TanushMM/AWS_S3_File_Upload_Flask_Python.git` for SSH
- go to the cloned directory using `cd`
- Fill the `docker-compose.yaml` with the necessary environment variables that allows the Flask application to access AWS S3 bucket.
- run the following command `sudo docker-compose up` , this is will first build the docker image and then runs it as per the configurations provided in the `docker-compose.yaml` file.
- To access the running application go to `http://127.0.0.1:5000`

## Contents of **docker-compose.yaml** file
```
version: "3.9"

services:
  s3-python-boto3:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      S3_BUCKET: <replace with your bucket name>
      S3_REGION: <replace with the region on which your S3 bucker is hosted>
      S3_ACCESS_KEY: <replace with you IAM user Access Key>
      S3_SECRET_KEY: <replace with your IAM user Secret Key>
```

## Project Structure
├── application <br>
│&emsp;├── app.py <br>
│&emsp;└── templates <br>
│&emsp;&emsp;├── deleted.html <br>
│&emsp;&emsp;├── index.html <br>
│&emsp;&emsp;└── uploaded.html <br>
├── Dockerfile <br>
├── README.md <br>
├── docker-compose.yaml <br>
└── requirements.txt