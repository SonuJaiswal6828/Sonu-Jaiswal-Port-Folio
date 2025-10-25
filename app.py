from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# --- Email configuration ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jsonu77768@gmail.com'
app.config['MAIL_PASSWORD'] = 'fgxw vnvz dbds plxe'  # Gmail app password
app.config['MAIL_DEFAULT_SENDER'] = ('Portfolio Contact', 'jsonu77768@gmail.com')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message_body = request.form['message']

    msg = Message(subject=f"New Contact: {subject}", recipients=['jsonu77768@gmail.com'])
    msg.body = f"""
    You have a new message from your portfolio website:

    Name: {name}
    Email: {email}
    Subject: {subject}
    Message:
    {message_body}
    """

    mail.send(msg)
    return render_template('thankyou.html', name=name)


