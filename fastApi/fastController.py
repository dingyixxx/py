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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(dyApp, host="0.0.0.0", port=8000)
