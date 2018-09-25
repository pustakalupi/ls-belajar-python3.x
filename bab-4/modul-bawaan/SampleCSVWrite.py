import csv

#cara pertama
with open('dummy-write.csv', mode='w') as csvf:
    csvw = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvw.writerow(['id', 'gender', 'ip_address'])
    csvw.writerow(['1', 'Male', '127.0.0.1'])

#cara kedua
with open('dummy-write-1.csv', mode='w') as csvf:
    namaKolom = ['id', 'gender', 'ip_address']
    csvw = csv.DictWriter(csvf, fieldnames=namaKolom)
    csvw.writeheader()
    csvw.writerow({'id': '1', 'gender' : '"Female"', 'ip_address' : '192.168.0.1'})