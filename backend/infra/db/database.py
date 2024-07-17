import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_new_client():
    try:
        client = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST'), 
            port=os.getenv('POSTGRES_PORT'),       
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            dbname=os.getenv('POSTGRES_DB')
        )
        return client
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        raise

def query(query_object):
    client = None
    try:
        client = get_new_client()
        cursor = client.cursor()
        cursor.execute(query_object)
        result = cursor.fetchall()
        return result
    except Exception as error:
        print(error)
        raise
    finally:
        if client:
            client.close()
