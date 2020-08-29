import math

def standings():
    while True:
        try:
            N = int(input().strip())
            num_list = []
            for i in range(1,N + 1,1):
                if N % i == 0:
                    num_list.append(i)
            print(len(num_list),' '.join(str(s) for s in num_list))
        except:
            break


def standings2():
    num = int(input())
    i = 1
    rs = []
    while i < math.sqrt(num) + 1:
        if num % i == 0:
            if str(int(i)) not in rs:
                rs.append(str(int(i)))
            i2 = num / i
            if str(int(i2)) not in rs:
                rs.append(str(int(i2)))
        i += 1
    print(len(rs), ' '.join(sorted(rs, key=lambda x: int(x))))

if __name__ == "__main__":
    standings2()
    
    
    
    
    
'''
题目描述
solo发现他参加Online Judge的比赛表现很不稳定，于是他翻开历史记录，发现他在每一轮的比赛中他的排名R都能整除参赛人数N(包括solo)，于是他每次参赛都会先预测他的排名情况，以给自己更大的自信。

解答要求
时间限制：15000ms, 内存限制：64MB
输入
输入只有一个整数N(0<N<109)，代表参赛人数。

输出
在一行输出solo参赛可能的获得的排名数S以及由小到大输出各个排名Ri (0<i ≤ S)，用空格隔开。

样例
输入样例 1 复制

10
输出样例 1

4 1 2 5 10
'''
