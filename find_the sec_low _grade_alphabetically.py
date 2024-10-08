n = int(input())


class_1 = []

for i in range (n):
    name = input()
    grade = float(input())

    class_1.append([name, grade])
    
uniq_grade = sorted(set( student [1] for student in class_1))
sec_low_grade = uniq_grade[1]

stud_with_sec_low = [ students[0] for students in class_1 if students[1] == sec_low_grade]

final = []
for result in stud_with_sec_low:
    final.append(result)
final.sort()

for finall_result in final:
    print(finall_result)
    






    
    
