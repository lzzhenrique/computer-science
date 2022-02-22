import csv
import json


class SalesReport():
    def __init__(self, format, export_file):
        self.format = format
        self.export_file = export_file + self.format

    def build(self):
        return [
            {
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
            },
            {
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
            },
        ]

    def serializeJSON(self):
        with open(self.export_file, 'w') as file:
            json.dump(self.build(), file)

    def serializeCSV(self):
        with open(self.export_file, "w") as file:
            writer = csv.writer(file)
            writer.writerows(self.build())


report_sales = SalesReport(format='.csv', export_file='meu_relatorio')
print(report_sales.export_file)
print(report_sales.serializeCSV())
