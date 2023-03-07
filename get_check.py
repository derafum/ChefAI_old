"""import requests
import json
url = 'https://proverkacheka.com/api/v1/check/get'
data={'token':'20253.Umk1V1xWs9M87DoWY','qrraw': 't=20230306T1324&s=59.98&fn=7281440500232639&i=8355&fp=3680124697&n=1'}
resp = requests.post(url, data=data)
print(resp.text)"""
import requests
import json
import os
# создать модуль сканирования в основной ветке
from dotenv import load_dotenv

load_dotenv()


class ScanCheck:
    def __init__(self):
        self.url = 'https://proverkacheka.com/api/v1/check/get'
        self.token = os.getenv('token')
    # получаем в str данные чека и переводим в json
    def get_json(self, qrraw: str):
        data = {'token': self.token,
                'qrraw': qrraw}
        resp = requests.post(self.url, data=data)
        file_json = json.loads(resp.text)
        return file_json
    # сохраняем данные чека в виде json
    def save_check_to_json(self, file_json):
        with open('info_check.json', 'w') as f:
            json.dump(file_json, f)