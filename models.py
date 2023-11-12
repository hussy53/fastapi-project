# Import the necessary packages
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel # Instantiates a base model, like user has a name & id. Pydantic is used for data validation

# Gender class
class Gender(str, Enum):
    male = "male"
    female = "female"

# Roles assigned to a user
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

# Creates a user class
class User(BaseModel):
    id : Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    middle_name : Optional[str]
    gender : Gender
    roles : List[Role]

# Creates a class that updates the user
class UserUpdateRequest(BaseModel):
    first_name : Optional[str]
    last_name : Optional[str]
    middle_name : Optional[str]
    gender : Optional[Gender]
    roles : Optional[List[Role]]