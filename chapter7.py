current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

lists = ['uno', 'dos', 'tres', 'cuatro']

if list:
    print(list[0])
else:
    print('No existe')

message = input('enter some text\n')
print(f"You entered '{message}'")

message = input('enter your age: ')
age = int(message)
if age >= 21:
    print('you may drink')
else:
    print('you shell not drink')


# import chapter8
from chapter8 import build_profile as bp
profile = bp('a', 'b', c='d')

