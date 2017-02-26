class SampleClass:
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError("コンストラクタ引数にint型を指定してください")
        self.number = number

    def add(self, input):
        self.number = self.number + input
        return self.number

    def http_get(self):
        return True
