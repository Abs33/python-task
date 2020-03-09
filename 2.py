TempStr = input()
if TempStr[0:3] in ['RMB']:
    C = eval(TempStr[3:])/6.78
    print("USD{:.2f}".format(C))
elif TempStr[0:3] in['USD']:
    F = 6.78*eval(TempStr[3:])
    print("RMB{:.2f}".format(F))

    #TempConvert.py
val=input("请输入带温度表示符号的温度值(例如：32C)：")#
if val[-1] in ['C','c']:
    f=1.8*float(val[0:-1])+32
    print("转换后的温度为：%.2fF"%f)# %f中的指的是表达式f的输出值
elif val[-1] in ['F','f']:
    c=(float(val[0:-1])-32)/1.8
    print("转换后的温度为：%.2fC"%c)
else:
    print("输入错误，请重新输入")