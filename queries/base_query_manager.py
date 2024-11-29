from abc import ABC, abstractmethod


class BaseQueryManager(ABC):
    @abstractmethod
    def get_all_rows(self):
        pass
