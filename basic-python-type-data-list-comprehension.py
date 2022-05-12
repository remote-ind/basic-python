# IN THIS CHAPTER WE WILL DO LIKE PREVIOUS LIST TECHNIC, BUT WE WILL USE COMPREHENSION ON THE LIST

# USING DEL FUNCTION TO DELETE 1 LIST IN THE VARIABLE
print('This is continent of the world :')
continent = ['Africa', 'Australia', 'America', 'Asia', 'Europe', 'Antarctica']
del continent[-1]
for i in range(0, len(continent)):
    print(continent[i])

# USING LIST COMPREHENSION TO DELETE ALL LIST IN THE VARIABLE
print('\nThis is the end of the world :')
continent = ['Africa', 'Australia', 'America', 'Asia', 'Europe', 'Antarctica']
del continent[:]
# This is list comprehension Start : End, but we don't define the number of comprehension to delete all list
for i in range(0, len(continent)):
    print(continent[i])

# USING LIST COMPREHENSION WITH DEFINING START : END
print('\nThis is smallest continent of the world :')
continent = ['Africa', 'Australia', 'America', 'Asia', 'Europe', 'Antarctica']
del continent[0:4]
# This is list comprehension Start : End, but we don't define the number of comprehension to delete all list
for i in range(0, len(continent)):
    print(continent[i])

# USING MINUS IN LIST COMPREHENSION
print('\nThis is coldest continent of the world :')
continent = ['Africa', 'Australia', 'America', 'Asia', 'Europe', 'Antarctica']
del continent[0:-1]
# This is list comprehension Start : End, but we don't define the number of comprehension to delete all list
for i in range(0, len(continent)):
    print(continent[i])
