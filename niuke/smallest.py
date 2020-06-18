while True:
    try:
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        arr1.pop(0)
        arr2.pop(0)
        arr1.append(0)
        arr2.append(0)
        num = int(input().strip())
        result = [0] * num
        index = 0
        while index < num:
            for i in range(len(arr1) - 1):
                for j in range(len(arr2) - 1):
                    if arr1[i] + arr2[j] > arr1[i] + arr2[j + 1]:
                        break
                    else:
                        result[index] += arr1[i] + arr2[j]
                        index += 1
        print(result)
        smallest = 0
        for index in range(num):
            smallest += result[index]
        print(smallest)
    except:
        break

