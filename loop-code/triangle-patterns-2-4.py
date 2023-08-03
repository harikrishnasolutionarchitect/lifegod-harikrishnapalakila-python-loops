n=10
for i in range(n):
    for j in range(i):
        if (i%2==0):
            print("2",end=' ')
        else:
            print("4",end=' ')
    print()
for i in range(n):
    for j in range(i,n):
        if (i%2==0):
            print("2",end=' ')
        else:
            print("4",end=' ')
    print()