# python里面的对象，是否像springboot一样是单例的？
# 否

class MyService:
    _instance = None
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(cls.__dict__)
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

myService=MyService()
# print(myService)

# def func(a, b, c):
#     print(f"a={a}, b={b}, c={c}")
#
# # * 解包列表/元组 → 位置参数
# args = [1, 2, 3]
# func(*args)  # 等价于 func(1, 2, 3)
#
# # ** 解包字典 → 关键字参数
# kwargs = {"a": 1, "b": 2, "c": 3}
# func(**kwargs)  # 等价于 func(a=1, b=2, c=3)
