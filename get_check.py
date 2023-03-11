import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()


class ScanCheck:
    """
        Класс для работы с чеком.
        ...
        Атрибуты
        --------
        url : str
            ссылка на proverkacheka
        token : str
            персональный токен
        last_responce : None
            последний полученный чек
        Методы
        ------
        get_json(qrraw: str) -> dict:
            Получаем чек в формате json

        save_check_to_json(filename:str = "info_check.json"):
            Сохраняем данные чека в формате json
        """
    def __init__(self):
        self.url = 'https://proverkacheka.com/api/v1/check/get'
        self.token = os.getenv('TOKEN')
        self.last_response = None

    def get_json(self, qrraw: str) -> dict:
        """Получаем данные чека и переводим в json"""
        data = {'token': self.token,
                'qrraw': qrraw}
        resp = requests.post(self.url, data=data)
        file_json = json.loads(resp.text)
        self.last_response = file_json
        return file_json

    def save_check_to_json(self, filename:str = "info_check.json"):
        """Сохраняем данные чека в формате json"""
        with open(filename, 'w') as f:
            json.dump(self.last_response, f, ensure_ascii=False, indent=2)