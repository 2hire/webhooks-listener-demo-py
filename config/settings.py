class BaseConfig():

   API_PREFIX = '/api/prefix' # we can even handle different versions here
   
   TESTING = False
   DEBUG = False
   
class DevConfig(BaseConfig):

   ENV = 'development'
   SERVICE_NAME = 'flask-be-template-dev'
   
   SECRET_KEY = 'dev'
   
   DEBUG = True
   TESTING = True


# TODO add a proper SECRET _KEY
class TestConfig(BaseConfig):

   ENV = 'development'
   SERVICE_NAME = 'flask-be-template-test'
   
   TESTING = True
   DEBUG = True

# TODO add a proper SECRET _KEY
class ProductionConfig(BaseConfig):

   ENV = 'production'
   SERVICE_NAME = 'flask-be-template'
