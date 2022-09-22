import requests
import json

page = requests.get('http://api.cctv.malangkota.go.id/records/cameras')

print(page.text)

page_json = page.json()

print(page_json)

for a in page_json:
    print(a)