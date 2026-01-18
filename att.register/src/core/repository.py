import pandas as pd
import requests
import io
from typing import Optional, List
from src.core.models import AttendanceRecord, Student
from src import config

class SheetsRepository:
    def __init__(self, csv_url: str = config.GOOGLE_SHEET_CSV_URL):
        self.csv_url = csv_url
        self._df: Optional[pd.DataFrame] = None

    def fetch_data(self) -> None:
        """Downloads the CSV from Google Sheets and loads it into a DataFrame."""
        try:
            response = requests.get(self.csv_url)
            response.raise_for_status()
            # Read CSV from memory string
            self._df = pd.read_csv(io.StringIO(response.text))
            
            # Basic validation: Check if required columns exist
            if config.COL_STUDENT_ID not in self._df.columns:
                raise ValueError(f"Colonna '{config.COL_STUDENT_ID}' non trovata nel Foglio.")
                
        except Exception as e:
            raise ConnectionError(f"Impossibile recuperare o analizzare i dati: {e}")

    def get_student_stats(self, student_id: str) -> Optional[AttendanceRecord]:
        """Calculates stats for a specific student ID."""
        if self._df is None:
            self.fetch_data()

        # Filter by Student ID (ensure string comparison)
        student_row = self._df[self._df[config.COL_STUDENT_ID].astype(str) == str(student_id)]
        
        if student_row.empty:
            return None
        
        # Calculate stats
        # Assuming all columns AFTER 'Name' are date columns containing "P" (Present) or "A" (Absent)
        # We need to identify date columns dynamically.
        # Strategy: Exclude Metadata columns (ID, Name) and count.
        
        metadata_cols = [config.COL_STUDENT_ID, config.COL_STUDENT_NAME]
        date_cols = [c for c in self._df.columns if c not in metadata_cols]
        
        total_lectures = len(date_cols)
        present_count = 0
        
        # Iterate over date columns for this student
        for col in date_cols:
            val = str(student_row.iloc[0][col]).strip().upper()
            if val in ['P', 'PRESENT', '1', 'TRUE']:
                present_count += 1
                
        return AttendanceRecord(
            student_id=student_id,
            total_lectures=total_lectures,
            present_count=present_count
        )

    def check_connection(self) -> bool:
        """Verifies if the URL is reachable and valid."""
        try:
            self.fetch_data()
            return True
        except:
            return False
