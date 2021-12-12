import requests
import base64


def encode(file):
    with open(file, 'rb') as f:
        data = {}
        data['data'] = str(base64.b64encode(f.read()), 'utf-8')
    return data


def predict(data):
    url = 'http://1.117.250.49:5800/api/predict'
    return(requests.post(url, data).text)


if __name__ == '__main__':
    print(predict(encode('./mmm/test.png')))
