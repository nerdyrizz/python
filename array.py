import array as arr

# create an array
array_num = arr.array('i', [1,3,5,3,7,9,3])
print("original array:" + str(array_num))

#count the number of occurences
print("Number of occuences of 3 in the said array:" + str(array_num.count(3)))

# reverse the array
array_num.reverse()
print("Array after reversing:" + str(array_num))

