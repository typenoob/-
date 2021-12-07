import requests
import base64
with open('test.png', 'rb') as f:
    url = 'http://127.0.0.1:5800/api/predict'
    data = {}
    data['data'] = str(base64.b64encode(f.read()), 'utf-8')
print(requests.post(url, data).text)
