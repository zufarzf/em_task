class Config:
    SECRET_KEY = 'd7873318b12f5eb86da0a2e758e0d51ecd759018237dcac2785cf4a3bc6f'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # например, 10MB
    UPLOAD_FOLDER = 'app/static/uploads'
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/database_name'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql-33ZF@localhost:3306/warehouse'


class TestingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False



CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,
    'def': DevelopmentConfig
}