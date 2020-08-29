def get_jc(n):
    result = 1
    for i in range(1, n + 1, 1):
        result = result * i
    return result

def get_num(n, k, result, list):
    if n > 1:
        m = get_jc(n - 1)
        num = k // m
        if not k / m > num:
            num = num - 1
        result = result + str(list.pop(num))
        return get_num(n-1, k - m * num, result, list)
    else:
        result = result + str(list.pop(0))
        return result

while True:
    try:
        n = int(input().strip())
        k = int(input().strip())
        list = list(range(1,n+1))
        # for i in range(1, n+1, 1):
            # list.append(i)
        print(get_num(n, k, '', list))
    except:
        break


# from itertools import product
# while 1:
#     num = int(input("num >>>"))
#     choice = int(input("choice >>>"))
#     seq = [[str(i) for i in range(1, num+1)] for _ in range(num)]
#     res = []
#     for d in product(*seq):
#         if len(set(d)) == num:
#             res.append(''.join(d))
#     res.sort()
#
#     print(res[choice-1])
#     print('==='*30)


'''
第k个排列：
给定参数n，从1到n会有n个整数：1,2,3,4,...，n,这n个数字共有n!种排列。
按大小顺序升序排列出所有排列情况，并一一标记，当n=3时，所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定n和k，返回第k个排列。
'''
