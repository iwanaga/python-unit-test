import requests
import json

class SampleClass:
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError("コンストラクタ引数にint型を指定してください")
        self.number = number
        self.http_request = requests

    def add(self, integer):
        self.number = self.number + integer
        return self.number

    def _http_get(self):
        return self.http_request.get('http://example.com/api/v1/foo')

    def get_http_message(self):
        return json.loads(self._http_get())
