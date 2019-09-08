import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgres://akytzteaimkxlw:f0cd397c45dce1092fb841f906f20127249ddde5e52781e8c664319ed1c5c5af@ec2-23-21-156-171.compute-1.amazonaws.com:5432/da6mkl1d5igvou'
    SQLALCHEMY_TRACK_MODIFICATIONS = False