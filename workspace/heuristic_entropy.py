from _utils import * 
import math
from tqdm import tqdm
import random

patterns_dictionary = "data/patterns.txt"
patterns = load_dictionary(patterns_dictionary)

already_tried = []

#FIRST HEURISTIC: entropy
def heuristic_entropy(possible_solutions, guesses, attempts):
    entropy_list = {}
    max = -1
    max_word = ""
    #print(len(possible_solutions))
    #print(possible_solutions)
    if (len(possible_solutions) == 1): return possible_solutions[0]
    else:
        progress_bar = tqdm(total=len(guesses), desc="Progress")
        for word in guesses:
            sum = sum_entropy(word, possible_solutions)
            entropy_list[word] = sum
            progress_bar.update(1)
        progress_bar.close()
        for w,s in entropy_list.items():
            if s > max:
                max = s
                max_word = w  
        #print(max_word, max) 
        if (max < 2) or attempts == 6: #if entropy equals 1, i have equiprobable solutions, i need to try one
            for element in already_tried[:]:
                if element in possible_solutions:
                    possible_solutions.remove(element)
            #print(possible_solutions)
            max_word = random.choice(possible_solutions)   
            already_tried.append(max_word)     
        return max_word

def sum_entropy(word, possible_solutions):
    sum=0
    for pattern in patterns:
        sum+=get_entropy(word, pattern, possible_solutions)
    return sum

def get_entropy(word, pattern, possible_solutions): #implements the formula
    probability = calculate_probability(word, pattern, possible_solutions)
    if (probability == 0):
        return 0.0
    e = probability * math.log2((1/probability))
    return e

def calculate_probability(word, pattern, possible_solutions):
	feasible_sol = get_all_possible_solutions(possible_solutions, word, pattern)
	if(feasible_sol==[]):
		return 0
	return len(feasible_sol)/len(possible_solutions)

def get_all_possible_solutions(possible_solutions, word, pattern):
	pos_solutions = []
	for solution in possible_solutions:
		if testing_pattern(solution, word, pattern):
			pos_solutions.append(solution)
	return pos_solutions

def testing_pattern(guess, word, pattern):
	match_count = {}
	for i in range(5):
		if pattern[i] == "g":
			if guess[i] != word[i]:
				return False
			else:
				if(guess[i] not in match_count):
					match_count[word[i]] = 1
				else:
					match_count[word[i]] += 1
	for i in range(5):
		if pattern[i] == "y":
			if guess[i] not in word:
				return False
			else:
				if (guess[i]==word[i]):
					return False
				if(guess[i] not in match_count):
					match_count[guess[i]] = 1
				else:
					if (word.count(guess[i]) <= match_count[guess[i]]):
						return False
					else:
						match_count[guess[i]] += 1
	for i in range(5):
		if pattern[i] ==  "b":
			if word[i] == guess[i]:
				return False
			else:
				for j in range(i,len(pattern)):
					if guess[i] == guess[j] and pattern[j]=="y":
						return False
				if guess[i] in word:
					if guess[i] in match_count:
						if word.count(guess[i]) > match_count[guess[i]]:
							return False
					elif guess[i] not in match_count:
						return False
	return True