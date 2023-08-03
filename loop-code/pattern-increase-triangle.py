n=20
for row in range(n):
    for col in range(row+1):
        print("1",end='')
    for col in range(row+1):
        print("*",end='')
    print()