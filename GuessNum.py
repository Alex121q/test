"""
猜数字
"""
# 用户输入一个数字  电脑随机生成一个数字
# 判断用户输入的数字和电脑随机生成的数字是否相同
# 如果相同 提示猜对了
# 猜大了猜小了  提示大了小了

# 随机模块
import random

# 产生一个随机数
num = int(random.randint(1, 100))
print(num)
guess_num = None
count = 1
while count < 4:
    guess_num = int(input('请输入一个数字(1~100):'))
    if guess_num < num:
        print('小了小了')
    elif guess_num > num:
        print('大了大了')
    else:
        print('恭喜大傻逼猜对了^_^,猜了', count, '次')
        print('''
    ****************
    *Congratulation*
    ****************
         ''')
        break
    count += 1
else :
    print('你输了，大笨蛋，正确答案是:', num)
