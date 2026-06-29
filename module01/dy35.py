# 不定长参数
def calc_data(*args,name):
    print(args)
    print(type(args))
    print(min(args))
#
#
# print(calc_data(10,20, 30, name="lili"))
# print(calc_data(10, 20, 30,40,60, name="lili"))
#

def calc_data1(*args,**kwargs):
    print(args)
    print(type(args))
    print(min(args))
    print(kwargs)
    print(type(kwargs))


# print(calc_data1(10,20, 30,age=18, name="lili"))

# 先写不定长位置参数，再写不定长关键字参数
