'''
done
'''

import sys
#import os #coba aktifkan dan lihat bedanya di "modul yang telah dimuat"

print("arguments: ")
for i in sys.argv:
    print(i)

print("modul yang telah dimuat:")
print(sys.modules.keys())

print('isi PYTHONPATH: ', sys.path, '.\n')

print("tulis apapun di sini: ")
user_input = sys.stdin.readline()
print("Input : " + user_input)