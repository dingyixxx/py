s="黄山落叶松叶落山黄"
s1="上海自来水来自海上"

print(s.index("黄"))
for e in range(0, len(s)):
    l=e
    r=len(s)-1-l
    if l==r:
        break
    if s[l]==s[r]:
        continue
    else:
        print("不是回文")
        break

print("回回~")