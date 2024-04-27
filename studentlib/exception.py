class MyException(Exception):

    def __init__(self, x, message):
        super().__init__()
        self.message = message
        self.x = x

    def get_message(self):
        return self.message
