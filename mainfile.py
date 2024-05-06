import requests

url = "https://api.le-systeme-solaire.net/rest/bodies/?data&exclude&order&page&rowData"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
