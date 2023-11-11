from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel # Instantiates a base model, like user has a name & id. Pydantic is used for data validation

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

# Create a user class
class User(BaseModel):
    id : Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    middle_name : Optional[str]
    gender : Gender
    roles : List[Role]

# Create a class that updates the user
class UserUpdateRequest(BaseModel):
    first_name : Optional[str]
    last_name : Optional[str]
    middle_name : Optional[str]
    gender : Optional[Gender]
    roles : Optional[List[Role]]