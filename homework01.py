#pro1:算法1：输出1-100内所有的偶数
def pro1():
    ans_01=[i for i in range(100) if i%2==0]
    print(ans_01)

#pro2:法2：输出1-100内所有的奇数
def pro2():
    for i in range(1,100,2):
        print(i)
#pro3:算法3：计算闰年
def pro3():
    year=int(input("input:"))
    if (year%4==0 and year%100!=10) or year%400==0 :
        print('{}是闰年'.format(year))
    else:
        print('{}不是闰年'.format(year))



#pro4:算法4：判断最大值
def pro4():
    num1=int(input("input num1:"))
    num2=int(input("input num2:"))
    num3=int(input("input num3:"))
    print("max:{}".format((num1 if num1>num3 else num3) if num1>num2 else (num2 if num2>num3 else num3)))

#pro5:算法5：输出1000以内的水仙花数

def pro5():
    for i in range(100,1000):
        if(i % 10) ** 3 + (i // 10 % 10 ) ** 3 + (i // 100) ** 3 == i:
            print(i)


#pro6:算法6：互不相同且无重复数字的三位数
def pro6():
    print("result:")
    for i in range(1,5):
        for j in range(1, 5):
            for k in range(1, 5):
                print(i+j*10+k*100)


#pro7:算法7：输出9*9乘法表

def pro7():
    for i in range(1,10):
        for j in range(1,10):