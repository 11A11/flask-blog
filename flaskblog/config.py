import os,json

class Config:
    # save locally, or hardcode. If hardcoded, gitignore this.
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # enter your own
    MAIL_USERNAME = os.environ.get('EMAIL_USER') 
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
