from Interface.Connector import Connector
pyredis = {}


class RedisConnector(Connector):
    def __init__(self, address, port):
        self.db = pyredis.connect(address, port)
        print(f'criada uma conexao em {address}: {port}')

    def get_count(token, self):
        result = self.search(token)
        amount = result.get("access_count", None)
        return amount

    def update_count(token, self):
        amount = self.get_count()
        if amount is None:
            self.db.insert({token: 1})
        else:
            self.db.insert({token: amount+1})
