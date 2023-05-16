def multiplication_table(n):
    for m in range(1,11):
        for a in range(1, n+1):
            print(m*a, end='\t')
        print()
ma = int(input("Enter the number you want the table for : "))
print(multiplication_table(ma))
