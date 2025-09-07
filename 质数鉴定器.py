while True:
    # 质数鉴定器
    print("请输入任意整数:",end='')
    a = int(input())
    b = 2
    count = 0
    判断 = True
    lst = []
    dic = {}
    if a == 1:
        print("1既不是质数也不是合数")
        判断 = False
    #专门存储合数的两个因数
    while True:
        c = a/b
        if c == 1:
            break
        elif c-int(c) == 0:
            dic[b] = c
            lst.append(b)
        b+=1
    #重置b为2
    b = 2
    while 判断:
        c = a/b
        if c-int(c) != 0:
            b+= 1
            count+= 1
        elif c-int(c) == 0:
            if c==1&count!=0:
                print("这是一个质数")
                break
            else:
                print("这是一个合数")
                print('这个数可以由以下因数得来：')
                if len(lst)/2==int(len(lst)/2):
                    for n in range(int(len(lst)/2)):
                        print(f'{lst[n]} × {dic[lst[n]]}')
                elif len(lst)/2 != int(len(lst)/2):
                    for n in range(int((len(lst)+1)/2)):
                        print(f'{lst[n]} × {dic[lst[n]]}')
                break

