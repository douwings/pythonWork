while True:
    try:
        num = int(input().strip())
        list = {}
        for i in range(num):
            k, v = map(int, input().strip().split(' '))
            list[k] = list.setdefault(k, 0) + v
        for k in sorted(list.keys()):
            print(k, list[k])
    except:
        break
