tuplex = ("tuple", False, 12.30, 4)
print(tuplex)


tuplex = (2,4,6,8,10,12)
print(tuplex)
# tuples are immutable, so we cant add new elements
# using mrege of tuples options with the + operator u can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)

# counts the number of times of 50's apperance in the tuple
tuplex = (50, 89, 76, 67, 50, 50, 67)
print(tuplex.count(50))

tuplex = ( 2, 3, 4, 5, 6, 7, 3, 8, 9, 7)
# used tuple[start:stop] the start index is inclusive and the stop index is exclusive
_slice = tuplex[2:5]
print(_slice)