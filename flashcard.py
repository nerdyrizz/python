class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + ' ( '+self.meaning+' )'
    
flash = []
print('Welcome to the flashcard app!')
# the following loop will be repeated while the user wants to add flashcards
while True:
    word = input("Enter the name you want to add to the flashcard: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))
    option = input(" Enter 0 if you want to enter more flashcards, else enter 1: ")
    if(option):
        break

# displaying all flashcards
print("\nHere are your flashcards:")
for i in flash:
    print(">",i)
