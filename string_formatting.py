n = int(input())

for i in range (1,n+1):

    decimal = i
    octal = oct(i)[2:]
    hexa = hex(i)[2:]
    binary = bin(i)[2:]

    print(f"{decimal:>5}{octal:>5} {hexa:>4} {binary:>7}")

