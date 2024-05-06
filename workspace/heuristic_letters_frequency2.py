from _utils import *

frequency_dictionary = "data/frequency_letters.txt"
freq = load_dictionary(frequency_dictionary)

discarded_guesses = []

#heuristic based on the most frequent letters in the english language (all words, not only 5-letters words)
def heuristic_letters_frequency2(possible_solutions):
    frequencies = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        frequencies[letter] = 0
    for el in freq:
        el = el.split(',')
        frequencies[el[0].lower()] = el[1]
    final_word = chose_next_guess(possible_solutions, frequencies)
    return final_word

def chose_next_guess(possible_solutions, frequencies):
    total_value_words = {}
    if len(possible_solutions) > 1:
        for solution in possible_solutions:
            value = 0
            for i in range(5):
                for w,f in frequencies.items():
                    if solution[i] == w:
                        value += int(f)
                total_value_words[solution] = value
        min = 1000 #most common letter rank lower, so i need the solution with the minimun sum
        for word, value in total_value_words.items():
            if value < min and word not in discarded_guesses:
                final_word = word
                min = value
        discarded_guesses.append(final_word)
    else:
        final_word = possible_solutions[0]
    return final_word



