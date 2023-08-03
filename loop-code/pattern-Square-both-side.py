n=20
for row in range(n):
    for col in range(n-row-1):
        print("*",end=' ')
    for col in range(row+1):
        print("1",end=' ')
    for col in range(n-1):
        print(" ",end='')
    for col in range(n-row-1):
        print("##",end=' ')
    for col in range(row+1):
        print("22",end=' ')
    for col in range(n-1):
        print(" ",end='')
    for col in range(n-row-1):
        print(" ",end='')
    for col in range(row+1):
        print("33",end=' ')
    print()