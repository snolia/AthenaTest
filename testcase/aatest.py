import requests

url = "http://192.168.10.56:8763/ms-order-data/appOrder/topieces-pieces"

querystring = {"districtNo":"","serviceNo":"","pieces":"true","mixSearch":""}

headers = {
    'token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyLXR5cGUiOiJEWExYMDQiLCJ1c2VyLW5hbWUiOiLpmYjlj4zllpwiLCJ1c2VyLXBhcmFtIjoie1wiaXNBZG1pblwiOjF9IiwidXNlci1zdWJqZWN0aW9uIjoiMmJjMTJkYWUtNDFlMy0xMWU3LTk3ZDEtMDI0MmFjMTIwMDIxIiwidXNlci1pZCI6IjA2NGU3Nzc1LTQ1MWMtMTFlNy1iM2NkLTAwNTA1NjlmN2IwYyIsImlzcyI6IjEzOTc1MTg3NjU5IiwidXNlci1jb2RlIjoiMTM5NzUxODc2NTkiLCJleHAiOjE1MTI2MjcyNjIsImlhdCI6MTUxMDAzNTI2Mn0.wdqOnSjPrcNHiSJ0dntwBoA_gtPbL2LwYt4jZE5D094",
    'pagenum': "1",
    'pagesize': "20",
    'cache-control': "no-cache",
    'postman-token': "707b333a-decd-afad-f2d2-c7ff4ac09195"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)