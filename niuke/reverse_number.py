while True:
    try:
        num = input().strip()[::-1]
        outline = ''
        for item in num:
            if item not in outline:
                outline += item
        print(outline)
    except:
        break
