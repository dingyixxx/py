import random

names = ["王林", "李慕婉", "许立国", "韩立",
         "涛哥", "莫厉海", "十三", "虎咆",
         "红蝶", "天运子"]

remaining = names.copy()

while remaining:
    input("\n按回车键点名...")
    person = random.choice(remaining)
    remaining.remove(person)
    print(f"🎯 {person} (剩余{len(remaining)}人)")

    if not remaining:
        print("\n✅ 所有人都已点过！")
        break

    choice = input("继续吗？(y/n): ")
    if choice.lower() != 'y':
        break
