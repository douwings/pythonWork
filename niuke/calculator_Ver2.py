# def calculator_Ver2():
#     n = input().strip()
#     # 前后括号不一定对应的上 可判断是否数量一样
#     print('YES' if len(n.split(')')) == len(n.split('(')) else 'NO')


# def calculator_Ver2():
#     n = input().strip()
#     num = 0
#     for i in range(len(n)):
#         if n[i] == '(':
#             num += 1
#         elif n[i] == ')':
#             num -= 1
#         if num < 0:
#             break
#     print('YES' if num == 0 else 'NO')


def calculator_Ver2():
    n = input().strip()
    stack = []
    for i in n:
        if i ==')':
            if not stack:
                print('NO')
                return
            else:
                stack.pop()
        if i =='(':
            stack.append(i)
    print("YES") if not stack else print("NO")
    
if __name__ == "__main__":
    calculator_Ver2()
    
    
    
    
    
    
    
'''
解题思路：
最开始想着是否是数量对应 后来发现不只数量对应 还要位置对应，所以有了第二种方法。但感觉此题应该考察单调栈相关内容 又写了解法3。
也想过直接用eval()方法 但考虑到测试到(1/0)这种无法通过所以抛弃了
'''
    
    
    
    
'''
题目描述
Solo小学二年级了，可是问题又来了，他经常把算术表达式中的括号搞混乱，让老师很是头大，于是老师决定再次雇用你编写一个程序来检验Solo的答案的括号是否完全匹配。
注意：(1+2)(23)是括号完全匹配的，((1+2)(23)和((1+2)23则没有完全匹配。

解答要求
时间限制：1000ms, 内存限制：64MB
输入
输入只有一行，即一个长度不超过100的字符串S，表示Solo的算术表达式，（你只需考虑相互之间的括号是否完全匹配，不需考虑表达式的其他合法问题）。
注意：S中不一定包含括号。

输出
若表达式的括号完全匹配了则输出“YES”，否则输出“NO”。

样例
输入样例 1 复制

5.6*(-2*(1+(-3)))
输出样例 1

YES

输入样例 2 复制

-2
输出样例 2

YES

输入样例 3 复制

1+2)
输出样例 3

NO

输入样例 4 复制

(1+2))(
输出样例 4

NO

'''
