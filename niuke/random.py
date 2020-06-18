import sys

def is_number(indata):
    try:
        float(indata)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    while True:
        num = sys.stdin.readline()
        num_list = []
        for i in range(int(num)):
            data = sys.stdin.readline()
            num_list.append(int(data))

        num_list = list(set(num_list))
        num_list.sort()
        for item in num_list:
            print(item)