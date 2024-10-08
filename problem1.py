#problem 1

# small explanation (get all combination, then sum of each cobination is need to come not equal to n value)

x = int(input("Enter the X value : "))
y = int(input("Enter the Y value : "))
z = int(input("Enter the z value : "))

n = int(input("Enter the n value : "))


result = [[i,j,k]for i in range (x+1) for j in range (y+1) for k in range (z+1) if (i+j+k) != n]
print(result)
