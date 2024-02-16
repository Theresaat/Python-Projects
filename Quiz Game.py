print("Hey, Welcome to Quizit!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()
print("Great! Let's play : ) ")

result = 0 

answer = input ("What does LOL Stand for? ")
if answer.lower() == "laugh out loud":
    print("Correct!")
    result += 1
else:
    print("Incorrect!")

answer = input ("What does TTYL Stand for? ")
if answer.lower() == "talk to you later":
    print("Correct!")
    result += 1
else:
    print("Incorrect!")

answer = input ("What does ROM Stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    result += 1
else:
    print("Incorrect!")

print(" You got " + str(result) + " question correct!")