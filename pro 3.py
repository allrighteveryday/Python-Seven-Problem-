# 编写函数
def get_num(*n):
    # 求最大值 & 最小值
    count = 0
    max = 0
    min = 0
    for i in n:
        count += 1
    j = 0
    max = n[0]
    min = n[0]
    while j + 1 != count:
        if n[j] > max:
            max = n[j]
        if n[j] < min:
            min = n[j]
        j += 1
    # 求平均值
    sum = 0
    for x in n:
        sum = sum + x

    return (max, min, sum / count)


print(get_num(2, 2, 6, 8, 9))
