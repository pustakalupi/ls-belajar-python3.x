'''
done
'''

import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

kursor = koneksi.cursor()

kursor.execute("CREATE DATABASE pustakalupi")