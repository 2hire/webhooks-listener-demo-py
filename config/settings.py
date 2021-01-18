import os 

class BaseConfig():

   API_PREFIX = '/api/wld' # we can even handle different versions here
   
   TESTING = False
   DEBUG = False
   
   SECRET = os.environ.get('SECRET', "thisIsARandomString")

class DevConfig(BaseConfig):

   ENV = 'development'
   SERVICE_NAME = 'wld-dev'
   
   SECRET_KEY = 'dev'
   
   DEBUG = True
   TESTING = True


# TODO add a proper SECRET _KEY
class TestConfig(BaseConfig):

   ENV = 'development'
   SERVICE_NAME = 'wld-test'
   
   TESTING = True
   DEBUG = True

# TODO add a proper SECRET _KEY
class ProductionConfig(BaseConfig):

   ENV = 'production'
   SERVICE_NAME = 'wld'
