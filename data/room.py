from dataclasses import dataclass


@dataclass
class Room:
    id: int
    places_count: int
    room_type: str

    def __str__(self) -> str:
        return self.room_type
