# TYPE DATA SKALAR / SEQUENCE
print('THIS IS TYPE DATA SKALAR')
car1 = 'BMW'
car2 = 'TESLA'
car3 = 'MERCI'
car4 = 'JEEP'

print(car1)
print(car2)
print(car3)
print(car4)

# TYPE DATA LIST/ARRAY
print('\nTHIS IS TYPE DATA LIST / ARRAY')

car = ['BMW','TESLA','MERCI','JEEP']
print(car)
car.append('TOYOTA')
print(car)

# SHOW MY ELECTRIC CAR
print('\nMY ELECTRIC CAR!')

print(f'This is my new {car[1]}!')

# SHOW MY CARS with For & In
print('\nMY GARAGE!')

for i in car:
    print(f'This is my new {i}!')

# SHOW MY CARS with For & In Range
print('\nMY NEW GARAGE')

for i in range(0, len(car)):
    print(f'Hello Guys! this is my new {car[i]}!')



