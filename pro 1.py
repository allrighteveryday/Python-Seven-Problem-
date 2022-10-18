# 百分制判断
while True:
    try:
        mark = int(input('请输入一个百分制成绩'))
        if 90 <= mark <= 100:
            print('A')
        elif 80 <= mark <= 89:
            print('B')
        elif 70 <= mark <= 79:
            print('C')
        elif 60 <= mark <= 69:
            print('D')
        elif 0 <= mark < 60:
            print('E')
        else:
            if mark < 0:
                print('分数不能为负数')
            if mark > 100:
                print('分数不能大于100')
            print('请重新输入')
    except ValueError:
        print('请输入正确格式')
