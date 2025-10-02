# diff types of sets in python
# set of integers
my_set = {1,2,3,4,5}
print(my_set)

# set of mixed datatypes
my_set = {3, "Smaira", 6.7, 89, True}
print(my_set)

#set cannot have duplicates
my_set = {1,2,3,67,5,67,2,6,34,1,3,1,2}
print(my_set)

# we can make a set from a list
my_set = set([1,2,3,4,2,4,1,3,4,2,1,2,3,2,1,3,4,2,4,5])
print(my_set, "\n")

# remove a number from a set
num_set = set([1,3,4,2,4,2,4,2,1,4,5,2,1,3,4])
print("orginal set:")
print(num_set)
num_set.pop()
print("Set after emoving the first element:")
print(num_set)