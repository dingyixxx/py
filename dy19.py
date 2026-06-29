nums=[]
sum=0
for e in range(10):
    num=int(input("请输入数字："))#如果不转成数字，
    nums.append(num)
    sum+=num

nums.sort()
print(sum/len(nums))

# num=10/float(2)
# print(num)