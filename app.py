from flask import Flask,render_template,request,send_file
from crypto_utils import encrypt_files,decrypt_files
import io
from cryptography.fernet import InvalidToken
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt",methods=["POST"])

def encrypt():
    file=request.files["image"]
    if file is None:
        return "no images uploaded"
    password=request.form["password"]
    data=file.read()
    encrypted=encrypt_files(data,password)
    filename=file.filename.split(".")[0]
    return send_file(io.BytesIO(encrypted),as_attachment=True,download_name=f"{filename}_encrypted.bin")

@app.route("/decrypt",methods=["POST"])
def decrypt():
    file=request.files["file"]
    if file is None:
        return "no file uploaded"
    password=request.form["password"]
    data=file.read()
    filename=file.filename.split(".")[0]
    try:
        decrypted=decrypt_files(data,password)
    except InvalidToken:
        return "Wrong password/Corrupted File"
    filename=file.filename.split(".")[0]
    return send_file(
        io.BytesIO(decrypted),as_attachment=True,download_name=f"{filename}_decrypted.jpg",mimetype="image/jpg")

if __name__ == "__main__": 
    app.run(debug=True)