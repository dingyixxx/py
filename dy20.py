num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 1. 合并列表

# num_list=[*num_list1,*num_list2] #解包=合并
num_list=num_list1+num_list2 #解包=合并
print(num_list)

for num in num_list2:
    num_list1.append(num)

num_list1.sort()
print(num_list1)

res=[]
for i, e in enumerate(num_list1):
    if   i<len(num_list1)-1 and num_list1[i] != num_list1[i+1]:
        res.append(num_list1[i])
    elif i==len(num_list1)-1 and (len(res)==0 or res[-1] !=num_list1[i]):
        res.append(num_list1[i])

print(res)

res1=[]
for e in num_list1:
    if e not in res1:
        res1.append(e)
print(res1)


#解包
