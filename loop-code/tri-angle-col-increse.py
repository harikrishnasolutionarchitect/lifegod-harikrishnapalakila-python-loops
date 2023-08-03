num=int(input("Enter any Number: "))
for row in range(num):
    val = row+1
    dec = num-1
    for col in range(num):
        print(val,end=' ')
        val = val+dec
        dec = dec-1
    print()