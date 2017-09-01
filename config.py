class Config:
    SECRET_KEY = 'YATARTH IS A DINCHUCKS'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class DevelopmentMongoConnect(DevelopmentConfig):
    PYMONGO_DATABASE_URI = 'localhost:27017'
    PYMONGO_DB = 'assignment1'

class TestingConfig(Config):
    DEBUG = True

class TestingMongoConnect(TestingConfig):
    PYMONGO_DATABASE_URI = 'localhost:27017'
    PYMONGO_DB = 'restaurants'

class ProductionConfig(Config):
    pass

class ProductionMongoConnect(ProductionConfig):
    pass

config = {
    'development': DevelopmentMongoConnect,
    'testing': TestingMongoConnect,
    'production': ProductionMongoConnect,
    'default': DevelopmentMongoConnect
}