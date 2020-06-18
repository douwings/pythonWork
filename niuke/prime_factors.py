while True:
    try:
        num = int(input().strip())
        i = 2
        while num != 1:
            if num%i ==0:
                print(i,end=' ')
                num = num/i
            else:
                i+= 1
    except:
        break