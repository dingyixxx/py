for e in range(10):
    print(e)

print("------")

for e in range(100, 120):
    print(e)

print("------")

for e in range(200, 250, 3):
    #shift + enter 快速创建一行新行
    print(e)

print("------")

m=5
n=10

while m>0:
    content=""
    temp=n
    while temp>0:
        content+="*"
        temp-=1
    print(content)
    m-=1
print("------")

a=20
b=8

for i in range(b):
    for j in range(a):
        print("*", end=".") #end表示以xx为结尾，默认是\n换行符
    print("")
