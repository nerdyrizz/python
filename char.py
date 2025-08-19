string = input("Enter a word: ")
char = input("Enter a character to count: ")
i = 0
count = 0
while i <len(string):
    if string[i] == char:
        count += 1
    i += 1
print(char, "occurs", count, "times in" , string)