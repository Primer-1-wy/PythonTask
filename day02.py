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


#第六章
#pro7:算法1：二分查找法 binery serch
def pro7():
    l = [random.randint(1, 50) for i in range(20)]  # 创建一个无序的序列
    print('无序序列为：{}'.format(l))
    l.sort()
    print('有序序列为：{}'.format(l))
    target=int(input("输入查询值"))
    left=0
    right=len(l)
    while left<=right:
        mid=(left+right)//2
        if(l[mid]>target):
            right=mid-1
        elif(l[mid]<target):
            left=mid+1
        else:#l[mid]==target
            print("{}是寻找值".format(l[mid]))
            break

'''

'''
#pro8:算法2：二维矩阵的元素查找
def pro8():
    l_2d = [
        [x for x in range(1, 6)],
        [y for y in range(2, 7)],
        [z for z in range(3, 8)],
        [m for m in range(4, 9)]
    ]
    target = int(input('请输入您要查找的数字>>>：'))
    # 是否找到的结果集
    is_in = False
    # 行方向起始检索位置：0，即第一行，从上往下
    row = 0
    # 最大行数
    maxrow = len(l) - 1
    # 列方向起始检索位置：len(l_2d[0]) - 1,即最后一列，从右向左
    col = len(l_2d[0]) - 1
    try:
        # 当列数不断减小且行数不断增大，即从右上 - 左下查找，没有到达左下角顶点时，循环一直执行
        while col >= 0 and row <= maxrow:
      # 如果目标值大于当前值，说明在行方向上，目标值在当前值的下面行，则行数+1
            if target > l_2d[row][col]:
                row += 1
    # 如果目标值小于当前值，说明在列方向上，目标值在当前值的左边，则列数-1
            elif target < l_2d[row][col]:
                col -= 1
            else:
                is_in = True
                break
    except Exception as e:
        pass
    if is_in:
        print('找到了！{}在当前序列！'.format(target))
    else:
        print('没找到！抱歉了！')


#pro9:算法3：有序序列插入
def pro9():
    l = [random.randint(1, 50) for i in range(20)]  # 创建一个无序的序列
    print('无序序列为：{}'.format(l))
    l.sort()
    print('有序序列为：{}'.format(l))
    target = int(input('请输入你要插入的数字>>>:'))

    for i in range(len(l)):
        if(target<l[0]):
            index=0
        elif(target>l[-1]):
            index=len(l)
        elif(target<l[i]):
            index=i
    l.insert(index,target)
    print('插入新值后的新的升序序列为：{}'.format(l))


#pro10:算法4：统计出现次数最多的元素
def pro10():
    l = [random.randint(1, 50) for i in range(20)]  # 创建一个无序的序列
    print('无序序列为：{}'.format(l))
    l.sort()
    print('有序序列为：{}'.format(l))
    dicts = {}
    for i in l:
        if i not in dicts:
            dicts[i] = 1
    else:
        dicts[i] += 1
    print('各元素的出现次数：{}'.format(dicts))
    # 存放次数最大的键值
    iIndex = ''
    # 存放其对应的键名，键名即列表中出现过的元素
    iMax = 0
    # bug版找最大值：当最大次数存在多个元素时只能找到一个
    for key in dicts:
        if dicts[key] > iMax:
            iIndex = key
    iMax = dicts[key]
    print("最大元素:{},出现次数{}".format(iIndex,iMax))
#第七章


#pro11:
def pro11():
    def fib(n):

        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)


#pro12:
def pro12(month):

    if month == 1:
        return 1
    elif month == 2:
        return 1
    else:
        return pro12(month - 1) + pro12(month - 2)

