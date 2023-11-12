# Import the necessary packages
from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User, UserUpdateRequest

# Create a fastapi instance
app = FastAPI()

# DATABASE(db) : Create a database with a list of users
db : List[User] = [
    User (
        id = UUID("b61c6edc-6a81-43f4-9e7b-3077884c392d"),
        first_name = "Lisa",
        last_name = "Tyfold",
        middle_name = " ",
        gender = Gender.female,
        roles = [Role.student]
    ),
    User (
        id = UUID("339e308c-6559-45bf-967a-11745ae82af2"),
        first_name = "Alex",
        last_name = "Jones",
        middle_name = " ",
        gender = Gender.male,
        roles = [Role.admin, Role.user]
    )
]

# Create a root when the app loads up
@app.get("/")
async def root():
    return {"Welcome to a basic fastapi application. This is app creates, reads, updates and deletes users from a database. Give it a shot!"}

# Fetch the list of users stored in the db initially
@app.get("/api/v1/users")
async def fetch_users():
    return db

# Create/register a user
# Returns the user id to the client
@app.post("/api/v1/users")
async def register_user(user : User):
    db.append(user)
    return {"id" : user.id}

# Deletes a user
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id : UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

    raise HTTPException (
        status_code = 404,
        detail = f"user with user id: {user_id} does not exist"
    )    

# Updates a user
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update : UserUpdateRequest, user_id : UUID):
    for user in db:
        if user.id == user_id:
            # Update their credentials
            if user_update.first_name is not None:
                user.first_name = user_update.first_name

            if user_update.last_name is not None:
                user.last_name = user_update.last_name

            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name

            if user_update.gender is not None:
                user.gender = user_update.gender

            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code = 404,
        detail = f"user with user id: {user_id} does not exist"
    )