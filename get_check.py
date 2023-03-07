import os

import json
import requests


class ScanCheck:
    def __init__(self):
        self.url = 'https://proverkacheka.com/api/v1/check/get'
        self.token = os.getenv('TOKEN')
        self.last_response = None

    def get_json(self, qrraw: str):
        """Получить результат проверки чека в json формате"""
        data = {'token': self.token,
                'qrraw': qrraw}
        self.last_response = requests.post(self.url, data=data)
        return json.loads(self.last_response.text)

    def save_check_to_json(self, filename: str = 'info_check.json'):
        """Сохраняем данные чека в виде json"""
        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump(json.loads(self.last_response.text), file)
