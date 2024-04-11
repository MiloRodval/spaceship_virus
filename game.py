from random import choices

alphabet: str = 'qwertyuiopasdfghjklzxcvbnm'
list_alphabet: list = []
user_input_list: list = []

for l in alphabet:
    list_alphabet.append(l)

random_letters: list = choices(list_alphabet, k=5)

for l in random_letters:
    print(l, end='')

user_input = input('Your turn: ')

for x in user_input:
    user_input_list.append(x)

if user_input_list == random_letters:
    print('You win!')
else:
    print('You are a looser')