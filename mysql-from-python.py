import os
import pymysql

#Get username from workspace
username = os.getenv('gh_user')

#Connect to the database
connection = pymysql.connect(host = 'localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()