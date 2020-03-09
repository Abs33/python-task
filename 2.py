
money = input("请输入您要转换的货币数加类型")
def One(money):
    if money[-1:]=="$":
        sum = eval(money[:-1])*6.78
        print("{}$为{}￥".format(eval(money[:-1]),sum))
    elif money[-1:] == "￥":
        sum = eval(money[:-1])/6.78
        print("{}￥为{}$".format(eval(money[:-1]), sum))
    else:
        print("您的输入有误2，请重新输入")
def Three(money):
    if money[-3:]=="USD":
        sum = eval(money[:-3])*6.78
        print("{}USD为{}RMB".format(eval(money[:-3]),sum))
    elif money[-3:] == "RMB":
        sum = eval(money[:-3])/6.78
        print("{}RMB为{}USD".format(eval(money[:-3]), sum))
    else:
        print("您的输入有误3，请重新输入")
if money[-1:] == "$"or money[-1:] =="￥":
    One(money)
elif money[-3:] == "RMB"or money[-3:] =="USD":
    Three(money)
else:
    print("您的输入有误1，请重新输入")


  
val=input("请输入带温度表示符号的温度值(例如：32C)：")#
if val[-1] in ['C','c']:
    f=1.8*float(val[0:-1])+32
    print("转换后的温度为：%.2fF"%f)# %f中的指的是表达式f的输出值
elif val[-1] in ['F','f']:
    c=(float(val[0:-1])-32)/1.8
    print("转换后的温度为：%.2fC"%c)
else:
    print("输入错误，请重新输入")