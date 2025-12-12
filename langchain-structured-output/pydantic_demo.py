from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    cgpa: float = Field(gt=0, lt=10)

new_student = {'name': 'Satyam', 'age': 22,'cgpa': 9}

student = Student(**new_student)

print(student)