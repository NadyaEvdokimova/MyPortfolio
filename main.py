from flask import Flask, render_template, send_file, request
from flask_bootstrap import Bootstrap5
import smtplib
from datetime import datetime
import os
import socket

app = Flask(__name__)
Bootstrap5(app)
OWN_EMAIL = os.environ.get('EMAIL')
OWN_PASSWORD = os.environ.get('PASSWORD')


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/download')
def download_cv():
    path = "Nadja Evdokimova Junior Python Developer.docx"
    return send_file(path, as_attachment=True)


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, message):
    try:
        smtp_server = "smtp.gmail.com"
        port = 587
        socket.create_connection((smtp_server, port), timeout=10)
        print("Connection to SMTP server successful")
    except Exception as e:
        print(f"Failed to connect to SMTP server: {e}")
    # email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(OWN_EMAIL, OWN_PASSWORD)
    #     connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=False, port=5001)
