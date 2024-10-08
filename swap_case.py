def swap_case(string):
    
    j = []

    for i in (string):
        if i.isupper():
            j.append(i.lower())

        elif i.islower():
            j.append(i.upper())


    result = ''.join(j)
    print(result)
string = input()  
swap_case(string)
    
        
