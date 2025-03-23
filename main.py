import os
import smtplib
from email.mime.text import MIMEText

from flask import Flask, request, flash, redirect, url_for, render_template
from flask_mail import Mail, Message

secret_key = os.urandom(32)

app = Flask(__name__)
app.secret_key = secret_key

app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME="nvson.red@gmail.com",
    MAIL_PASSWORD="hnwy yjez wuzr jqoj"  #Mk ung dung google
)

mail = Mail(app)

@app.route("/")
def index():
    data = {
        "your_email": "nvson.red@gmail.com",
        "password": "hnwy yjez wuzr jqoj"
    }
    return render_template("index.html", data=data)

@app.route("/", methods=["GET", "POST"])
def send_email():
    if request.method == "POST":
        sender_email = request.form["sender_email"]
        # sender_password = request.form["sender_password"]
        recipient_email = request.form["recipient_email"]
        subject = request.form["subject"]
        body = request.form["body"]

        try:
            # Update the mail sender credentials dynamically
            app.config.update(
                MAIL_USERNAME=sender_email,
                # MAIL_PASSWORD=sender_password
            )
            msg = Message(subject=subject,
                          sender=sender_email,
                          recipients=[recipient_email])
            msg.body = body
            mail.send(msg)
            flash("Email sent successfully!", "success")
        except Exception as e:
            flash(f"Failed to send email: {str(e)}", "danger")
        return redirect(url_for("send_email"))

    return """
    Your HTML here (replace this string with the HTML template you posted above)
    """

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)