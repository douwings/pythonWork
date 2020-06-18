while True:
    try:
        num = int(input().strip())
        outlist = []
        for i in range(num):
            outlist.append(input().strip())
        outlist.sort()
        for item in outlist:
            print(item)
    except:
        break
