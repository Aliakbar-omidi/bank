class BankNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Job Not Found !!!")