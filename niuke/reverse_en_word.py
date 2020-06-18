while True:
    try:
        num = input().strip().split(' ')
        for i in range(len(num)-1, -1, -1):
            print(num[i], end=' ')
        print('')
    except:
        break