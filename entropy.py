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
    classification = []
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    # Grab text
    #filePath = input["file_path"]
    #fileName = os.path.basename(filePath)
    filePath = "./test2.txt"
    with open(filePath, "r") as file:
        input_lines = file.readlines()

    fileName = "test_2"
    vm = True

    if (vm == True):
        (char_count, characters, frequencies) = analyse_voynich(input_lines)
        threshold = 0.5
        prob = frequencies/char_count
        char_prob_dictionary = {}

        for i in range(len(prob)):
            char_prob_dictionary[characters[i]] = prob[i]

        vm = format_text(filePath)
        PN, PN_norm = entropy_voynich(char_prob_dictionary, vm, threshold)
        output_lines.append("Possible numbers based Entropy (Not normalised) = " + str(PN) + "\n") 
        output_lines.append("Possible numbers based Entropy (Normalised) = " + str(PN_norm) + "\n")
        
        output_path = "./entropy/" + fileName + "_entropy.txt"
        with open(output_path, "w") as file:
            for line in output_lines:
                file.write(line)
        exit()
         
    else:
        (char_count, characters, frequencies) = analyse(input_lines)
    
        prob = frequencies/char_count
        char_prob_dictionary = {}

        for i in range(len(prob)):
            char_prob_dictionary[characters[i]] = prob[i]
            #print(characters[i] + " " +str(frequencies[i]))

        text = format_text(filePath)
        classification = classify(text, numbers)

        print("probabilities")
        print(char_prob_dictionary)
        print("\n")


        entropy, entropy_norm = entropy_score(char_prob_dictionary, text, classification)
        ent = []

        for char in characters:
            ent.append(char_prob_dictionary[char]*math.log(char_prob_dictionary[char],2))

    # print("Feature Entropy")
    # print(ent) 

    # print("Entropy Values:")
    # print(entropy)
    # print("")
    # print("Entropy Values Normalised:")
    # print(entropy_norm)

        ave_num, ave_word, ave_num_norm, ave_word_norm = results(entropy, entropy_norm, classification, fileName)
            
    output_lines.append("Summary\n")
    output_lines.append("\n")
    output_lines.append("-------")
    output_lines.append("character entropy")
    output_lines.append("-------")
    output_lines.append("\n")

    entropy_list = list(zip(characters, ent))
    entropy_list.sort(key=lambda x: x[1], reverse=True)
    for (character, ent) in entropy_list:
        output_lines.append(character + ": " + str(ent) + "\n")
    
    output_lines.append("\n")
    output_lines.append("-------")
    output_lines.append("string entropy")
    output_lines.append("-------")
    output_lines.append("\n")

    entropy_list = list(zip(text, entropy, entropy_norm))
    for (text, entropy, entropy_norm) in entropy_list:
        output_lines.append(text + ": " + "entropy = " + str(entropy) + ", entropy normalised = " + str(entropy_norm) + "\n")
    
    output_lines.append("\n")
    output_lines.append("Average Entropy (Number) = " + str(ave_num) + "\n")
    output_lines.append("Average Entropy (Word) = " + str(ave_word) + "\n")
    output_lines.append("Average Entropy Normalised (Number) = " + str(ave_num_norm) + "\n")
    output_lines.append("Average Entropy Normalised (Word) = " + str(ave_word_norm) + "\n")

    output_path = "./entropy/" + fileName + "_entropy.txt"
    with open(output_path, "w") as file:
       for line in output_lines:
           file.write(line)


def entropy_score(prob: dict, all_strings: list, classification :list) :
    score = []
    score_norm = []
    entropy = 0

    print(len(all_strings))
    print(len(classification))

    for s in range(len(all_strings)) :
        for char in all_strings[s] :
            entropy = entropy - prob[char]*math.log(prob[char],2)
        score.append(entropy)
        score_norm.append(entropy/len(all_strings[s]))

        entropy = 0

    return score, score_norm

def entropy_voynich(prob: dict, all_strings: list, threshold) :
    possible_num = []
    possible_num_norm = []
    entropy = 0

    # print(all_strings)
    # print(prob)
    #print(len(all_strings))

    for s in range(len(all_strings)) :
        string = constructVMCharacters(all_strings[s])
        for char in string :
            entropy = entropy - prob[char]*math.log(prob[char],2)
        norm = entropy/len(string)

        # assesses based on threshold
        if(entropy > threshold) :
           possible_num.append(all_strings[s])
        if (norm > threshold) :
            possible_num_norm.append(all_strings[s])
        entropy = 0

    return possible_num, possible_num_norm

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
            if(len(string) != 0):
                formatted_text.append(string)
        
    return formatted_text


def results(entropy_score:list, entropy_score_norm:list,  classification: list, fileName) :

    entropy_num, entropy_word = [], []
    entropy_norm_num, entropy_norm_word = [], []

    for j in range(len(classification)):

        if (classification[j] == "Number") :
            entropy_num.append(entropy_score[j])
            entropy_norm_num.append(entropy_score_norm[j])
        else:
            entropy_word.append(entropy_score[j])
            entropy_norm_word.append(entropy_score_norm[j])

    ave_n = statistics.mean(entropy_num)
    ave_w = statistics.mean(entropy_word)

    ave_n_norm = statistics.mean(entropy_norm_num)
    ave_w_norm = statistics.mean(entropy_norm_word)

    entropy = plott.figure()
    plott.plot(range(len(entropy_score)), entropy_score)
    plott.xlabel("Index of words in Text")
    plott.ylabel("Entropy Score (Non-Normalised)")
    plott.title("Non-Normalised Entropy Scores of " + fileName)
    plott.savefig("./entropy_figures/" + fileName +"_entropy.png")   

    entropy_norm = plott.figure()
    plott.plot(range(len(entropy_score_norm)), entropy_score_norm)
    plott.xlabel("Rank of Recurring Words")
    plott.ylabel("Entropy Score (Normalised)")
    plott.title("Non-Normalised Entropy Scores of " + fileName)
    plott.savefig("./entropy_figures_norm/" + fileName +"_entropy_norm.png")

    return ave_n, ave_w, ave_n_norm, ave_w_norm 

def classify(all_strings: list, numbers: list) :
    classification = []
    list_of_lengths = []
    num_count, word_count = 0, 0

    print(all_strings)
    
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
    char_count = 0

    for line in lines:
        words = line.split()
        for word in words:
            characters = constructVMCharacters(word)
            for character in characters:
                if character not in unique_characters:
                    unique_characters.append(character)
                    char_count+= 1

    frequency = np.zeros(len(unique_characters))
    for line in lines:
        words = line.split()

        for word in words:
            characters = constructVMCharacters(word)
            char_count += len(characters)
            for character in characters:
                if character in unique_characters: 
                    index = unique_characters.index(character)
                    frequency[index] = frequency[index] + 1
            
    
    return char_count, unique_characters, frequency

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
    char_count = 0
    
    for line in lines:
        words = line.split()
        
        for word in words:
            for character in word:
                # Get unique characters
                if character not in unique_characters:
                    unique_characters.append(character)

            char_count += len(word)

    frequency = np.zeros(len(unique_characters))
    for line in lines:
        for word in line:
            for char in word : 
                if char in unique_characters :
                    index = unique_characters.index(char)
                    frequency[index] = frequency[index] + 1
            
    
    return char_count, unique_characters, frequency


def get_input():
    parser = argparse.ArgumentParser(description="Entropy Analyser.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("text_path", help="The path to the directory of text to analyse.")
    args = parser.parse_args()
    input = vars(args)
    return input

if __name__ == "__main__":
    main()