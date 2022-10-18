# 篮球比赛案例
adv, time = int(input('请输入领先的分数')), int(input('请输入剩余时间（单位：秒）'))
while True:
    ctrl = input('是否为控球方（请输入‘是’或‘否’）')
    if ctrl == '是' or ctrl == '否':
        if ctrl == '是':
            adv += 0.5
        elif ctrl == '否':
            adv -= 0.5
        break
    else:
        print('输入错误，请重新输入')
adv = adv ** 2
if adv > time:
    print('安全领先')
else:
    print('非安全领先')

