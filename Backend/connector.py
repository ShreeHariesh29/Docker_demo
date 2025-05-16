import pymysql
import pymysql.cursors
import os

def DB_Connection ():
    try:
        connector = pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', '1234'),
            database=os.getenv('DB_NAME', 'newecommerce'),
            port=int(os.getenv('DB_PORT', '3306')),
            cursorclass=pymysql.cursors.DictCursor,

        )
        return connector
    except pymysql.MySQLError as e:
        raise Exception("Error in connecting with data base") from e