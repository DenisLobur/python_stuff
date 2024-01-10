cars = ['bmw', 'audi', 'toyota', 'mercedes']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if 'toyota' in cars:
    print('yes')

if 'audi' not in cars:
    print('no audi')
else:
    print('audi in list')