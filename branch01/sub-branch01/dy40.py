# import random
#
# random.randint(10,100)
#
# import random as rd
# rd.randint(10,100)

# from random import randint,choice
# aaa=choice([111,222,333])
# print(aaa)
# randint(10,1000)

# from random import  randint as rint
# rint(10,1000)

# from module02 import say_hello, name

# rint(10,1000)
#
# from random import  *
# rint(10,1000)

# import module02.my_fun
# import  module02.my_var
#
# module02.my_fun.say_hello()
# print(module02.my_var.name)

# say_hello()
# print(name)







# import module02.my_var
# import  module02.my_fun
#
# print("import 包名.模块名 调用时：包名.模块名.功能名")
# module02.my_fun.say_hello()
# print(module02.my_var.name)






# from module02 import my_fun
# from module02 import my_var
#
# print("from 包名 import 模块名 调用时：模块名.功能名")
# my_fun.say_hello()
# print(my_var.name)







# from module02 import  *
#
# print("from 包名 import *，如果采用这种方法，必须在__init__.py增加导入的模块，或者__all__ 调用时：模块名.功能名")
# my_fun.say_hello()
# print(my_var.name)










from branch02.module02.my_fun import say_hello
from branch02.module02.my_var import name

print("from 包名.模块名 import 功能名 调用时：功能名")
say_hello()
print(name)







# from module02.my_fun import *
# from module02.my_var import *
#
# print("from 包名.模块名 import * 调用时：功能名")
# say_hello()
# print(name)


#选中项目，右键，new，python package
#包 比 普通文件夹 目录icon 文件夹上多一个小圆圈


