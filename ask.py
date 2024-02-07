# 调用大包中的子包
import stock.food.beef
# 注意导入的是 stock.food.beef，调用的时候一定要加上所有的包路径前缀
stock.food.beef.stockleft()

# 我们也可以使用from…import… 的方式，像这样
# from stock.food.beef import stockleft
# stockleft()

# Python语言提供了功能丰富的标准库。这些标准库把开发中常用的功能都做好了。
# 这些标准库里面有一部分叫做内置类型（built-in types） 和 内置函数 （built-in functions） 。
# 内置类型和内置函数无须使用import导入，可以直接使用。
# 内置类型有：int、float、str、list、tuple等
# 还有些标准库，需要使用import导入，才能使用。
# 常见有 sys, os, time, datetime, json，random等
# 比如，我们要结束Python程序，就可以使用sys库里面的exit函数
# import sys
# sys.exit(0)

# 比如，我们要得到字符串形式的当前日期和时间，可以使用datetime库
# import datetime
# 返回这样的格式 '20160423'
# datetime.date.today().strftime("%Y%m%d")

# 返回这样的格式 '20160423 19:37:36'
# datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")

# 比如，我们要获取随机数字，可以使用random库
# from random import randint
# 在数字1到8之间(包括1和8本身)，随机取出一个数字
# num = randint(1,8)
# print(num)