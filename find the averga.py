n = int(input())

student_mark = {}

for i in range (n):
    name, *line = input().split() # * is on eof the operator used to collect all data
    mark = list(map(float, line)) # map function is used to convert the type to type for example list to float from line.
    student_mark[name] = mark
query_name = input()    

for stud in student_mark:
    if stud == query_name:
        mark = student_mark[stud]
        leng = len(mark)
        average = sum(mark)// leng
        print(average) # finall ans
        print(type(mark)) # Test (all Test is not needed incase you want just delete)
        print(len(mark)) # Test
        print("True") # Test
    
print(stud) # Test

print(student_mark)    

'''
input format :
2 ===> it is used to get how many input
siva 30 40
guru 20 40
guru --->it is used you want which person average
'''