def gcd(n1,n2):
    return gcd(n2, n1 % n2) if n2 > 0 else n1
def lcm(n1,n2):
    return n1 * n2 // gcd(n1, n2)

if __name__ == '__main__':
    while True:
        try:
            nums = input().strip().split(' ')
            print(lcm(int(nums[0]),int(nums[1])))
        except:
            break