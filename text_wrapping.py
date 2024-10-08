
# text_wrapping

def wrap_string(string, width):

    for i in range (0, len(string), width):
        print(i)
        print(string[i:i+width])
    
string = input()
width = int(input())
wrap_string(string, width)


s = input()
y = s[0:len(s):4]
print(y)

# or another method same problem


# text_wrapping

def wrap_string(string, max_width):
    wrapped_string = [string[i:i+max_width] for i in range (0, len(string), max_width)]
    print(wrapped_string)
    print('\n'.join(wrapped_string))

    
string = input()
max_width = int(input())
wrap_string(string, max_width)


