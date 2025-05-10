import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64
from database import settings

def send_email(to_email: str, subject: str, body: str, qr_code_base64: str):
    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"

    # Create email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach body
    msg.attach(MIMEText(body, "plain"))

    # Attach QR code
    qr_code_data = base64.b64decode(qr_code_base64)
    qr_code_attachment = MIMEBase("application", "octet-stream")
    qr_code_attachment.set_payload(qr_code_data)
    encoders.encode_base64(qr_code_attachment)
    qr_code_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename=qr_code.png",
    )
    msg.attach(qr_code_attachment)

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())