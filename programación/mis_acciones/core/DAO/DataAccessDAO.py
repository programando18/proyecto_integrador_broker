from abc import ABC, abstractmethod


# REVISAR ËSTO, NO ESTA BIEN IMPLEMENTADO
class DataAccessDAO(ABC):

    @abstractmethod
    def execute_query(self, query: str, params=None):
        """Execute a given SQL query."""
        pass

    @abstractmethod
    def get_inversor_by_id(self, id_inversor: int):
        """Retrieve a single inversor record by its ID."""
        pass

    @abstractmethod
    def get_in(self, email: str, password: str):
        """Create a new inversor record with the given data."""
        pass

    @abstractmethod
    def update_inversor(self, id: int, data: dict):
        """Update the inversor record identified by ID with the new data."""
        pass

    @abstractmethod
    def delete_inversor(self, id: int):
        """Delete the inversor record identified by ID."""
        pass

    @abstractmethod
    def get_all_inversores(self):
        """Retrieve all inversor records."""
        pass
