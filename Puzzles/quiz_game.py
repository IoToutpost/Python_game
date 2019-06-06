import random

questions = ["As you like it", "The Tempest", "Measure for Measure",
             "Much Ado About Nothing", "The Comedy of Errors",
             "King Lear", "Cymbeline", "Hamlet", "Coriolanus", "Othello",
             "Love's Labour's Lost", "King John", "Julius Caesar", "Edward III"]

chosen_phrase = random.choice(questions)
chosen_phrase = chosen_phrase.upper()


vowels = ["A", "E", "I", "O", "U", " ", "'"]
puzzle = ""

for letter in chosen_phrase:
    if not letter in vowels:
        puzzle += letter


puzzle_with_spaces = ""

while len(puzzle) > 0:
    group_length = random.randint(1,5)
    puzzle_with_spaces += puzzle[:group_length] + " "
    puzzle = puzzle[group_length:]


print(puzzle_with_spaces)
guess = input("What is your guess? ")
guess = guess.upper()

if guess == chosen_phrase:
    print("That's correct!")
else:
    print("No. The answer is ", chosen_phrase)
