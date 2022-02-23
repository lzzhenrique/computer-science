import json
from SalesReport import SalesReport


class SalesReportJSON(SalesReport):
    FILE_EXTENSION = '.json'

    def serialize(self):
        with open(self.get_export_file_name(), 'w') as file:
            json.dump(self.build(), file)

    def getLength(self):
        print(len(self.build()))
