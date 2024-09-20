from dataclasses import dataclass


@dataclass
class DreamTeam:
    team_name: str
    c: str
    pf: str
    sf: str
    sg: str
    pg: str
    id: int = None


print(type(int(list({4})[0])))