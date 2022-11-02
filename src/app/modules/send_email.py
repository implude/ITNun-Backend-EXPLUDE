from dotenv import load_dotenv   
load_dotenv() #load .env fi
import smtplib, os
from email.mime.text import MIMEText

GOOGLE_APP_PASSWORD = os.environ["GOOGLE_APP_PASSWORD"]
EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]

def send_verification_email(email, email_verification_code):

    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.ehlo()

    smtp.starttls()

    smtp.login(EMAIL_ADDRESS, GOOGLE_APP_PASSWORD)

    msg = MIMEText(email_verification_code)
    msg['Subject'] = '잇는 | 이메일 인증'

    smtp.sendmail(EMAIL_ADDRESS, email, msg.as_string())

    smtp.quit()
