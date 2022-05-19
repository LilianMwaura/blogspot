import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wambui:db_password@localhost:5432/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)  
    pass
    
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wambui:db_password@localhost:5432/blog'
    SECRET_KEY = 'thisismysecret'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 