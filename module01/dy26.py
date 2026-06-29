a=1
b=22
a,b=b,a
print(a)
print(b)
#不需要临时变量


students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周铁", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "通天", 66, 59, 72)
)


# 1. 计算每个学生的总分、各科平均分，然后一并输出来。
# 2. 统计各科成绩的最低分、最高分、平均分，并输出。
# 3. 查找成绩优秀（平均分大于90）的学生，并输出。 shift+tab缩进
print(f"总分\t平均分")
for id,name,chinese,math,english in students:
    total=0
    total+=chinese+math+english
    avg=total/3
    print(f"{total}-{avg:.1f}-{avg}")
# for student in students:
#     total=0
#     total+=student[2]+student[3]+student[4]
#     avg=total/3
#     print(f"{total}-{avg:.1f}-{avg}")

chinese_scors=[student[2] for student in students]
math_scors=[student[3] for student in students]
english_scors=[student[4] for student in students]

print(f"语文最高分：{max(chinese_scors)}\t语文最低分：{min(chinese_scors)}\t语文平均分：{sum(chinese_scors)/len(chinese_scors)}")
print(f"语文最高分：{max(math_scors)}\t语文最低分：{min(math_scors)}\t语文平均分：{sum(math_scors)/len(math_scors)}")
print(f"语文最高分：{max(english_scors)}\t语文最低分：{min(english_scors)}\t语文平均分：{sum(english_scors)/len(english_scors)}")
