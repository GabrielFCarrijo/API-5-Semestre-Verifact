import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        connection = psycopg2.connect(
            user=os.getenv('PG_USER'),
            password=os.getenv('PG_PASSWORD'),
            host=os.getenv('PG_HOST'),
            port=os.getenv('PG_PORT'),
            database=os.getenv('PG_DATABASE')
        )
        return connection
    except (Exception, Error) as error:
        print("Erro ao conectar ao PostgreSQL:", error)
