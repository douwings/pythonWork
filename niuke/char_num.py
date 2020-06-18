while True:
    try:
        line = input().strip()
        new_line = ''
        for item in line:
            if 0< ord(item) < 127:
                if item not in new_line:
                    new_line+= item
        print(len(new_line))
    except:
        break