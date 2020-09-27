import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
  word_completion = "_" * len(word) #Initially empty
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("Game started!")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess = raw_input('Please guess a letter: ').upper();
    if len(guess) == 1 and guess.isalpha():
      if guess not in word:
        print(guess, "is not in the word.")
        tries -= 1
        guessed_letters.append(guess)
      elif guess in guessed_letters:
        print("You already guessed the letter", guess)
      else:
        print("Good job,", guess, "is in the word!")
        guessed_letters.append(guess)
        word_as_list = list(word_completion)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        word_completion = "".join(word_as_list)
        if "_" not in word_completion:
          guessed = True

    else:
      print("Not a valid guess")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

  if guessed:
    print("Congrats, you Win!")
  else:
    print("You ran out of tries. The word was " + word + ".")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
  word = get_word()
  play(word)
  play_again = raw_input("Play Again? (Y/N) ").upper()
  while play_again == "Y":
    word = get_word()
    play(word)

if __name__ == "__main__":
    main()
