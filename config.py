import os


class BaseConfig(object):
  SECRET_KEY = '80dbaac3590e4641bb2442b38a4fc638'
  database_name = 'expiry_dev'
  SQLALCHEMY_ECHO = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  @property
  def SQLALCHEMY_DATABASE_URI(self): 
    return f'postgresql://expiry@127.0.0.1:5432/{self.database_name}'
  
class DevConfig(BaseConfig):
  ENV = 'development'


class TestConfig(BaseConfig):
  ENV = 'test'
  DEBUG = True
  database_name = 'expiry_test'
  SQLALCHEMY_ECHO = True
  #consider making ENV='development and getting that one for free?

class ProdConfig(BaseConfig):
  ENV = 'production'
  SECRET_KEY = os.environ.get("SECRET_KEY")