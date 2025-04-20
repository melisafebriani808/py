# rows = 5
# for j in range(1, rows+1):
#     print(" * " * j)

# rows = 7  # Jumlah baris pola
# b = 0

# for i in range(rows, 0, -1):
#     b += 1
#     for j in range('*', i + 1):
#         print(b, end=' ')
#     print('\r')

rows = 5 
i = 1

while i <= rows:
    j = 1
    while j <= (rows - i + 1):
        print("*", end=" ")
        j += 1
    print() 
    i += 1

