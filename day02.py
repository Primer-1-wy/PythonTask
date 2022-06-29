#5.8

#pro1:算法1：回文字符串
def pro1(str):
    if str==str[::-1]:
        print("{}是一个回文字符串".format(str))
    else:
        print("{}不是一个回文字符串".format(str))



#pro2:算法2：字符串替换
def pro2(str):
    new_str=""#创建一个空字符串
    for i in str:
        if i==' ':
            new_str+=','
        else:
            new_str+=i
    return new_str

#pro3:算法3：字符串反序
def pro3(str):
   # new_str = ""  # 创建一个空字符串
    return str[::-1]
#print(pro3("123"))

#pro4:算法4：动态构成一个完整字符串
def pro4():
    new_str = ''
    while True:
        s = input('请输入一个字符：')
        if s == 'exit':
            new_str += ''
            break
        new_str += s
    print('构造的字符串为：{}'.format(new_str))

#pro5:算法5：动态生成一个列表
def pro5():
    l = []
    while True:
        num = input('请输入一个数字：')
        l.append(num)
        if len(l) == 10:
            break
    print('添加元素之后的列表为：{}'.format(l))

#pro6:算法6：将一个列表反序
def pro6(Alist):
    return Alist[::-1]

#print(pro6([1,2,3,4,5,6]))


import random
l=[random.randint(1,50) for i in range(20)]#创建一个无序的序列

print('无序序列为：{}'.format(l))

#第六章
#pro7:算法1：二分查找法
def pro7():
    l = [random.randint(1, 50) for i in range(20)]  # 创建一个无序的序列
    l.sort()
    print('有序序列为：{}'.format(l))
    target=input("输入查询值")
    left=0
    right=len(l)
    

