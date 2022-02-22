import csv
from SalesReport import SalesReport


class SalesReportCSV(SalesReport):
    FILE_EXTENSION = '.csv'

    def serialize(self):
        with open(self.get_export_file_name(), 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.build())

    def getLength(self):
        print(len(self.build()))


report_sales = SalesReportCSV('meu_arquivo')

print(report_sales.serialize())