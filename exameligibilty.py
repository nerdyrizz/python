medical_cause = input("Do have a medical cause Y/N: ")
att = int(input("Enter your attendance percentage: "))
if medical_cause.lower() == 'y': 
    print("You are eligible for the exam.")
else:
    if att >= 75:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")