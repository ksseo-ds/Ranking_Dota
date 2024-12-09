import os
from peewee import *
from dotenv import load_dotenv

load_dotenv()

db_pass = os.getenv("DB_PASS") 

db_dota = PostgresqlDatabase('dota_rank',
                            user = 'postgres', 
                            password = db_pass,
                            host='localhost',
                            port=5432 )