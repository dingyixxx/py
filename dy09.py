while True:
    day = int(input("今天星期几："))
    match day:
        case 1:
            print("星期一")
        case 2:
            print("星期二")
        case 3:
            print("星期三")
        case 4:
            print("星期四")
        case 5:
            print("星期五")
        case 6 | 7:
            print("rest...")
        case _:
            print("其他所有情况")