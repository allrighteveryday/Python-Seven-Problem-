# 赶鸭子
# def fun(times, num):
#     if times-1:
#         fun(times-1, 2*(num+1))
#
#
#
#
#
# print(fun(7, 2))
# 失败！
# def fun(times, num):
#     if times:
#         fun(times - 1, 2 * (num + 1))
#     if times == 0:
#         print(num)
#
# fun(7, 2)
# # 及时地把最后一个值输出

def fun(n, times, num):
    if n == times:
        return num # 出口
    else:
        return (2 * ((fun(n + 1, times, num))+1))

# 验算
print(fun(0, 7, 2))

num = fun(0, 7, 2)
for i in range(7):
    num = (num / 2) - 1
print(num)

# 总结：递归函数
# 1.函数自己调用自己
# 2.函数调用自己的限制条件
# 3.思路得清晰
# 4.函数返回值得找到一个出口（如上述递归）

