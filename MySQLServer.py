import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",       # Change if your DB host is different
        user="root",            # Change to your MySQL username
        password="gloria@mysql25" # Change to your MySQL password
    )

    cursor = connection.cursor()

    # Create database (if not exists, handle it gracefully)
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist")
    else:
        print(f"Error: {err}")
finally:
    # Clean up: Close cursor and connection if they were opened
    try:
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
    except NameError:
        pass
