# for e in range(1,21):
#     print(e)
#
#
# #列表推导式
# num=[e**2 for e in range(1, 21)]
# print(num)
from dy20 import num_list1

num_list5=[e**2  for e in num_list1 if e%2==0 ]
print(num_list5)
