# THIS IS MY NEW CHAPTER ABOUT TYPE DATA LIST IN PYTHON #
print('Show Country Data List from Euro :')
euro = ['Germany', 'Spain', 'England', 'France']
print(euro)

# SHOW THE DATA FROM SPECIFIC INDEX #
print('\nShow Country Data List in Third Index :')
print(euro[2]) # In Python, The Data List Start from 0 (Zero) #

# SHOW THE DATA WITH REPETITION (FOR) #
print('\nShow Country Data List with For :')
for i in euro:
    print(i)

# SHOW THE DATA WITH LEN FUNCTION IN REPETITION #
print('\nShow Country Data with Length of List :')
for i in range (0, len(euro)): # Len is the one of function we can use to show data from the length of list #
    print(euro[i])

# STEP TO ADD NEW DATA IN THE END OF LIST #
print('\nAdd One New Country Data in The End :')
euro.append('Netherland')
for i in range (0, len(euro)):
    print(euro[i])

# STEP TO CLEAR ALL DATA LIST #
print('\nClear All Country Data from List :')
euro.clear()
for i in range (0, len(euro)):
    print(euro[i])

# CHANGE DATA FROM SPECIFIC INDEX #
menu = ['Juice', 'Steak', 'Salad', 'Pudding'] # We create new data again
print('\nChange First Menu :')
menu[0] = 'Coffee'
for i in range (0, len(menu)):
    print(menu[i])

# DELETE OR MOVE SPECIFIC DATA TO ANOTHER VARIABLE WITH POP #
vegetarian = menu.pop(2) # You must create new variable with pop function
print('\nMenu without Vegetarian Food :')
for i in range (0, len(menu)):
    print(menu[i])

print('\nThis is Vegetarian Food :')
print(vegetarian) # Here you can see the data which get pop out from the list