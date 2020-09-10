# Author: Mack Mason mjm8542@psu.edu
# Collaborator: Jiulong Tang jzt5526@psu.edu
# Collaborator: Brendan Corso bvc5434@psu.edu
# Collaborator Peter Schulman pks5481@psu.edu
# Section: 4
# Breakout: 6

def getLetterGrade(grade):
  grade = float(grade)
  if grade >= 93.0:
    return "A"
    grade = "A"
  elif grade < 93.0 and grade >= 90.0:
    return "A-"
    grade = "A-"
  elif grade < 90.0 and grade >= 87.0:
    return "B+"
    grade = "B+"
  elif grade < 87.0 and grade >= 83.0:
    return "B"
    grade = "B"
  elif grade < 83.0 and grade >= 80.0:
    return "B-"
    grade = "B-"
  elif grade < 80.0 and grade >= 77.0:
    return "C+"
    grade = "C+"
  elif grade < 77.0 and grade >= 70.0:
    return "C"
    grade = "C"
  elif grade < 70.0 and grade >= 60.0:
    return "D"
    grade = "D"
  else:
    return "F"
    grade = "F"
 
def run():
  grade = input("Enter your CMPSC 131 grade: ")
  newGrade = getLetterGrade(grade)
  print(f"Your letter grade for CMPSC 131 is {newGrade}.")


if __name__ == "__main__":
  run()