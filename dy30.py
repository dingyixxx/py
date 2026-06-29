str="1234567890"
for i, e in enumerate(str):
    str[i]="h" #TypeError: 'str' object does not support item assignment

print(str)

# sum() len() max() min()