class ServiceException(Exception):
    def __init__(self, msg, *args):
        super().__init__(*args)
        self.msg = msg
