import random
class FruitQuiz:
    # create a constructor
    def __init__(self):
       # create a dictionary to store questions and answers
       self.fruits = {
           'apple' : 'red', 'banana' : 'yellow', 'watermelon' : 'green', 'orange' : 'orange' }
       # function of the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("Whats the color of {}?".format(fruit))
            user_answer = input()
            if user_answer.lower() == color:
                print("Correct!")
            else:
                print("Wrong! The correct answer is {}".format(color))
            option = int(input("Enter 0 to continue or 1 to exit: "))
            if option == 1:
                break
print("Welcome to the Fruit Color Quiz!")
fq = FruitQuiz()
fq.quiz()
           
           