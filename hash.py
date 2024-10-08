n = int(input())

integer_list = map(int,input().split())

t = tuple(integer_list)
hashed_value = hash(t)
print(hashed_value)



