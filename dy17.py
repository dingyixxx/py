import  random

random_number=random.randint(1,100)
print(f"...................................................................................................................................................................................{random_number}")
while True:
    num=int(input("请输入您猜的数字："))
    print(f"num-{num}")
    if num<random_number:
        print("往大了猜")
    elif num>random_number:
        print("往小了猜")
    else:
        print("猜对了"+str(num))
        break