from dataclasses import dataclass

from dataclasses import dataclass

@dataclass
class Player:
   player_name: str  # שם השחקן
   position: str  # עמדה שבה השחקן משחק (כגון שחקן קדמי, שחקן אחורי)
   games: int  # מספר המשחקים שהשחקן השתתף בהם בעונה
   three_percent: float  # אחוזי הקליעה משלוש נקודות
   two_percent: float  # אחוזי הקליעה משתי נקודות
   effective_fg_percent: float  # אחוזי קליעה אפקטיביים (משקלל את הקליעות משלוש נקודות)
   atr: float
   ppg: float
   points: int  # מספר הנקודות שהשחקן קלע
   team: str  # שם הקבוצה שבה השחקן משחק
   season: int  # העונה שבה נרשמו הסטטיסטיקות
   player_id: str  # מזהה ייחודי של השחקן (יכול להיות שונה מהמזהה הראשון)