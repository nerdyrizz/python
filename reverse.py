string = input("Enter a string to reverse: ")
string2 = ""
for i in string:
    string2 = i + string2
print("Original string:", string)
print("Reversed string:", string2)