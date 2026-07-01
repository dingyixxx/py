with open("output.txt", "r", encoding="utf-8") as f:
    for line in f:           # 惰性读取，不会一次性加载全部
        print(line.strip())
