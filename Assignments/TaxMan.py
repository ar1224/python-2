class TaxMan:

    def __init__(self, items, tax):
        self.items = items
        self.tax = tax
        self.total = 0.0

    def calc_total(self):
        for x in self.items:
            y = x['price']
            self.total += y
        newTax = float(self.tax.strip("%"))/100
        newTax *= self.total
        self.total += newTax

    def get_total(self):
        return self.total