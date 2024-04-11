from random import choices
from functions import from_word_to_list

alphabet: str = 'qwertyuiopasdfghjklzxcvbnm'
list_alphabet: list = from_word_to_list(alphabet)
random_letters: list = choices(list_alphabet, k=5)

for l in random_letters:
    print(l, end='')
print()

user_input_list: list = from_word_to_list(input('Your turn: '))

if user_input_list == random_letters:
    print('You win!')
else:
    print('You are a looser')