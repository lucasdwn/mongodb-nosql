import os
import pymongo
import redis

from dotenv import load_dotenv
from pymongo.server_api import ServerApi

load_dotenv()
database_url = os.getenv('DATABASE_ACCESS')
redis_url = os.getenv('REDIS_URL')
redis_port = os.getenv('REDIS_PORT')
redis_password = os.getenv('REDIS_PASSWORD')

def connect():
    client = pymongo.MongoClient(database_url, server_api=ServerApi('1'))
    mydb = client.MercadoLivre
    return mydb

def connectRedis():
    client = redis.Redis(host=redis_url,
                   port=redis_port,
                   password=redis_password)
    return client