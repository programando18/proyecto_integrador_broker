from abc import ABC, abstractmethod


class DataAccessPortaDAO(ABC):

    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def get_all(self, id: int):
        pass

    @abstractmethod
    def create(self, id: int):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, object):
        pass
