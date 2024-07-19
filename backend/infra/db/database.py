import os
from dotenv import load_dotenv
import psycopg2

class Database():
    load_dotenv()

    def _get_new_client(self):
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

    def query(self, query_object):
        client = None
        try:
            client = self._get_new_client()
            cursor = client.cursor()
            cursor.execute(query_object)
            if cursor.description:  
                result = cursor.fetchall()
            else:
                result = None
            client.commit()  
            return result
        except Exception as error:
            print(error)
            raise
        finally:
            if client:
                client.close()
