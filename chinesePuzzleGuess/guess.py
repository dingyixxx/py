from fastapi import FastAPI
import uvicorn

# 创建FastAPI实例
dyApp = FastAPI(
    title="FastAPI Demo",
    description="FastAPI学习项目",
    version="1.0.0"
)


# ==================== 路由定义 ====================

@dyApp.get("/")
def root():
    """根路径"""
    return {"message": "Hello World"}


@dyApp.get("/users")
def get_users():
    """获取用户列表"""
    return [
        {"id": 1, "name": "Alice", "age": 18},
        {"id": 2, "name": "Bob", "age": 20}
    ]


# ==================== 启动入口 ====================

if __name__ == "__main__":
    # 方式1：直接运行（推荐开发时使用）
    uvicorn.run(dyApp, host="0.0.0.0", port=8000)

    # 方式2：命令行启动
    # python -m uvicorn fastApi.fastController:dyApp --reload
