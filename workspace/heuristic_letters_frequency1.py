from _utils import * 

discarded_guesses = []

#we classify the frequency of each letter inside the possible solutions (restricting the search in the possible solution of five letters)
def heuristic_letters_frequency1(possible_solutions, guesses):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequency = {}
    for letter in alphabet:
        frequency[letter] = 0
    for letter in alphabet:
        for g in guesses:
            frequency[letter] += count_letter(letter, g)
    
    #print(frequency) #list of all the letters and their frequency
    next_guess = chose_next_guess(possible_solutions, frequency)
    return next_guess


def count_letter(letter, guess):
    count=0
    for i in range(5):
        if guess[i] == letter:
            count += 1
    return count

#for every letter in the possible solution, i sum the frequency of each letter. if the sum is the greater, it means the word contains the greater number of most frequent letters, and we choose that one
def chose_next_guess(possible_solutions, frequency):
    total_value_words = {}
    if len(possible_solutions) > 1:
        for solution in possible_solutions:
            value = 0
            for i in range(5):
                for w,f in frequency.items():
                    if solution[i] == w:
                        value += f
            total_value_words[solution] = value
            #print(total_value_words)
        max = 0
        for word, value in total_value_words.items():
            if value > max and word not in discarded_guesses:
                final_word = word
                max = value
        discarded_guesses.append(final_word)
    else:
        final_word = possible_solutions[0]
    #print(discarded_guesses)
    #print(final_word, max)
    return final_word




