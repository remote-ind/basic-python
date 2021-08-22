"""
TYPE DATA DICTIONARY
It's connecting between KEY and VALUE
As known as KVP / KEY VALUE PAIR
"""

print('TYPE DATA DICTIONARY WITH SIMPLE CASE')
bike = {'kawasaki': 'Ninja', 'honda': 'CBR', 'yamaha': 'R25', 'ducati': 'Diavel'}

print(bike)
print(bike['kawasaki'])
print(bike['ducati'])

print('\nTYPE DATA DICTIONARY WITH COMPLEXITY')
moto_gp = {
    'location': 'Catalunya',
    'rider': [
        {'name': 'Lorenzo', 'number': 99},
        {'name': 'Vinales', 'number': 12},
        {'name': 'Marquez', 'number': 93},
        {'name': 'Rossi', 'number': 46}
    ]
}

print(moto_gp)
print(f"\nOur winner from {moto_gp['location']} sircuit is :")
print(f"First winner {moto_gp['rider'][2]}")
print(f"Second place {moto_gp['rider'][1]}")
print(f"Third place {moto_gp['rider'][0]}")
print(f"Our crash and dumped rider on {moto_gp['location']} is rider with number {moto_gp['rider'][3]['number']}")
print(f"Good Bye {moto_gp['rider'][3]['name']}!!!")
