# # 写文件
# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write("Hello\n")
#     f.write("World\n")

# 读文件
with open("output.txt", "r", encoding="utf-8") as f:
    # content = f.read()        # 读全部
    # lines = f.readlines()   # 读所有行到 list
    line = f.readline()     # 读一行
    print("+"*60)
    # print(line)
