from Compressor import Compressor
from zipfile import ZipFile


class ZipCompressor(Compressor):
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        just_file_name = file_name.split('.')[0]
        with ZipFile(just_file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)
