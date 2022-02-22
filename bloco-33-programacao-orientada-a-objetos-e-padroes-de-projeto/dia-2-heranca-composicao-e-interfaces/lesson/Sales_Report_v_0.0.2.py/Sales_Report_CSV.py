import csv
from SalesReport import SalesReport


class SalesReportCSV(SalesReport):
    def serialize(self):
        with open(self.export_file + '.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.build())


report_sales = SalesReportCSV('meu_arquivo')

print(report_sales.serialize())
