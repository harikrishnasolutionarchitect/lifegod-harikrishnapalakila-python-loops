n=5
for row in range(n):
    for col in range(row+1):
        print("  ", end='  ')
    for col in range(row,n):
        print("Jai-Sree-Ram",end='  ')
    for col in range(row-n-1):
        print("  ", end='  ')
    for col in range(row,n):
        print("Jai-Sree-Ram",end='  ')

    print()