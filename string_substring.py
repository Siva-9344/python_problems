
            

def count_substring(string, substring):
    count = 0

    for i in range (len(string)-len(substring)+1):

        if string[i:i+len(substring)] == substring:
            count +=1
    return count        
            

string = input()
substring = input()
count = count_substring(string, substring)
print(count)


# input -->sivava
# input -->va
# output --> 2 (because two times there)
