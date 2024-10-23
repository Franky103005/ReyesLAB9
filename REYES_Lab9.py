rows = int(input("Enter the number of rows: "))
i = 1

for j in range(1,rows + 1):
    for k in range(j):
        print(i,end=" ")
        i += 1
    print()