while True:
    try:
        line = input().strip().lower()
        code = input().strip()
        print(line.count(code))
    except:
        break