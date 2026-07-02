from fastapi import FastAPI
# pip install fastapi uvicorn
# python -c "import fastapi; print(fastapi.__version__)"
# python -m uvicorn fastController:app --reload

# 创建FastAPI实例
dyApp = FastAPI()

# 定义功能接口
@dyApp.get("/")
def root():
    return {"message": "Hello World"}

# 定义功能接口
@dyApp.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Alice", "age": 18},
        {"id": 2, "name": "Bob", "age": 20}
    ]
# fastapi dev fastController.py
# uvicorn fastApi.fastController:app --reload 包名.模块名：实例

from pydantic import BaseModel, Field
from typing import Optional

class CreateUserRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)  # ... 表示必填
    age: int = Field(ge=0, le=150, default=0)           # ge=大于等于, le=小于等于
    email: Optional[str] = Field(None, pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')

# FastAPI 会自动验证请求参数
@dyApp.post("/users")
def create_user(user: CreateUserRequest):
    return user



if __name__ == "__main__":
    user = CreateUserRequest(name="John", age=30, email="john--example.com")
    print(user)
    # import uvicorn
    # uvicorn.run(dyApp, host="0.0.0.0", port=8000)
