# Armstrong number

n = input()
x = len(n)
y = int(n)

result = 0

for i in n:
    result = result + int(i)**x

print(type(result))    

if result ==  y:
    print("this is armstrong number")
else:
    print('this is not armstrong number')
    
