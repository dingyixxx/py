# name=input("please enter your name:")
# print(f"欢迎您，亲爱的{name}")
#
#
# age=input("请输入您的年龄：")
# print(f"您的年龄是{age},类型是{type(age)}")

password=input("请输入您的银行卡密码：")
print(f"你输入了正确的密码~{password}")
amount=input("请输入您取款的金额：")
balance=10000-int(amount)
print(f"余额是：{balance}")

print("------")

num1=input("请输入第一个数字：")
print(f"您输入的数字是：{num1}")
num2=input("请输入第二个数字：")
print(f"您输入的数字是：{num2}")
print(int(num1)+int(num2))
exit(9)