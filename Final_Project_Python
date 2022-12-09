#FINAL PROJECT
#Shelemiah Sotelo
#8823190
#December2022


# imports
import random
import time
import sys

# Constants
CLASSIC = "classic"
TIME_ATTACK = "time-attack"
LIFELINE = "lifeline"
SUDDEN_DEATH = "sudden_death"

# Modes:
# Classic - 7 questions will be scored based on the time answered
# Time-attack - timer will be set, how many questions player can answer within the given time 
# Lifeline - player has 5 tries
# Sudden_death - one try only
# Settings to be used inside game. 7 questions to represent BTS members
settings = {
  "number_of_questions": 7,
  "timer": 10,
  "mode": CLASSIC, # classic, time-attack, lifeline, sudden_death
  "time-attack": 60, # sample time of 1 minute
  "choice": "numbers" # letters or numbers
}

####################### Start of Classes/Functions #######################

# Class to be used to change color on console
class colors:
  WHITE = "\u001b[37m"
  GREEN = "\033[92m"
  RED = "\033[91m"
  PURPLE = "\033[0;35m"

# Class to easily create a question object
class Quiz:
  # For creating instance of quiz class
  def __init__(self, list):
    try:
      self.question = list[0]

      # Limited to 5 choices only
      self.choice_map = ['a', 'b', 'c', 'd', 'e']
      self.choices = list[1].split(',')

      # Check if there is a choice that always needs to be at the bottom
      self._aoda = "all of the above"
      self._noda = "none of the above"

      try:
        self._aoda_index = self.choices.index(self._aoda)
      except ValueError:
        self._aoda_index = -1
      # Remove AODA or NODA before shuffle
      if self._aoda_index>=0:
        self.choices.pop(self._aoda_index)

      try:
        self._noda_index = self.choices.index(self._noda)
      except ValueError:
        self._noda_index = -1
      if self._noda_index>=0:
        self.choices.pop(self._noda_index)

      # Randomizing the choices
      random.shuffle(self.choices)

      # Put AODA or NODA at the bottom
      if self._aoda_index>=0:
        self.choices.append(self._aoda)
      if self._noda_index>=0:
        self.choices.append(self._noda)


      # Searches for the index of correct answer from the choices
      self.answer = self.choices.index(list[2].strip())

      self.read_time = int(list[3])
      
    except:
      print("There is an issue with the question bank .txt file. Please contact programmer to fix")

  # Method to display question to console
  def show_question(self, id):
    print("\n{}) {}".format(str(id+1), self.question))

  # Method to display choices to console
  def show_choices(self):
    if settings["choice"].lower() == "letters":
      for choice_id, choice in enumerate(self.choices):
        print("   {}. {}".format(self.choice_map[choice_id], choice))
    elif settings["choice"].lower() == "numbers":
      for choice_id, choice in enumerate(self.choices):
        print("   {}. {}".format(choice_id+1, choice))
  
  # Method to get answer from user and return correct or not
  def score_answer(self):
    before = time.time()

    while True:
      ans = input("Your answer: ")
      ans = ans.strip()
      after = time.time()
      # Time elapsed to answer the question
      anstime = after - before

      if settings["choice"].lower() == "letters":
        try:
          if self.choice_map.index(ans.strip().lower())==self.answer:
            print("{}Correct!{}".format(colors.GREEN, colors.WHITE))
            return self.calc_score(anstime)
          else:
            print("{}Wrong{}".format(colors.RED, colors.WHITE))
            # No score for wrong answers
            return [0, anstime]
        except ValueError:
          # Error message when choice is not available
          print('Choose from a-{} only'.format(self.choice_map[len(self.choices)-1]))
          continue

      elif settings["choice"].lower() == "numbers":
        try:
          if int(ans)==(self.answer+1):
            print("{}Correct!{}".format(colors.GREEN, colors.WHITE))
            return self.calc_score(anstime)
          elif int(ans) > len(self.choices) or int(ans) < 1:
            raise ValueError("Choose from 1-{} only".format(len(self.choices)))
          else:
            print("{}Wrong{}".format(colors.RED, colors.WHITE))
            # No score for wrong answers
            return [0, anstime]
        except ValueError:
          print('Enter integers from 1-{} only'.format(len(self.choices)))
          continue

  # Function for calculating score
  def calc_score(self, anstime):
    # Score calculated based on the time remaining. As time decreases, the score decreases too. 
    if settings["mode"]==CLASSIC:
      real_time = anstime - self.read_time
      if real_time < 0:
        real_time = 0
      remaining = settings["timer"] - real_time

      max_score_per_question = 100/settings["number_of_questions"]
      # This can become negative. Either have a setting to control if this will allow negatives
      return [max_score_per_question*(remaining/settings["timer"]), anstime]

    elif settings["mode"] == TIME_ATTACK or settings["mode"] == LIFELINE or settings["mode"] == SUDDEN_DEATH:
      return [1, anstime]

 
# Put a timer in console
def start_timer(timer):
  for remaining in range(timer, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("The quiz begins in {:2d}".format(remaining)) 
    sys.stdout.flush()
    time.sleep(1)
  sys.stdout.write("\rStart!                    \n")

####################### End of Classes/Functions #######################



########################### Start of flow ###########################

# Print the BTS logo
# It will print it as purple first, then will change it to white.
# Must use PowerShell or cmd
print(colors.PURPLE)                 
print("     ____ _____ ____          ")
print("    | __ )_   _/ ___|   |\  /|")
print("    |  _ \ | | \___ \   | || |")
print("    | |_) || |  ___) |  | || |")
print("    |____/ |_| |____/   |/  \|")
print(colors.WHITE)

# TODO: Can implement a login here (for future upgrade)

# Print welcome message for the quiz
print("\nWelcome to BTS quiz show\n")


# Ask user for mode of the game
print("Please choose mode (1-4): \n1. Classic - 7 questions to answer. Score will be based on how fast player can answer the questions.  \n2. Time-attack - Score will be based on how many questions will be answered in 60 seconds. \n3. Lifeline - You only have 5 lives. The game will end after 5 wrong answers. \n4. Sudden Death - The game will end after the first wrong answer.")
modeInput = int(input().strip())
if modeInput == 1:
    settings["mode"]=CLASSIC

elif modeInput == 2:
    settings["mode"]=TIME_ATTACK

elif modeInput == 3:
    settings["mode"]=LIFELINE

elif modeInput == 4:
    settings["mode"]=SUDDEN_DEATH

else:
    settings["mode"]=CLASSIC

# Confirmation of chosen mode
print("You've chosen:", settings["mode"].capitalize())

List_of_Questions = []
user = {
  "username": "",
  "score": 0,
  "times": [],
  "lives": 5
}

# Ask player's info
print("Please insert username: ")
user["username"]=input()


# Print the instruction
print("Choose the correct answer. (1-4)")

# Open question bank
# We can specify the directory if we want
BTS_Quiz_bank = "BTS_Quiz_bank.txt"
with open(BTS_Quiz_bank, 'r') as file:
  # Read each line. One line contains one question with its choices and answer
  for line in file:
    object= line.split('? ')
    List_of_Questions.append(Quiz(object))

  # close the file
  file.close()

# Also randomize the questions
random.shuffle(List_of_Questions)

#Start Timer
start_timer(5)

# Game will end after 7 questions, and score will be based on how fast player answered the 7 questions.
if settings["mode"] == CLASSIC:
  for id in range(0, settings["number_of_questions"]):
    item = List_of_Questions[id]

    item.show_question(id)
    item.show_choices()
    
    result = item.score_answer()

    user["score"] = user["score"]+result[0]
    user["times"].append(result[1])

# Game will be in 60 seconds, score will be base on how many questions the player can answer within 60 seconds. 
elif settings["mode"] == TIME_ATTACK:
  start_time = time.time()
  id = 0

  # Game will run until runbank runs out of questions.
  while time.time() - start_time < settings["time-attack"]:

    if (id+1) > len(List_of_Questions):
      print("Sorry no more questions from question bank. More questions soon")
      break

    item = List_of_Questions[id]

    item.show_question(id)
    item.show_choices()

    result = item.score_answer()

    user["score"] = user["score"]+result[0]
    user["times"].append(result[1])
    id += 1

elif settings["mode"] == LIFELINE or settings["mode"] == SUDDEN_DEATH:

  # Only 1 life for sudden death
  if settings["mode"] == SUDDEN_DEATH:
    user["lives"] = 1

  id = 0

  # Game will still run until question bank runs out of questions. 
  # Game will end after 5 wrong answers for LIFELINE
  # Game will end after 5 wrong answers for SUDDEN_DEATH
  while user["lives"] > 0:

    if (id+1) > len(List_of_Questions):
      print("Sorry no more questions from question bank. More questions soon")
      break

    item = List_of_Questions[id]

    item.show_question(id)
    item.show_choices()

    result = item.score_answer()

    if(result[0]) == 0:
      user["lives"] -= 1

    user["score"] = user["score"]+result[0]
    user["times"].append(result[1])
    id += 1


print("\n", end="")

# Print final game score
print("Congratulations ARMY! \nYour final score is: {:.2f}".format(user["score"]))
