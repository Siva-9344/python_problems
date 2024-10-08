# mutations

s = input()

j = input().split()
i_0 = int(j[0])
i_1 = j[1]

e_li = []

for i in s:
    e_li.append(i)
    
e_li[i_0] = str(i_1)

result = "".join(e_li) # it is used to convert list to normal string like this ['s', 'i', 'v', 'a'] convert to "siva"
print(result)


# input_1: gugan
# input_2: 0 s
# output: sugan
