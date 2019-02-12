from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisasecret"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "example@gmail.com"
app.config["MAIL_PASSWORD"] = "password"


mail =Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def service():
    return render_template('services.html')


@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        comment = request.form['messages']
        mailformat = '<h3> Name : </h3>' + name +'<h3>Email :</h3>' + email + '<h3>Subject :</h3>' + subject + '<h2>Message :</h2>' + comment
        msg = Message(subject= name ,html=mailformat, sender='gphileto@gmail.com', recipients=['gphileto@gmail.com'])
        mail.send(msg)
        flash('Thank you for sending us a message. Our specialists will contact you as soon as possible.')
        return redirect(url_for('index'))


if '__main__' == __name__:
    app.run(debug=True)
