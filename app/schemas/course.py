from pydantic import BaseModel, Field
from typing import Optional

class CourseBase(BaseModel):
    name: str = Field(..., description="The name of the course.")
    price: float = Field(..., description="The price of the course.")
    is_early_bird: Optional[bool] = Field(default=None, description="Whether the course has an early bird discount.")

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True