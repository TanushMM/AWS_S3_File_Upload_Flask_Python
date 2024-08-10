from flask import Flask, request, redirect, render_template, jsonify, url_for
import boto3
import os   
from dotenv import load_dotenv
load_dotenv()

S3_BUCKET = os.getenv('S3_BUCKET')
S3_REGION = os.getenv('S3_REGION')
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")

s3 = boto3.client(
    's3',
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files['file']
    if file.filename == '':
        return jsonify({"Message":"File not uploaded or File name is empty"})
    
    s3_file_name = file.filename
    try:
        s3.upload_fileobj(file, S3_BUCKET, s3_file_name, ExtraArgs={'ACL': 'public-read'})
        return redirect(url_for("uploaded_file", filename=s3_file_name))
    except Exception as e:
        return f"<h1>{e}</h1>"

@app.route("/uploaded/<filename>")
def uploaded_file(filename):
    file_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{filename}"
    return render_template('uploaded.html', file_url=file_url, filename=filename)

@app.route("/delete/<filename>")
def delete_file(filename):
    s3.delete_object(Bucket = S3_BUCKET, Key = filename)
    return render_template("deleted.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
