from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Student:
    id: str
    name: str

@dataclass
class AttendanceRecord:
    student_id: str
    total_lectures: int
    present_count: int
    
    @property
    def absence_count(self) -> int:
        return self.total_lectures - self.present_count

    @property
    def attendance_percentage(self) -> float:
        if self.total_lectures == 0:
            return 0.0
        return (self.present_count / self.total_lectures) * 100.0
