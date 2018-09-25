'''
done
'''

import json

print("json ke python")
data = '{"nama" : "Pustakalupi", "produk":"buku", "jumlahProduk" : "3"}'
diPython = json.loads(data)
print(diPython)
print(diPython["nama"])
print(diPython["jumlahProduk"])

print("python ke json")
data1 = {
  "nama": "JSONConverter",
  "kode_versi": 40,
  "portabel": True,
  "dependencies": ("opencv","numpy"),
  "scripts": [
    {"start": "python", "arg": "jcon.py"},
    {"install": "install.sh"}
  ]
}

print(json.dumps(data1))