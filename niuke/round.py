while True:
    try:
        num = float(input().strip())
        print(int(num + 0.5))
        print(round(num))
    except:
        break