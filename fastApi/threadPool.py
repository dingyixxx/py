import time
from concurrent.futures import ThreadPoolExecutor

def download(url: str) -> str:
    start = time.time()
    time.sleep(1)
    elapsed = time.time() - start
    print(f"[{time.strftime('%H:%M:%S')}] {url} 完成 (耗时 {elapsed:.2f}s)")
    return f"{url} done"

urls: list[str] = ["http://a.com", "http://b.com", "http://c.com", "http://d.com", "http://e.com", "http://f.com", "http://g.com", "http://h.com", "http://i.com", "http://j.com"]

start_all = time.time()
with ThreadPoolExecutor(max_workers=3) as pool:
    results = pool.map(download, urls)

print(f"\n总耗时: {time.time() - start_all:.4f}s")
for r in results:
    print(r)
