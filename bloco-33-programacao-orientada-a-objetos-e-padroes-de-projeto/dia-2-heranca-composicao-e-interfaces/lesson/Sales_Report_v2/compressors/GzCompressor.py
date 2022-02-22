import gzip


class GzCompressor():
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        just_file_name = file_name.split('.')[0]
        with open(file_name, 'rb') as content:
            with gzip.open(just_file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)
