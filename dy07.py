while True:
    name = input("请输入您的账号：")
    print(f"您输入的账号是{name}")
    password = input("请输入您的密码：")
    print(f"您输入的密码是{password}")

    # if(name=="18888888888" and password=="666888"):
    #     print("登陆成功")
    # else:
    #     print("登录失败")


    if((name !="18888888888") or (password !="666888")):
        print("失败...")
    else:
        print("登陆成功~~~~~")

