import time

# 题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#
# li = [1, 2, 3, 4]
# count = 0
# num_list = []
# for x in li:
#     for y in li:
#         for z in li:
#             if x == y or x == z or y == z:
#                 continue
#             else:
#                 count += 1
#                 print(x * 100 + y * 10 + z)
# print(count)


# # 题目2：输入某年某月某日，判断这一天是这一年的第几天？
# def which_day(some_day):
#     t = time.strptime(some_day, '%Y-%m-%d')
#     return t.tm_yday
#
#
# t = which_day('2012-12-12')
# print(t)


# 题目3：输入三个整数x,y,z，请把这三个数由小到大输出。
# def sor(x, y, z):
#     a = [x, y, z]
#     b = sorted(a)
#     for i in b:
#         print(i)
#
#
# sor(232, 436, 7809)

# 题目4：斐波那契数列。
# def fibonacci_sequence(n):
#     fs_list = []
#
#     def fib(s):
#         if (s == 1) or (s == 2):
#             return 1
#         return fib(s - 1) + fib(s - 2)
#
#     for i in range(1, n + 1):
#         fs_list.append(fib(i))
#     return fs_list
#
#
# print(fibonacci_sequence(10))
# 题目5：将一个列表的数据复制到另一个列表中。
# 题目6：输出 9*9 乘法口诀表。 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{i} * {j} = {i * j} ', end='')
#     print()
# 题目7：暂停一秒输出。 程序分析：使用 time 模块的 sleep() 函数。
# 题目8：暂停一秒输出，并格式化当前时间。
# for i in range(100000):
#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
#     time.sleep(1)


# 题目9：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
# def fibonacci_sequence(n):
#     if n < 3:
#         return 2
#     else:
#         t = n // 3
#         return fibonacci_sequence(t - 1) + t * 2


# 题目10：判断101-200之间有多少个素数，并输出所有素数。
# def prime_number(num1, num2):
#     num_list = []
#     for i in range(num1, num2 + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             num_list.append(i)
#     return num_list
#
#
# print(prime_number(101, 200))

# 题目11：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# num = 100
# num_list = []
# for i in range(100, 1000):
#     x = str(i)
#     if int(x[0]) ** 3 + int(x[1]) ** 3 + int(x[2]) ** 3 == i:
#         num_list.append(i)
# print(num_list)

# 题目12：学习成绩分类：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
# def level(num):
#     if num >= 90:
#         return 'A'
#     elif 60 <= num < 90:
#         return 'B'
#     else:
#         return 'C'
# 题目13：获取当前的时间并输出指定格式的日期。
# print(time.strftime('%Y-%m-%d', time.gmtime()))
# 题目14：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符输出的数并分别统计每一种类型的个数。
# 题目15：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# high = 100
# pass_long = 0
# for i in range(10):
#     high /= 2
#     pass_long += high * 2
# print(high, pass_long)
# 题目16：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 递归法
# def num_sum(a, num):
#     count = num - 1
#     s = a * (10 ** count)
#     if s / 10 < 1:
#         return s
#     return num_sum(a, count) + s
#
#
# print(num_sum(2, 1))
#
#
# def sum_(a, num):
#     sum_n = 0
#     for i in range(1, num + 1):
#         sum_n += num_sum(a, i)
#     return sum_n
#
#
# print(sum_(3, 3))
'''递进法'''


def sum_num(a, num):
    if num == 1:
        return a
    sum_single_num = 0
    single_num = a
    for i in range(1, num):
        i = 10 ** i
        single_num += i * a
        sum_single_num += single_num
    return sum_single_num + a


print(sum_num(2, 4))

# 题目17：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# 题目18：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
# 题目19，输出以下图形
# 题目20：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 题目21：求1+2!+3!+...+20!的和。
# 题目22：利用递归方法求5!。
# 题目23：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
# 题目24：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
# 题目25：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
# 题目26：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# 题目27：添加逗号分隔列表成字符串。
# 题目28：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母
# 题目29：对random模块随机生成的10个数进行降序排序，排序法则
# 题目30，两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
# 题目31：求输入数字的平方，如果平方运算后小于 50 则退出。
# ————————————————
# 版权声明：本文为CSDN博主「Ctrl精」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_43468607/article/details/103205745
