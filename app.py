from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.get("data")

        if not data:
            return "Please enter valid data"

        img = qrcode.make(data)
        file_path = "qr_code.png"
        img.save(file_path)

        return send_file(file_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)