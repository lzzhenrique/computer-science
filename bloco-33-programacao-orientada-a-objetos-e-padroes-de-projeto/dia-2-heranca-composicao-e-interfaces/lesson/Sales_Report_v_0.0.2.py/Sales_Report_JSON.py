import json
from SalesReport import SalesReport


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)

    def getLength(self):
        print(len(self.build()))


report_sales = SalesReportJSON('meu_arquivo')
print(report_sales.getLength())
