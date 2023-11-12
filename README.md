
# Simple FastApi Project

Imagine you are an administrator for a university!

Task: **Explore the members of the university and make changes when needed**. Instructions given below.

Description: This application does basic CRUD operations. The application includes a FastApi server connected to a dummy database (db) of users. Initially there are two users contained in the database. Take advantage of the operations to explore and alter the database.


## Prerequisites
On your machine:
- pip install **fastapi**
- pip install **uvicorn[standard]**
## Deployment

To deploy this project, go to the project directory and run:

 On windows:

```bash
  python -m uvicorn main:app --reload
```
On mac:
```bash
  uvicorn main:app --reload
```



## API Reference

#### Root webpage

```http
  local_host/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | `GET` | Create a welcome page when the app loads up |

#### Fetch items

```http
  local_host/api/v1/users
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| - | `GET` | Fetch the list of users stored in the db initially |

#### Creates items

```http
  local_host/api/v1/users
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `-` | `POST` | Creates/registers a user to be stored in the db |

#### Deletes items

```http
  local_host/api/v1/users/{user_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_id` | `DELETE` | Deletes a user from the db |

#### Updates items

```http
  local_host/api/v1/users/{user_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_id` | `PUT` | Updates a user from the db |


