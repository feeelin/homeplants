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

    @abstractmethod
    def insert_row(self, row: dict):
        pass

    @abstractmethod
    def delete_row(self, id: int) -> None:
        pass

    def transform_result_to_dataclass(self, result: tuple) -> list[dataclass_type]:
        result_translated = []
        for r in result:
            result_translated.append(self.data_class(*r))
        return result_translated

    @staticmethod
    def build_values_string(row: dict) -> str:
        to_build = []
        for key, value in row.items():
            if key != "id":
                if value is not None:
                    to_build.append(f"{key} = '{value}'")
                else:
                    to_build.append(f"{key} = NULL")
        values = ", ".join(to_build)
        return values

    @staticmethod
    def build_values_string_without_keys(row: dict) -> str:
        to_build = []
        for key, value in row.items():
            if key != "id":
                if value is not None:
                    to_build.append(f"'{value}'")
                else:
                    to_build.append(f"NULL")
        values = ", ".join(to_build)
        return values

    @staticmethod
    def get_values_names_string(row: dict) -> str:
        all_keys = list(row.keys())
        if "id" in all_keys:
            all_keys.remove("id")
        return ", ".join(all_keys)
