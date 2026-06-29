def out_line():
    print("------123------")

out_line()

def say(aa):
    if type(aa) == str:
        # print(f"str-{aa}")
        return f"str-{aa}"
    elif type(aa)==int:
        # print(f"int-{aa}")
        return  f"int-{aa}"


print(say("南瓜..."))
print(say(123))