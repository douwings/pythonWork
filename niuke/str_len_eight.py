def fun(s):
    print(s[:8])
    s = s[8:]
    if len(s) > 8:
        fun(s)

while True:
    try:
        str1 = input().strip() + '00000000'
        str2 = input().strip() + '00000000'
        fun(str1)
        fun(str2)
    except:
        break