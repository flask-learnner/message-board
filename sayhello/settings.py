import os
import sys
from sayhello import app

WIN=sys.platform.startswith('win')
if WIN :
    prefix='sqlite:///'
else :
    prefix='sqlite:////'

dev_db=prefix + os.path.join(os.path.dirname(__file__),'data.db')

SECRET_KEY=os.getenv('SECRET_KEY','secret string')
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URI',dev_db)
