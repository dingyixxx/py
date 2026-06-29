# 左上角 - 计算圆面积
from dy32 import return2
"""
www
"""


def circle_area(r):
    area = 3.14 * r ** 2
    return area

area = circle_area(10)
print(area)


# 左下角 - 计算成绩统计
def calc_score(score_list):
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)
    return max_s, min_s, avg_s

s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
max_score, min_score, avg_score = calc_score(s_list)


# 右侧 - 高阶函数（函数作为参数）
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calc(x, y, oper):
    return oper(x, y)

result = calc(10, 20, add)
print(result)

x=lambda x,y,z:print(f"{x}-{y}-{z}")
y=lambda x,y,z:(x,y,z)


res=y(10, 20, 30)
print(res)
print(type(res))



# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)

data_list.sort(key=lambda item: -len(item))
print(data_list)

# 代码的可读性和可维护性，比简洁，更重要

"""
www
"""