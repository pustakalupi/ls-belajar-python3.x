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

kursor.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), isbn VARCHAR(255))")