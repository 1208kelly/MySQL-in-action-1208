import os
import datetime
import pymysql

# Get username from workspace
username = os.getenv('gh_user')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("""Create Table if not exists
                        friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists.
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
