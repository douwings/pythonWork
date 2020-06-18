# def yue (n,m):
#     print((yue(n-1,m)+m-1)%n)
#     return n if n == 1 else (yue(n-1,m)+m-1)%n

# if __name__ == "__main__":
#     n = input('N:')
#     m = input('M:')
#     print(yue(int(n),int(m)))


def yue(n,m):
    #参数定义：
    peoples = []
    for _ in range(n):
        peoples.append(True)
 
    result = []
    num =1
    #主逻辑
    while(any(peoples)):
        for index,people in enumerate(peoples):
            if people:
                if num == m:
                    peoples[index] = False
                    result.append(index+1)
                    print('本轮出局者',index+1)#每轮的出局者                
                    print('队伍状态', peoples)#每次的队列状态
                    num = 1               
                else:
                    num += 1
    print('-'* 25)
    print('\n总数为%d,报数为%d' % (n,m))        
    print('约瑟夫序列为：\n%s\n' % result)      
    print('-'* 25)

if __name__ == "__main__":
    n = input('N:')
    m = input('M:')
    yue(int(n),int(m))
    # print(yue(int(n),int(m)))