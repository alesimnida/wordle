from heuristic_entropy import heuristic_entropy
from heuristic_words_frequency import heuristic_words_frequency
from heuristic_letters_frequency1 import heuristic_letters_frequency1
from heuristic_letters_frequency2 import heuristic_letters_frequency2

discarded_guess = []
discaded_letters_all = []
wrong_positions_all = {}
already_found_all = []

def guess(right_position, wrong_position, discarded, guesses, already_found, choice):

    choices_minus_discarded = []
    choices_right_position = []
    possible_solutions = []

    for a in already_found:
        already_found_all.append(a)

    if len(discarded) != 0:
        for d in discarded:
            discaded_letters_all.append(d)

        for e in already_found_all:
            for (i,d) in enumerate(discaded_letters_all):
                if e == d:
                    del discaded_letters_all[i] #TODO: così dovrei aver sistemato la cosa della lettera che si ripete/no?
    
        number_discarded = len(discaded_letters_all)
        for g in guesses:
            count = 0
            for d in discaded_letters_all:
                if (d not in g):
                    count = count + 1 #salvo tutte le parole che contemporaneamente non hanno NESSUNA delle lettere discarded
            if count == number_discarded:
                    choices_minus_discarded.append(g)
    else:
        choices_minus_discarded = guesses

    if len(right_position) != 0:
        number_right = len(right_position)
        for c in choices_minus_discarded:
            count = 0
            for pos,letter in right_position.items():
                if (c[pos] == letter):
                    count = count + 1
            if (count == number_right):
                choices_right_position.append(c)
    else:
        choices_right_position = choices_minus_discarded

    for pos,letter in wrong_position.items():
            wrong_positions_all[pos] = letter
    if len(wrong_positions_all) != 0:

        common_keys = set(wrong_positions_all.keys()) & set(right_position.keys())
        common_items = {key: wrong_positions_all[key] for key in common_keys if wrong_positions_all[key] == right_position.get(key)}
        for i, (p, l) in enumerate(common_items.items()):
            del wrong_positions_all[p]

        number_right_let_wrong_pos = len(wrong_positions_all)
        for c in choices_right_position:
            count = 0
            for pos,letter in wrong_positions_all.items():
                if (c[pos] != letter) and (letter in c):
                    count = count + 1
            if (count == number_right_let_wrong_pos):
                    possible_solutions.append(c)
    else:
        possible_solutions = choices_right_position

    if choice == 4 or choice == 5:
        final_guess = heuristic_entropy(possible_solutions, guesses)
    elif choice == 3:
        final_guess = heuristic_words_frequency(possible_solutions)
    elif choice == 2:
        #circoscritta alle possible solutions
        final_guess = heuristic_letters_frequency1(possible_solutions, guesses)
    elif choice == 1:
        #nella lingua inglese
        final_guess = heuristic_letters_frequency2(possible_solutions)
      
    return final_guess

