import sys

def charprint(strs):
    for s in strs:
        if "a"<= s <= "z":
            print(s,end='')
    for s in strs:
        if "A"<= s <= "Z":
            print(s,end='')

if __name__ == '__main__':
    while True:
        line = sys.stdin.readline().strip()
        lens = len(line)
        if not line:
            break
        charprint(line)