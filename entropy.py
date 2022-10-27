from fileinput import filename
import numbers
import os
import numpy as np
import argparse
import math
import statistics
import matplotlib.pyplot as plott
from concurrent.futures import process

def main() :

    #input = get_input()
    output_lines = []
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    # Grab text
    #filePath = input["file_path"]
    #fileName = os.path.basename(filePath)
    filePath = "./text.txt"
    with open(filePath, "r") as file:
        input_lines = file.readlines()

    # Find frequency
    if (input["voynich"]):
        (word_count, characters, frequencies) = analyse_voynich(input_lines)
    else:
        (word_count, characters, frequencies) = analyse(input_lines)

    prob = frequencies/word_count
    char_prob_dictionary = {}

    # Make dictionary of characters and their probabilities
    for i in len(prob):
        char_prob_dictionary[characters[i]] = prob[i]

    text = format_text(filePath)

    entropy, entropy_num, entropy_word = entropy_score(char_prob_dictionary, text, classification)
    classification = classify(text, numbers)
    results(entropy, entropy_num, entropy_word, classification)

    output_lines.append("Summary\n")

    entropy_list = list(zip(characters, frequencies))
    entropy_list.sort(key=lambda x: x[1], reverse=True)

    for (character, frequency) in entropy_list:
        output_lines.append(character + ": " + str(frequency) + "\n")

    output_path = "./entropy/" + fileName + "_entropy.txt"
    with open(output_path, "w") as file:
       for line in output_lines:
           file.write(line)


def entropy_score(prob: dict, all_strings: list, classification :list) :
    score = []
    score_num = []
    score_word = []
    entropy = 0

    for s in range(len(all_strings)) :
        for char in s :
            entropy = entropy - prob[char]*math.log(prob[char],2)
        score.append(entropy)

        if (classification[s] == "Number") :
            score_num.append(entropy)
        else:
            score_word.append(entropy)

        entropy = 0

    return score, score_num, score_word

def format_text(text) :
    formatted, formatted_text = [], []
    file = open(text, 'r')
    text = file.readlines()
    file.close()

    for line_no in range(len(text)):
        formatted.append(text[line_no].replace("\n",""))
        formatted[line_no] = formatted[line_no].split(" ")

    for line in formatted : 
        for string in line:
            formatted_text.append(string)
        
    return formatted_text

def results(entropy_score:list, entropy_score_norm:list,  classification: list, fileName) :

    entropy_num, entropy_word = [], []

    for i in range(len(entropy_score)) :

        if (classification[i] == "Number") :
            entropy_num.append(entropy_score[i])
        
        else :
            entropy_word.append(entropy_score[i])

    ave_n = statistics.mean(entropy_num)
    ave_w = statistics.mean(entropy_word)

    entropy = plott.figure()
    plott.plot(range(len(entropy_score)), entropy_score)
    plott.xlabel("Index of words in Text")
    plott.ylabel("Entropy Score (Non-Normalised)")
    plott.title("Non-Normalised Entropy Scores of " + fileName)
    plott.savefig("./entropy_figures/" + fileName +"_entropy.png")   

    entropy_norm = plott.figure()
    plott.plot(range(len(entropy_score)), entropy_score)
    plott.xlabel("Rank of Recurring Words")
    plott.ylabel("Entropy Score (Normalised)")
    plott.title("Non-Normalised Entropy Scores of " + fileName)
    plott.savefig("./entropy_figures_norm/" + fileName +"_entropy_norm.png")   


def classify(all_strings: list, numbers: list) :
    classification = []
    list_of_lengths = []

    for string in all_strings :
        list_of_lengths.append(len(string))

        for character in string :
            num_flag = 0
            if character in numbers :
                num_flag = 1
                break

        if num_flag == 1 :
            num_count = num_count + 1
            classification.append("Number")

        else :
            word_count = word_count + 1
            classification.append("Word")
    
    return classification


# Performs Voynich Manuscript specific analysis
def analyse_voynich(lines):
    unique_characters = []
    word_count = 0
    word_len_sum = 0

    for line in lines:
        words = line.split()
        word_count += len(words)
        for word in words:
            characters = constructVMCharacters(word)
            for character in characters:
                if character not in unique_characters:
                    unique_characters.append(character)

            word_len_sum += len(characters)

    frequency = np.zeros(len(unique_characters))
    for line in lines:
        words = line.split()

        for word in words:
            characters = constructVMCharacters(word)
            for character in characters:
                if character in unique_characters:
                    index = unique_characters.index(character)
                    frequency[index] = frequency[index] + 1
            
    
    return word_count, unique_characters, frequency

# Constructs characters according to special VM rules
def constructVMCharacters(word):
    i = 0
    characters = []
    while i < len(word):
        character = ""
        if(word[i] == "{"):
            j = i
            while word[j] != "}":
                character += word[j]
                j += 1
            else:
                character += word[j]
            i = j
        elif(word[i] == "@"):
            j = i
            while word[j] != ";":
                character += word[j]
                j += 1
            else:
                character += word[j]
            i = j
        else:
            character = word[i]
        
        characters.append(character)
        i += 1
    return characters

# Performs general analysis for other texts
def analyse(lines):
    unique_characters = []
    word_count = 0
    
    for line in lines:
        words = line.split()
        
        for word in words:
            for character in word:
                # Get unique characters
                if character not in unique_characters:
                    unique_characters.append(character)
        
        word_count += len(words)

    frequency = np.zeros(len(unique_characters))
    for line in lines:
        for word in line:
            for char in word : 
                if char in unique_characters :
                    index = unique_characters.index(char)
                    frequency[index] = frequency[index] + 1
            
    
    return word_count, unique_characters, frequency


def get_input():
    parser = argparse.ArgumentParser(description="Entropy Analyser.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("text_path", help="The path to the directory of text to analyse.")
    args = parser.parse_args()
    input = vars(args)
    return input

if __name__ == "__main__":
    main()