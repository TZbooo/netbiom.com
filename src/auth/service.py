import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from passlib.context import CryptContext

from src.config import SMTP_SENDER_USERNAME, SMTP_SENDER_PASSWORD


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hasher:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)


def get_email_message(
    recipient: str,
    subject: str,
    message: str
) -> MIMEMultipart:
    email_message = MIMEMultipart()
    email_message['From'] = SMTP_SENDER_USERNAME
    email_message['To'] = recipient
    email_message['Subject'] = subject
    email_message.attach(MIMEText(message))
    return email_message


def send_email(recipient: str, message: str) -> None:
    email_message = get_email_message(
        recipient,
        'NetBiom web panel email confirmation',
        message
    )
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(SMTP_SENDER_USERNAME, SMTP_SENDER_PASSWORD)

    mailserver.sendmail(SMTP_SENDER_USERNAME, recipient, email_message.as_string())
    mailserver.quit()
