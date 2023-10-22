import smtplib,random
from email.message import EmailMessage

def send_mail(to,code):
    sender = 'webcasino80@gmail.com'
    pswd = 'ollonoroktajwvac'
    servername = 'smtp.gmail.com'
    
    server = smtplib.SMTP(servername, 587)
    server.starttls()
    
    msg = EmailMessage()
    text = 'Code to authentication is %d' % code
    msg['Subject'] = f'The contents of [number]'
    msg['From'] = sender
    msg['To'] = to
    msg.set_content(text)
    
    
    server.login(sender,pswd)
    server.send_message(msg)

def codeGenerator():
    return random.randint(100000,999999)
