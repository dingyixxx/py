


while True:
    name = input("name:")
    password = input("pass:")
    if ""==name and "" ==password:
        print("不能为空")
        continue
    if "admin"==name and "666888" ==password:
        print("成功~！")
        break
    elif "zhangsan" == name and "123456" == password:
        print("成功~！")
        break
    elif "taoge" == name and "888666" == password:
        print("成功~！")
        break
    else:
        print("fail...")


