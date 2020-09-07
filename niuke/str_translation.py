import numpy as np

def str_translation():
    num = int(input().strip())
    for n in range(num):
        str1 = input().strip()
        str2 = input().strip()
        lenstr1 = len(str1)
        lenstr2 = len(str2)
        dp = np.zeros((lenstr1+1,lenstr2+1), dtype=int)                 # 上一步无操作
        dpAdd = np.zeros((lenstr1+1,lenstr2+1), dtype=int)              # 上一步追加操作
        dpDel = np.zeros((lenstr1+1,lenstr2+1), dtype=int)              # 上一步删除操作
        
        for i in range(lenstr1 + 1):
            dpAdd[i][0] = dp[i][0] = 3000                               # 非空字符串转换为空字符串，追加操作和无操作都做不到
            dpDel[i][0] = 2                                             # 非空字符串转换为空字符串，只需要一步删除操作

        for i in range(lenstr2 + 1):
            dpDel[0][i] = dp[0][i] = 3000                               # 空字符串转换为非空字符串，删除操作和无操作都做不到
            dpAdd[0][i] = i + 2                                         # 空字符串转换为非空字符串，需要追加i个字符

        dp[0][0] = dpAdd[0][0] = dpDel[0][0] = 0                        # 空字符串相互转换均无开销
        
        for i in range(1,lenstr1+1):
            for j in range(1,lenstr2+1):
                # 无操作，若最后一个字符相同，三种方式取最小值，否则做不到
                dp[i][j] = min(dp[i - 1][j - 1], dpAdd[i - 1][j - 1], dpDel[i - 1][j - 1]) if str1[i - 1] == str2[j - 1] else 3000
                # 追加操作，还差最后一个字符: str2的第j个字符
                # 如果之前也是追加操作，那么开销仅+1，其他操作开销+3，三者取最小值
                dpAdd[i][j] = min(dpAdd[i][j - 1] + 1, dp[i][j - 1] + 3, dpDel[i][j - 1] + 3)
                # 删除操作，多了最后一个字符：a的第i个字符
                # 如果之前也是删除操作，那么开销不变，其他操作开销+2，三者取最小值
                dpDel[i][j] = min(dpDel[i - 1][j], dp[i - 1][j] + 2, dpAdd[i - 1][j] + 2) 
        
        print(min(dp[lenstr1][lenstr2],dpAdd[lenstr1][lenstr2],dpDel[lenstr1][lenstr2]))
    
if __name__ == "__main__":
    str_translation()
    
    
    
    
    
    
    
    
'''
解题思路：python跑的时间会超出限制 但逻辑应该是正确的  需要注意的是这里的数组生成 使用dp = [[0]*m]*n这种生成的字符串是浅拷贝，赋值过程会有变化。
'''    
    
    
'''
题目描述
给出两个字串A，B。将A字串转化为B字串，转化一共有两种方式:删除连续的n个字符，一次操作费用为2。增加连续的n个字符(增加的字符是什么由你决定)，一次操作费用为n+2。求把A变为B最小费用。

解答要求
时间限制：1000ms, 内存限制：64MB
输入
第一行输入一个正整数T(1 <= T <= 10)，表示有T组测试数据。
对于每组测试数据：
两行字符串A, B（字符串长度不超过2000，字符仅包含小写字母）

输出
对于每组测试数据，输出一行一个整数，表示最小费用。

样例
输入样例 1 复制

2
dsafsadfadf
fdfd
aaaaaaaa
bbbbbbbb
输出样例 1

7
12
'''
