while True:
    try:
        print(str(bin(int(input().strip()))).count('1'))
    except:
        break
