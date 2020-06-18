import sys

if __name__ == '__main__':
    while True:
        try:
            hex_num = sys.stdin.readline()
            print(int(hex_num,16))
        except TypeError:
            print(1)