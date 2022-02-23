from lesson.Interfaces.FullConnector import Connector
pysql = {}


class SqlConnector(Connector):
    def __init__(self, address, port):
        self.db = pysql.connect(address, port)
        print(f'criada uma conexao em {address}: {port}')

    def get_count(token, self):
        query = f'SELECT count FROM Access WHERE token={token};--'
        self.db.execute(query)

    def count_request(token, self):
        query = f'UPDATE access SET count = count+=1 WHERE token={token};--'
        self.db.execute(query)
