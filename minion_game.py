
def minion_game(string):
    vowels = "AEIOU"
    stuert_score = 0
    kevin_score = 0
    string_length = len(string)


    for i in range (string_length):
        if string[i] in vowels:
            kevin_score = kevin_score + string_length -i

        else:
            stuert_score = stuert_score+ string_length -i

    if stuert_score > kevin_score:
        print("Stuart", stuert_score)
    else:
        print("Kevin",kevin_score)
        
string = input()
minion_game(string)