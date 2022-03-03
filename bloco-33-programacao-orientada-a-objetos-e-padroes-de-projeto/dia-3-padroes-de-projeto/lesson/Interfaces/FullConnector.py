from Interfaces.ReadOnlyConnector import ReadOnlyConnector
from abc import abstractmethod


class FullConnector(ReadOnlyConnector):
    # def __init__(self, nome):
    #     self.__nome = nome

    @abstractmethod
    def count_request(self, token):
        pass
