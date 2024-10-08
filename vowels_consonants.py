
# find the vowels and consonants

s = input()
vowels = 'AEIOUaeiou'
vowe = []
const = []

for char in s:
    if char in vowels:
        vowe.append(char)
    else:
        const.append(char)


uniq_vow = set(vowe)
uniq_const = set(const)

print(f"this vowels only present in this sentence  : {''.join(uniq_vow)}")
print(f"this consonants only present in this sentence  : {''.join(uniq_const)}")
print()
print(''.join(vowe))
print(''.join(const))
