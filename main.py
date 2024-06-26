from flask import Flask, render_template, send_file, request
from flask_bootstrap import Bootstrap5
import smtplib
from datetime import datetime
import os
from email.mime.text import MIMEText

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
        subject = "Email from MyPortfolio"
        body = f"Name: {data['name']}\nEmail: {data['email']}\nMessage:{data['message']}"
        sender = OWN_EMAIL
        recipient = OWN_EMAIL
        password = OWN_PASSWORD
        send_email(subject, body, sender, recipient, password)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(subject, body, sender, recipient, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())


if __name__ == "__main__":
    app.run(debug=False, port=5001)
