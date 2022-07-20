from datetime import date, datetime
from pydantic import BaseModel, validator


class Announcement(BaseModel):
    """Model for announcement."""
    title: str
    description: str
    date: str

    @validator('date')
    def date_format(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return v
