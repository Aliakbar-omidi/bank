class BankNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Bank Not Found !!!")