from narwhals import String


class OrderManager:

    def __init__(self, ib, mode='paper'):
        self.ib = ib
        self.mode = mode.lower()
        if self.mode != ['paper', 'live']:
            raise Exception(f'Invalid mode : {mode}. Use paper or live')








