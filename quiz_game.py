print("Welcome to the Quiz Game!")

playing = input("Are you ready to play? (yes/no) ")
if playing == "yes":
    print("Great! Let's play!")
else:
    print("Okay, maybe another time.")

score = 0
answer = input("What does CPU stand for? ")
if answer.casefold() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.casefold() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.casefold() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.casefold() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " out of 4 correct!")
print("You scored " + str(score/4*100) + "%!")
print("Thanks for playing!")