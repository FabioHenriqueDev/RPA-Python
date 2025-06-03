import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


def enviar_email(email):
    load_dotenv()
    smtp_server = 'smtp.gmail.com' 
    smtp_port = 587 
    sender_email = os.environ["email"]
    sender_password = os.environ["senha_app"]

    # Compondo o e-mail
    msg = MIMEMultipart()
    msg['Subject'] = 'Bem-vindo(a) ao nosso sistema! 🎉'
    msg['From'] = sender_email
    msg['To'] = email


    html = f"""
            <html>
            <body style="font-family: Arial">
                <h1 style="color: blue;">Olá</h1>
                <img src="https://i.pinimg.com/736x/27/68/3e/27683e7872af4e367e2f27e9efdd1993.jpg" alt="Boas-Vindas" style="width:100%;max-width:600px;height:auto;">
                <h2>Esse email ép ara teste.</h2>
            </body>
            </html>
        """

    msg.attach(MIMEText(html, 'html'))

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
        print('Email Enviado com Sucesso')