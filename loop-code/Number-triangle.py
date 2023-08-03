n=10
for i in range(1,n+1):

    for j in range(1,n-i):
        print("*",end=' ')

    for j in range(1,i):
        print(" ",end=' ')

    for j in range(1,i+1):
        print(" ",end=' ')

    for j in range(i,n):
        print("*",end=' ')

    for j in range(2):
        print("  ",end='')
    for j in range(1,n-i):
        print("*",end=' ')

    for j in range(1,i):
        print(" ",end=' ')

    for j in range(1,i+1):
        print(" ",end=' ')

    for j in range(i,n):
        print("*",end=' ')
    
    for j in range(4):
        print(" ",end='')
    
    for j in range(5):
        print("-123-",end='')
    for j in range(5):
        print( j+1,end=' ')
    for j in range(10):
        print( i+j,end='')
    print()