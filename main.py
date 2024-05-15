from flask import Flask, render_template, send_file, request
from flask_bootstrap import Bootstrap5
import smtplib
from datetime import datetime
import os

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
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
