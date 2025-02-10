# This is FASTAPIs with Hardcoded Data in a Single File, its goot to start, for proper approaches the below is actual FAST API Codebase with proper stucture



# from fastapi import FastAPI
# from pydantic import BaseModel,Field
# from typing import Optional

# app = FastAPI(
#     title="Course Management API",
#     description="An API to manage courses, including adding, retrieving, and deleting courses.",
#     version="1.0.0")

# fake_db=[]

# class Course(BaseModel):
#     id: int = Field(description="The unique identifier for the course.")
#     name :str
#     price: float
#     is_early_bird: Optional[bool] = None


# @app.get("/", tags=["General"])
# def read_root():
#     return {"text": "Hellow World"}

# @app.get("/courses", tags=["Courses"])
# def get_courses():
#     """
#     Retrieve all courses from the database.
#     - **Returns**: A list of all courses.
#     """
#     return fake_db



# @app.get("/courses/{course_id}", tags=["Courses"],description="Get a course by ID")
# def get_course(course_id: int):
#     return fake_db[course_id-1]



# @app.post("/courses", tags=["Courses"])
# def add_course(course: Course):
#     fake_db.append(course.dict())
#     return fake_db[-1]

# @app.delete("/courses/{course_id}", tags=["Courses"])
# def delete_course(course_id: int):
#     fake_db.pop(course_id-1)
#     return {"deleted": course_id}




from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.course import create_course, get_course, delete_course, get_courses
from app.schemas.course import Course,CourseCreate
from app.dependencies.deps import get_db
from app.database.database import Base,engine


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

@app.post("/courses/", response_model=Course)
def generate_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)

@app.get("/courses/", response_model=list[Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = get_courses(db, skip=skip, limit=limit)
    return courses

@app.get("/courses/{course_id}", response_model=Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.delete("/courses/{course_id}", response_model=Course)
def delete_course_by_id(course_id: int, db: Session = Depends(get_db)):
    db_course = delete_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course
