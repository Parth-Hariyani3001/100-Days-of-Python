import random
from hangman_art import logo,stages
from hangman_words import word_list

word = random.choice(word_list)
answer = []
for i in range(len(word)):
    answer.append("_")
lives = 7

word = list(word)
answer = list(answer)
end_of_game = False

print(logo)

while not end_of_game:
    print("Word to Guess ", ''.join(answer))

    user_guess = input("Enter a letter to guess : ")

    if len(user_guess) > 1:
        print("Guess single letter only")
        continue
    elif(user_guess in word):
        idx = word.index(user_guess)
        word[idx] = "_"
        answer[idx] = user_guess
    else:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life")
        lives -= 1
        print(stages[lives])
        print(f"******************{lives}/{len(stages)} LIVES LEFT************")
        if(lives == 0):
            end_of_game = True
            print("You lose")
        continue

    if "_" not in answer:
        end_of_game = True
        print("You win")