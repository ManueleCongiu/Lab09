from dataclasses import dataclass
from model.airports import Airport


@dataclass
class Connessione:
    v1: Airport
    v2: Airport
    peso: int

    def __str__(self):
        return f"Arco: {self.v1.ID} - {self.v2.ID} - peso: {self.peso}"
