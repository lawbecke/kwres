import string

class Listing:
    def __init__(self, mls_number, price):
        self.mls_number = mls_number
        self.price = price

    def to_csv(self):
        return string.join([
            str(self.mls_number),
            str(self.price)
        ], ", ")
