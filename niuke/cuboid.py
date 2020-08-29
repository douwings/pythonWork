def cuboid():
    while True:
        try:
            Length = int(input().strip())/4
            print(int(Length/3)*int(Length/3+0.5)*int(Length-int(Length/3)-int(Length/3+0.5)))
        except:
            break
        
if __name__ == "__main__":
    cuboid()
