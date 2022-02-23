from compressors.ZipCompressor import ZipCompressor
from Sales_Report_JSON import SalesReportJSON

sales_report_GZ = SalesReportJSON('relatorio_gz')
sales_report_ZIP = SalesReportJSON('relatorio_zip', ZipCompressor())

sales_report_GZ.compress()
sales_report_ZIP.compress()
