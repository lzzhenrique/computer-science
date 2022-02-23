from unittest import loader


class G3000LoaderAdapter:
    def __init__(self, loader):
        self.loader = loader

    def load_data(self):
        return [zip(loader.headers, row) for row in loader.rows]


class ReportAnalyzer:
    def __init__(self, loader):
        self.loader = loader

    def average(self):
        data = self.loader.load_data()
        total = sum(order['final_price'] for order in data)
        return total / len(data)
