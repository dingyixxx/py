def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


#装饰器
@singleton
class MyService:
    pass


# myService1=MyService()
# myService2=MyService()
# print(myService2 == myService1)

from MyLove import  love

love1=love
love2=love

print(love1 == love2)