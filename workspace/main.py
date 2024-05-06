import time, player, random, _utils

def is_valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses

def evaluate_guess(guess, word):
    str = ""
    right_position = {}
    wrong_position = {}
    discarded = []
    already_found = []
    right_letter_pos_for_duplicate = {}

    #inizialize to check duplicate > documentation
    for i in range(5):
        if (guess[i] == word[i]):
            right_letter_pos_for_duplicate[i] = guess[i]


    for i in range(5):
        if (guess[i] == word[i]) and (right_letter_pos_for_duplicate[i] == guess[i]):
            already_found.append(guess[i]) #lo faccio per riempire già l'already found, altrimenti se ho la lettera 'e' (ripetizione 1) alla pos giusta 4 ma io analizzo la 'e' in pos 2, me la mette gialla quando dovrebbe darmela grigia
    for i in range(5):
        if (guess[i] == word[i]) and (right_letter_pos_for_duplicate[i] == guess[i]): #green
            str += "\033[32m" + guess[i]
            right_position[i] = guess[i]
            already_found.append(guess[i])
        else:
            if (guess[i] in word) and guess[i] not in already_found: #ci sono più occorrenze di quella lettera, una l'ho trovata le altre no
                for j in word:
                    if guess[i] == j:
                        wrong_position[i] = guess[i]
                str += "\033[33m" + guess[i] #yellow
            else:
                str += "\033[0m" + guess[i] #gray
                discarded.append(guess[i])

    feedback = str + "\033[0m"
    print("\033[34m" + ">>> FEEDBACK: " + "\033[0m" + feedback)

    return right_position, wrong_position, discarded, already_found


def wordle(guesses):

    choice = input("which heuristic? Insert '1' (frequency letters general), '2' (frequency letters wordle), '3' (frequency words), '4' (entropy) or '5' (special entropy)\n")
    if int(choice) != 1 and int(choice) != 2 and int(choice) != 3 and int(choice) != 4 and int(choice) != 5:
        print("please insert a valid choice")
        exit
    file_test = _utils.naming(int(choice))
    file_test.write("User chose heuristic: " + choice + "\n")
    print(" ")
    print(" ")
    start = "\033[34m" + "Welcome to Wordle!"
    print(start + " You have 5 attempts to guess a five-letters english word." + "\033[0m")
    secret_word = random.choice(guesses).lower()
    #secret_word = "tithe"
    file_test.write("Secret word is: " + secret_word + "\n")
    #secret_word = "globe"
    #secret_word = "canal"
    #secret_word = "jumpy" #da ritestare nel momento in cui hai sviluppato un'euristica
    #secret_word = "fanin"
    print("(Shh... the secret word is: " + secret_word + ")")

    max_attempts = 6
    attempts = 1

    start_time = time.time()
    while attempts <= max_attempts:
        if attempts == 1:
            if int(choice) == 5:
                guess = "tares" #highest entropy
            else:
                guess = "sitar" #fixed > documentation
            print("The first attempt is with the word: " + guess)
        else:
            print("Attempt " + str(attempts) + ". Intelligent player is chosing a guess...")
            guess = player.guess(right_position, wrong_position, discarded, guesses, already_found, int(choice))
            print("Player chose: " + guess)
        file_test.write("Attempt n: " + str(attempts) + ". Player choose guess: " + guess + "\n")
        
        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Please enter an English word with 5 letters.")
            file_test.close
            break

        if guess == secret_word:
            success_time = round(time.time() - start_time, 4)
            file_test.write("Player won\n")
            file_test.write("Time taken (in seconds): " + str(success_time) + "\n")
            file_test.write("Number of attempts: " + str(attempts) + "\n")
            file_test.write("---------------------------------------------\n")
            file_test.close
            print("\033[34m" + ">>> Congratulations! You guessed the word:" + "\033[0m " + secret_word)
            return

        attempts += 1
        right_position, wrong_position, discarded, already_found = evaluate_guess(guess, secret_word)
        
    if attempts > max_attempts:
        success_time = round(time.time() - start_time, 4)
        file_test.write("Time taken (in seconds): " + str(success_time) + "\n")
        #file_test.write("Number of attempts: " + str(attempts) + "\n")
        file_test.write("Player lost\n")
        file_test.write("---------------------------------------------\n")
        file_test.close
        print("\033[34m" +" >>> Game over. The secret word was:" + "\033[0m " + secret_word)
        return

guesses_dictionary = "data/guesses.txt"
guesses = _utils.load_dictionary(guesses_dictionary)

wordle(guesses)