import random
import words as w
import player as p
import database as db

conn = db.create_connection()
db.create_table(conn)

new_or_old = int(input("1. for new player 2. To move one: "))

if new_or_old == 1:
    newPlayer = p.login()

    db.add_player(conn, newPlayer)
db.viewPlayerData(conn)
player_id = int(input("Select player using their id: "))

wordsSelection = w.words
# get random word from wordsSelection
word = random.choice(wordsSelection)

letters = ["_"] * len(word)
print(letters)


# have the user guess a letter

def received_letter():
    body = 7
    wins = 0
    losses = 0

    while True:

        if "_" not in letters:
            print("You won")
            wins += 1
            break

        if body == 0:
            print("You lose")
            losses += 1
            break

        guess = input("Enter a Letter: ")
        if guess in word:
            index = word.index(guess)
            while letters[index] != "_":
                index = word.index(guess, index + 1)
            letters[index] = guess

        else:

            body -= 1

        print(letters)

    db.update_player_stats(conn,player_id,wins,losses)


received_letter()
