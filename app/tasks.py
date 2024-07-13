import smtplib
from email.mime.text import MIMEText
from celery import Celery
from celery.utils.log import get_task_logger
from config import SMTP_SERVER, SMTP_PORT, SMTP_PASSWORD, FROM_EMAIL, BROKER_URL, RESULT_BACKEND

logger = get_task_logger(__name__)

celery_app = Celery('tasks', broker=BROKER_URL, backend=RESULT_BACKEND)

@celery_app.task
def send_email_task(to_email):
    msg = MIMEText("Promote Lanky asap!!!.")
    msg["Subject"] = "HNG_stage3 Task"
    msg["From"] = FROM_EMAIL
    msg["To"] = to_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(FROM_EMAIL, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, [to_email], msg.as_string())
            logger.info(f"Email sent to {to_email}")
    except Exception as e:
        logger.error(f"Failed to send email to {to_email}: {e}")
