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

sql = "INSERT INTO books (title, isbn) VALUES (%s, %s)"
val = ("Belajar Python 3 untuk SD", "87879879879")
kursor.execute(sql, val)

koneksi.commit()

print(kursor.rowcount, "row diinsert.")
print("last row ID:", kursor.lastrowid)