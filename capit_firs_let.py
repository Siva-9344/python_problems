s = input().split()

for i in s:
    capita_fir_let = i[0].upper()+i[1:]
    join = "".join(capita_fir_let)
    print(join, end = ' ')

# input: siva raman
#output: Siva Raman 
