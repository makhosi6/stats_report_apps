import os

class Config:
    # Secret/security key  
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_d748df6b11c4'

    # Database 
    # 'mysql+pymysql://...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SUGAR_DATABASE_URL') or 'mysql+mysqlconnector://root:password@192.168.0.159:3306/sugarcrm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JSON_SORT_KEYS = False
    SQLALCHEMY_ECHO = True 

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}