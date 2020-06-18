import sys

student = []

def init(initLine,socres):
    global student
    queryNum = initLine.split(' ')[1]
    student = socres.split(' ')
    return queryNum

def update(line):
    global student
    point = line.split(' ')[1]
    student[int(point) - 1] = line.split(' ')[2]


def query(line):
    global student
    start = int(line.split(' ')[1])
    limit = int(line.split(' ')[2])
    if start > limit:
        start, limit = limit, start

    start = start if int(line.split(' ')[1]) >= 1 else 1
    start = start if int(line.split(' ')[1]) < len(student) else len(student)

    limit = limit if int(line.split(' ')[1]) >= start else start
    limit = limit if int(line.split(' ')[1]) < len(student) else len(student)

    new_list = student[start-1: limit]
    return max(new_list)

if __name__ == '__main__':
    while True:
        initLine = sys.stdin.readline().strip()
        socres = sys.stdin.readline().strip()
        queryNum = init(initLine,socres)
        # print(queryNum)
        for i in range(int(queryNum)):
            line = sys.stdin.readline().strip()
            if line.startswith('U'):
                update(line)
            elif line.startswith('Q'):
                print(query(line))
        student = []