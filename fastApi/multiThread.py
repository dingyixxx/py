import threading
import time

def task(name: str, count: int):
    for i in range(count):
        print(f"{name}: {i}")
        time.sleep(0.5)

# 创建线程
t1 = threading.Thread(target=task, args=("线程A", 5))
t2 = threading.Thread(target=task, args=("线程B", 5))

t1.start()    # 启动
t2.start()

t1.join()     # 等待完成
t2.join()
print("全部完成")
