# Flask File Upload Application

This project is a simple web application built with Flask that allows users to upload files. The uploaded files are stored in an AWS S3 bucket, and users can download their files or delete them if needed. The application can containerized usign Docker and can be deployed on AWS Elastic Container Service.

## Features

- **File Upload:** Upload files directly from your browser.
- **File Download:** Download the uploaded file.
- **File Deletion:** Delete the uploaded file.
- **AWS S3 Integration:** Securely stores files in an AWS S3 bucket.
- **Dockerization:** The application can be Dockerized for easy deployment and scalability.

## Project Structure
├── application <br>
│&emsp;├── app.py <br>
│&emsp;└── templates <br>
│&emsp;&emsp;├── deleted.html <br>
│&emsp;&emsp;├── index.html <br>
│&emsp;&emsp;└── uploaded.html <br>
├── Dockerfile <br>
├── README.md <br>
└── requirements.txt

## Content structure of **.env** file
```
S3_BUCKET=<replace with your bucket name>
S3_REGION=<replace with the region on which your S3 bucker is hosted>
S3_ACCESS_KEY=<replace with you IAM user Access Key>
S3_SECRET_KEY=<replace with your IAM user Secret Key>
```
