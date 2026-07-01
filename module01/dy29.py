
dict1={"姓名":"dingyi","age":35,"hobby":["游泳",(11,True)],1:True,3.14:None,(1,2):"hello"}
# TypeError: unhashable type: 'list' key需要为不可变类型的数据容器（不能为list，set或者dict）
#字典没有索引
print(dict1["hobby"])

dict1["hobby"]="我变了"
print(type(dict1))
print(dict1["hobby"])

# print(dict1["emai"])   KeyError: 'emai'
dict1["emai"]="dingyixxx@126.com"

# del  dict1 ["emai"]
# dict1.pop("emai")
# print(dict1.get("emai"))
#
# for key in dict1.keys():
#     print(key)
#
# for value in dict1.values():
#     print(value)

for k,v in dict1.items():
    print(k)
    print(v)

for (k,v) in dict1.items():
    print(k)
    print(v)

# for item in dict1.items():
#     print(type(item))
#     print(item[0])
#     print(item[1])
#     print(item)
