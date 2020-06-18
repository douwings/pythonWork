import sys

soda_list = []

def drink(soda_num,drink_num):
    if soda_num < 2:
        return soda_num,drink_num
    if soda_num == 2:
        return 0, drink_num + 1
    drink_num = drink_num + soda_num // 3
    soda_num = soda_num % 3 + soda_num // 3
    return drink(soda_num,drink_num)

def drink2(soda_num):
    drink_num = soda_num/2
    if '.' in str(drink_num):
        drink_num = (soda_num - 1) / 2
    return int(drink_num)



if __name__ == '__main__':
    while True:
        indata = sys.stdin.readline().strip()
        # if not indata.isdigit():
        #     indata = 1
        if int(indata) == 0:
            break
        soda_list.append(int(indata))

    for item in soda_list:
        # soda_num1, drink_num1 = drink(item, 0)
        drink_num2 = drink2(item)
        # print(drink_num1)
        print(drink_num2)