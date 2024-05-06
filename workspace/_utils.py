import datetime

#current_time = datetime.datetime.now()
#timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M")

def naming(choice):
    if choice == 1:
        file_test = open(f"results/results_letters_frequency.txt","a")
    elif choice == 2:
        file_test = open(f"results/results_letters_wordle.txt","a")
    elif choice == 3:
        file_test = open(f"results/results_words_frequency.txt","a")
    elif choice == 4:
        file_test = open(f"results/results_entropy.txt","a")
    elif choice == 5:
        file_test = open(f"results/results_entropy_special.txt","a")
    return file_test

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words
