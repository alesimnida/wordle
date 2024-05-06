count_righe = 0
time = 0
attempts = 0
wins  = 0
losts = 0

choice = input("which heuristic? Insert '1' (frequency letters general), '2' (frequency letters wordle), '3' (frequency words), '4' (entropy) or '5' (special entropy)\n")
if int(choice) == 1:
    name = 'results/results_letters_frequency.txt'
elif int(choice) == 2:
    name = 'results/results_letters_wordle.txt'
elif int(choice) == 3:
    name = 'results/results_words_frequency.txt'
elif int(choice) == 4:
    name = 'results/results_entropy.txt'
else:
    name = 'results/results_entropy_special.txt'
    

print("Per euristica: ", choice)
with open(name, 'r') as file:
    # Ciclo attraverso ogni riga nel file
    for riga in file:
        if riga.startswith("-"):
            count_righe += 1
        if riga.startswith("Time"):
            time += float(riga.split(":")[1])
            #print(riga.split(":")[1])
        if riga.__contains__("Player won"):
            wins += 1
        if riga.__contains__("Player lost"):
            losts += 1
        if riga.startswith("Number of"):
            attempts += int(riga.split(":")[1])
    average_wins = (float(wins) / float(count_righe))*100
    average_loss = (float(losts) / float(count_righe))*100
    average_time = float(time) / float(count_righe)
    average_attempts = float(attempts) / float(count_righe)
    print(count_righe)
    print("Wins: ", str(average_wins))
    print("Loss: ", str(average_loss))
    print("Time: ", str(average_time))
    print("Attempts: ", str(average_attempts))