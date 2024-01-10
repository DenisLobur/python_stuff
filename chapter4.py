magicians = ['alice', 'bob', 'charlie', 'molina']
for magician in magicians:
    print(magician)
print(magicians)

for magician in magicians:
    print(f"{magician.title()} you're doing a great job!")
    print(f"I can't wait to your next trick {magician.title()}")

for value in range(1, 5):
    print(value)

numbers = list(range(5))
print(numbers)

squares = []
for value in range(1, 10):
    square = value ** 2
    squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value ** 2 for value in range(10)]
print(squares[:])

my_food = ['apple', 'banana', 'cherry']
my_friends_food = my_food[:]
my_food.append('orange')
print(my_food)
print(my_friends_food)

dimensions = (100, 200)
print(dimensions[0])
print(dimensions[1])
print(dimensions)
