#pro1:算法1：输出1-100内所有的偶数
import math


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
        for j in range(1,i+1):
            print("{}*{}={}".format(i,j,i*j),end=" ")
        print("")
#pro8:算法8：计算一个数的阶乘

def pro8(num):
    sum=1
    while(num!=0):
        sum*=num;
        num-=1
    return sum

#pro9:算法9：输出100以内的所有质数
def pro9():
    for i in range(2,100):
        flag = False
        for j in range(1,int(i/2)):
            if(j==i or j==1):
                continue
            if(i%j==0):
                flag=True
                break
        if(flag==False):
            print(i)

#pro10:算法10：分解质因数

def pro10():
    l=[]#创建一个空链表
    n=num=int(input("input:"))
    for i in range(n//2+1):
        for j in range(2,n):#整除判断
            if(n%j==0):
                l.append(j)
                n=n//j
                break

    if len(l)==0:
        print("无")
    else:
        l.append(n)#将最后一个质因数加入
        print("{}={}".format(num,l[0]),end="")
        for x in range(1,len(l)):
            print("*{}".format(l[x]),end="")


#pro11:算法11：斐波那契数列
def pro11(num):
    if num==1:
        return 1
    if num==0:
        return 0
    return pro11(num-2)+pro11(num-1)

def pro11_list():
    n=int(input("input:"))
    a=0
    b=1
    l=[0,1]
    for i in range(2,n+1):
        l.append(l[i-1]+l[i-2])
    print(l[n])


#pro12:算法12：经典算法：“不死兔子”
def pro12(num):
    while(num%3!=0):
        num-=1
    if num==3:
        return 1
    if num==0:
        return 1
    return pro12(num-3)+pro12(num-6)
#4=3+2    3=2+1  2=1+0 2=1+0        32   2110  10110->




#pro13:算法13：经典算法：“变态青蛙跳”
def pro13(num):
    a=1#第一层
    b=2#第二层
    c=0;
    if(num==0):
        return 0
    if(num==1):
        return a
    if(num==2):
        return b
    for i in range(2,num):
        c=a+b
        a=b
        b=c
    return c

#pro15:算法15：经典算法：“猴子吃桃”

def pro15(num):
    ans=1
    for i in range(num):
        ans+=1
        ans*=2
    print("{}天前还有{}个桃子".format(num, ans))
    return ans

