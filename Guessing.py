secret_word = "car"
guess = ""
guess_count = 0
guess_limit = 3
end_game = False

while guess != secret_word and not(end_game):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        end_game = True

if end_game:
    print("Out of guesses, You Lose!!!")

if not(end_game):
    print("Congratulations, You've Won!")