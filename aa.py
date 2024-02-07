# 导入 save 模块
# 导入后 save 就成为模块aa中的一个变量，对应一个模块对象
# 第二种方法是通过 from import 关键字导入其它模块里面的标识符（包括变量名和函数名等）
# 比如说from save import savetofile
# 导入后 savetofile 就成为模块aa中的一个变量，对应一个函数对象
# 然后save.savetofile(memberlist, avgfee)就变成了savetofile(memberlist, avgfee)
# 如果在一个模块文件中需要导多个其它模块，可以分开写导入语句，像这样
# import aa
# import bb
# import cc      也可以一起导入，模块之间用逗号隔开，像这样import aa, bb, cc
# 如果我们要从1个模块里导入多个标识符，可以这样from aa import func1,var1,func2,var2
# 如果我们要导入1个模块里面的很多个标识符，可以使用*代表所有可导入的标识符（包括变量名，函数名等）from aa import *
# 如果我们需要从两个模块导入函数，恰好这两个函数是同名的，这是我们可以给其中一个起个别名，避免冲突，比如
# from save import savetofile
# from save2 import savetofile as savetofile2
import save
fee = input('请输入午餐费用：')
members = input('请输入聚餐人姓名，以英文逗号,分隔：')

# 将人员放入一个列表
memberlist = members.split(',')
# 得到人数
headcount = len(memberlist)

# 计算人均费用
avgfee = int(fee) / headcount
print(avgfee)

# 使用 模块save里面的 savetofile 函数
save.savetofile(memberlist, avgfee)