while True:
    try:
        line = input().strip().split(' ')
        print(line)
        print(len(line[-1]))
    except:
        break