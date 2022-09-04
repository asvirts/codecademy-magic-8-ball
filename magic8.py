import random

name = "Andrew"
question = "Will the Buccaneers win the Super Bowl?"
answer = ""
randomNumber = random.randint(1, 9)

print(name + " asks: " + question)

if randomNumber == 1:
  answer = "Yes, definitely."
elif randomNumber == 2:
  answer = "It is decidedly so."
elif randomNumber == 3:
  answer = "Without a doubt."
elif randomNumber == 4:
  answer = "Reply hazy, try again."
elif randomNumber == 5:
  answer = "Ask again later."
elif randomNumber == 6:
  answer = "Better not tell you now."
elif randomNumber == 7:
  answer = "My sources say no."
elif randomNumber == 8:
  answer = "Outlook not so good."
elif answer == 9:
  answer = "Very doubtful."
else:
  print("Woops. There's been an error.")

print(answer)