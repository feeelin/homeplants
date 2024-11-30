from abc import ABC, abstractmethod
from typing import TypeVar

dataclass_type = TypeVar('dataclass_type')


class BaseQueryManager(ABC):
    data_class: dataclass_type

    @abstractmethod
    def get_all_rows(self):
        pass

    @abstractmethod
    def get_row_by_id(self, id: int):
        pass

    @abstractmethod
    def update_row(self, row):
        pass

    def transform_result_to_dataclass(self, result: tuple) -> list[dataclass_type]:
        result_translated = []
        for r in result:
            result_translated.append(self.data_class(*r))
        return result_translated
