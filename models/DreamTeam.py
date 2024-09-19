from dataclasses import dataclass
from typing import List


@dataclass
class DreamTeam:
    team_name: str
    C: str
    PF: str
    SF: str
    SG: str
    P: str
    id: int = None