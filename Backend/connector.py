# import pymysql
# import pymysql.cursors
# import os

# def DB_Connection ():
#     try:
#         connector = pymysql.connect(
#             host=os.getenv("MYSQL_HOST", "db"),  # 'db' is the service name from docker-compose.yml
#             user=os.getenv("MYSQL_USER", "root"),
#             password=os.getenv("MYSQL_PASSWORD", "1234"),
#             database=os.getenv("MYSQL_DATABASE", "ecommerce"),
#             port=int(os.getenv("MYSQL_PORT", 3306)),
#             cursorclass=pymysql.cursors.DictCursor,
#         )
#         return connector
#     except pymysql.MySQLError as e:
#         raise Exception("Error in connecting with data base") from e

import pymysql
import pymysql.cursors
import os
import time

def DB_Connection(max_retries=5, delay=3):
    attempt = 0
    while attempt < max_retries:
        try:
            print(f"Attempting MySQL connection ({attempt + 1}/{max_retries})...")
            connector = pymysql.connect(
                host=os.getenv("MYSQL_HOST", "db"),
                user=os.getenv("MYSQL_USER", "root"),
                password=os.getenv("MYSQL_PASSWORD", "1234"),
                database=os.getenv("MYSQL_DATABASE", "ecommerce"),
                port=int(os.getenv("MYSQL_PORT", 3306)),
                cursorclass=pymysql.cursors.DictCursor,
            )
            print("✅ MySQL connection successful.")
            return connector
        except pymysql.MySQLError as e:
            print(f"❌ Connection failed: {e}")
            attempt += 1
            time.sleep(delay)
    raise Exception("❌ Could not connect to MySQL after multiple attempts.")
