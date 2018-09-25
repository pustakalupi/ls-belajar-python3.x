'''
done

sebelumnya, install mysql connector:
pip3 install mysql-connector

kemudian install mysql server.

semua kode mysql berjalan dengan asumsi mysql connector sudah terinstall.
'''

import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

print(koneksi)