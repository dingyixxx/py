# 案例：基于match...case 实现一个简易的计算器，可以实现 + - * / 运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算。
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
oper = input("请输入运算符(+ - * /) ：")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0: # if条件成立，才匹配这个case
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持!!!")
