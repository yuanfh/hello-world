# hello-world
mòór€'s first repository

while True :
    try:
        a=input('输入温度：')
        if str(type(eval(a[0:-1]))) in ["<class 'int'>","<class 'float'>"]:
            if a[-1] in ('c','C'):
                t=float(a[0:-1])*1.8+32
                print('转换结果：%.2f 华氏度' %t)
            elif a[-1] in ('f','F'):
                t=(float(a[0:-1])-32)/1.8
                print('转换结果：%.2f 摄氏度' %t)
            else:
                print('温度单位错误！')
    except:
        print('温度数值错误！！')
    print('\n\n请继续',end='')
