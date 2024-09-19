from dataclasses import dataclass


@dataclass
class DreamTeam:
    team_name: str
    C: str
    PF: str
    SF: str
    SG: str
    P: str
    id: int = None