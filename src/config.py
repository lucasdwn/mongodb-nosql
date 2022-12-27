import os
import pymongo

from dotenv import load_dotenv
from pymongo.server_api import ServerApi

load_dotenv()
database_url = os.getenv('DATABASE_ACCESS')

def connect():
    client = pymongo.MongoClient(database_url, server_api=ServerApi('1'))
    mydb = client.MercadoLivre
    return mydb
