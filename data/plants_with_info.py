from dataclasses import dataclass


@dataclass
class PlantWithInfo:
    plant_id: int
    info_id: int
    age: int
    _1: int
    name: int
    class_id: int
    _2: int
    class_name: str
    soil_type: str
    replanting_time: str
    feed_type: str
    feed_time: str
    winter_water_regime: str
    summer_water_regime: str

    def __str__(self):
        return f"{self.name}. {self.age} лет. Класс {self.class_name}"
