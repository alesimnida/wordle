from _utils import *

frequency_dictionary = "data/frequency_words.txt"
frequencies = load_dictionary(frequency_dictionary)

#SECOND HEURISTIC: based on the frequency of the words in the english language (from wofram language and google english books ngram)
def heuristic_words_frequency(possible_solutions):
    max = 0
    max_frequency_word = ""
    for solution in possible_solutions:
        for frequency in frequencies:
            el = frequency.split(',')
            if el[0] == solution and float(el[1]) > float(max):
                max = el[1]
                max_frequency_word = el[0]
    #print(max_frequency_word, str(max))
    return max_frequency_word

        

