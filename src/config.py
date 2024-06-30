import os
from dotenv import load_dotenv


load_dotenv()

SECRET = os.getenv('SECRET')

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')


DB_HOST_TEST = os.getenv('DB_HOST_TEST')
DB_NAME_TEST = os.getenv('DB_NAME_TEST')
DB_PASS_TEST = os.getenv('DB_PASS_TEST')
DB_PORT_TEST = os.getenv('DB_PORT_TEST')
DB_USER_TEST = os.getenv('DB_USER_TEST')


SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
