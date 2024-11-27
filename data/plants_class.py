from dataclasses import dataclass


@dataclass
class PlantsClass:
    id: int
    class_name: str
    soil_type: str
    replanting_time: str
    feed_type: str
    feed_time: str
    winter_water_regime: str
    summer_water_regime: str

    def __str__(self):
        return f"{self.class_name}"
