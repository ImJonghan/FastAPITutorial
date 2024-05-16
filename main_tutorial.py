from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted"}

# @app.get("/chatgpt/{text}")
# def ai_system(text: str):
#     # openai chatgpt api 를 이용해서 동작
#     # 응답
#     return {"message": "응답"}
# @app.get("/image/")
# def ai_image(text: str):
#     # 어떤 작업
#     # 응답
#     return {"message": "응답"}
# @app.get("/robot/left/")
# def ai_ml(text: str):
#     # 어떤 작업    
#     # 응답
#     return {"message": "응답"}

class Student(BaseModel):
    student_id:int
    name:str
    email:str
# 학생 정보 조회
@app.get("/student/{student_id}")
def searchStudent(student_id:int):
    return {"student_id": student_id, "name": "김멋사", "email": "kimmutsa@example.com"}

@app.post("/item/")
def itemCreate(item:Item):
    return {"name": item.name, "description":item.description}