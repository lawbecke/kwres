class Listing:
    def __init__(self, mls_number):
        self.mls_number = mls_number

    def to_csv(self):
        return str(self.mls_number)
