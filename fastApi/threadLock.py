
import threading
import time

counter: int = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(10000):
        with lock:
            x = counter
            time.sleep(0)
            counter = x + 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"counter = {counter}")
