'''
done
'''

import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pustakalupi"
)

kursor = koneksi.cursor()

kursor.execute("SELECT * FROM books")

results = kursor.fetchall()

for x in results:
  print(x)