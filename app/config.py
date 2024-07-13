import os
from dotenv import load_dotenv

load_dotenv()

BROKER_URL = os.getenv("BROKER_URL")
RESULT_BACKEND= os.getenv("RESULT_BACKEND")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL")
LOG_FILE = os.getenv("LOG_FILE")
