from random import randint, shuffle

alphabet: str = 'qwertyuiopasdfghjklzxcvbnm'
list_alphabet = []

for l in alphabet:
    list_alphabet.append(l)

print(shuffle(list_alphabet))
