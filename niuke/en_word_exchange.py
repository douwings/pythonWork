while True:
    try:
        list = input().strip().split(' ')
        site_one = int(input().strip())
        site_two = int(input().strip())
        list[site_one], list[site_two] = list[site_two], list[site_one]
        for item in list:
            print(item, end=' ')
        print('')
    except:
        break
