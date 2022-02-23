from abc import ABC, abstractclassmethod


class Connector(ABC):
    @abstractclassmethod
    def get_count(token):
        pass

    @abstractclassmethod
    def count_request():
        pass
