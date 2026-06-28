part1="第一部分"
part2="第二部分"

print(part1+part2)
print("111""2222")
print("111","2222")


name="涛哥"
age=18
major="软件工程"
hobbies="Python,Java"

isReal=True
print(isReal,"aaa")#不能用+加号，应该用逗号
print(str(isReal)+"aaa")

print("大家好，我是"+name+",今年",age,"岁，学习的专业是"+major+"，爱好是"+hobbies)
print("大家好，我是"+name+",今年"+str(age)+"岁，学习的专业是"+major+"，爱好是"+hobbies)
print("大家好，我是%s,今%s岁，学习的专业是%s，爱好是%s"%(name,age,major,hobbies))
print(f"大家好，我是{name},今年{age}岁，学习的专业是{major}，爱好---是{hobbies}")


s1="大卫"
s2="鲁斯"
print("tell me why %s"%s1) # %s是占位符
print("我有两部分 %s && && %s"%(s1,s2))
