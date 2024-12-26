
from dotenv import dotenv_values

config = dotenv_values('config.txt')
import MySQLdb  # This is part of mysqlclient


# Establish connection using MySQLdb instead of mysql.connector
def conn():
    try:
        connection = MySQLdb.connect(
            host=config.get('host'),
            user=config.get('db_user'),
            password=config.get('db_password'),
            database=config.get('database'),
            port=int(config.get('port')) if config.get('port') else 3307  # Ensure port is an integer
        )
        print("Connected to the database")
        return connection
    except MySQLdb.Error as err:
        print(f"Error: {err}")
        return None
conn()
