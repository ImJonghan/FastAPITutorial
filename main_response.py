from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/user/{user_id}", response_model=User)
def get_user(user_id: int):
    # 실제 구현에서는 데이터베이스에서 사용자 정보를 조회하겠지만, 여기서는 예시 데이터를 사용합니다.
    # return User(name="Alice", age=30)
    return {"name":"Alice", "age":30, "more":"good"}
