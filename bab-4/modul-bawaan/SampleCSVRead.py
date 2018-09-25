import csv

#cara pertama, sebagai list
with open('dummy-read.csv') as csvf:
    csvreader = csv.reader(csvf, delimiter=',')
    ctr = 0
    for baris in csvreader:
        print("id: " + baris[0] + ", gender: " + baris[1] + ", IP: " + baris[2])
        ctr += 1
    print("Total baris:" + str(ctr))

#cara kedua, sebagai dictionary
with open('dummy-read.csv') as csvf:
    csvreader = csv.DictReader(csvf, delimiter=',')
    ctr = 0
    for baris in csvreader:
        print("id: " + baris["id"] + ", gender: " + baris["gender"] + ", IP: " + baris["ip_address"])
        ctr += 1
    print("Total baris:" + str(ctr))