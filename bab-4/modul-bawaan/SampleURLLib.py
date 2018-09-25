'''
done
'''

import urllib.request
print("---------------sample1----------------")
html = urllib.request.urlopen('https://duckduckgo.com').read()
print(html)

print("---------------sample2----------------")
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
req = urllib.request.Request('https://duckduckgo.com', headers = headers)
html = urllib.request.urlopen(req).read()
print(html)