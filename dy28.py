# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "通天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# {'乌丑', '厉飞雨', '王蝉', '曾牛', '墨居仁', '姜老道', '张铁', '韩立', '通天', '云露', '徐立国', '王林', '李化元', '天运子', '紫灵'}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"通天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1. 找出同时选修了 法语 和 艺术 的学生  french_set  art_set
fa_set=french_set & art_set
print(fa_set)

# 2. 找出同时选修了所有四门课程的学生
four_set=fa_set & basketball_set &football_set
print(four_set)

# 3. 找出选修了足球，但是没有选修篮球的学生
foot_over_basketball_set=football_set - basketball_set # &交集 |并集 -差集
print(foot_over_basketball_set)

print({e for e in football_set if e not in basketball_set})



# 4. 统计每一个学生选修的课程数量

print("通天" in art_set)

all_list=[*football_set,*basketball_set,*french_set,*art_set]
all_set=football_set|basketball_set|french_set|art_set
for e in all_set:
    print(f"{e}-{all_list.count(e)}")