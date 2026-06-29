num=9

for i in range(1, 1 + num):
    #1-9
    for j in range(1, 1 + i):
        print(f"{j}*{i}={i*j}",end="    ")
    print()