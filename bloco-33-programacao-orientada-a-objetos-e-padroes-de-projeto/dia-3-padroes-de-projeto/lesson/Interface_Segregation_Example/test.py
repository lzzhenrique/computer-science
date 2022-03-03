from Interfaces.FullConnector import FullConnector

# Dessa forma, a classe abaixo (henranca de FullConnector), pode ser intanciada


class SQLConnector(FullConnector):

    def count_request(self, token):
        print(token)

    def get_count(self, token):
        print(self)


# Do jeito abaixo, NAO FUNCIONA!!!


class SQLConnectorFail(FullConnector):

    def count_req(self, token):
        print(token)


teste_fail = SQLConnectorFail()
