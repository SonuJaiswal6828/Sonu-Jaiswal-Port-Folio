from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# --- Email configuration using environment variables ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('jsonu77768@gmail.com')  # Gmail address
app.config['MAIL_PASSWORD'] = os.environ.get('fgxw vnvz dbds plxe')  # App password
app.config['MAIL_DEFAULT_SENDER'] = (os.environ.get('MAIL_SENDER_NAME', 'Portfolio Contact'),
                                     os.environ.get('MAIL_USERNAME'))

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message_body = request.form.get('message')

    msg = Message(subject=f"New Contact: {subject}", recipients=[app.config['MAIL_USERNAME']])
    msg.body = f"""
You have a new message from your portfolio website:

Name: {name}
Email: {email}
Subject: {subject}
Message:
{message_body}
"""
    try:
        mail.send(msg)
        return render_template('thankyou.html', name=name)
    except Exception as e:
        return f"Error sending email: {str(e)}"

# No app.run() needed for Vercel serverless
