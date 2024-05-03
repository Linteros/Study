word = input()

vowels = ['a', 'e', 'u', 'o', 'i']
a = [i for i in word if i not in vowels]
print(a)