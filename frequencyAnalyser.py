from concurrent.futures import process
from fileinput import filename
import os
import numpy as np
import matplotlib.pyplot as plot
import argparse

def main():
    # Get input from command line
    input = get_input()
    output_lines = []

    # Open file
    filePath = input["file_path"]
    fileName = os.path.basename(filePath)
    with open(filePath, "r") as file:
        input_lines = file.readlines()

    # Analyse frequency details
    if (input["voynich"]):
        (word_count, characters, frequencies, longest_word_length, longest_word, average_word_length ) = analyse_voynich(input_lines)
    else:
        (word_count, characters, frequencies, longest_word_length, longest_word, average_word_length ) = analyse(input_lines)

        plotting( characters, frequencies, fileName )

    # Output
    output_lines.append("Summary\n")
    output_lines.append("-------\n")
    output_lines.append("Number of words: " + str(word_count) +"\n")
    output_lines.append("Number of unique characters: " + str(len(characters)) + "\n")
    output_lines.append("Longest word: " + longest_word + " (" + str(longest_word_length) + " characters)\n")
    output_lines.append("Average word length: " + str(average_word_length) + "\n")
    output_lines.append("--------------------\n")
    output_lines.append("Character frequencies\n")
    output_lines.append("--------------------\n")
    char_freq_list = list(zip(characters, frequencies))
    char_freq_list.sort(key=lambda x: x[1], reverse=True)
    for (character, frequency) in char_freq_list:
        output_lines.append(character + ": " + str(frequency) + "\n")

    output_path = "./texts/" + fileName + "_frequency_analysis.txt"
    with open(output_path, "w") as file:
       for line in output_lines:
           file.write(line)

# Performs Voynich Manuscript specific analysis
def analyse_voynich(lines):
    unique_characters = []
    longest_word_length = 0
    word_count = 0
    word_len_sum = 0
    longest_word = []

    for line in lines:
        words = line.split()
        word_count += len(words)
        for word in words:
            characters = constructVMCharacters(word)
            for character in characters:
                if character not in unique_characters:
                    unique_characters.append(character)

            word_len_sum += len(characters)

            # Iteratively calculate longest word
            if len(characters) > longest_word_length:
                longest_word_length = len(characters)
                longest_word = word
            
    frequency = np.zeros(len(unique_characters))
    for line in lines:
        words = line.split()

        for word in words:
            characters = constructVMCharacters(word)
            for character in characters:
                if character in unique_characters:
                    index = unique_characters.index(character)
                    frequency[index] = frequency[index] + 1
            
    
    average_word_length = word_len_sum / word_count

    return word_count, unique_characters, frequency, longest_word_length, longest_word, average_word_length

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
    longest_word_length = 0
    word_count = 0
    word_len_sum = 0
    longest_word = ""
    
    for line in lines:
        words = line.split()
        
        for word in words:
            for character in word:
                # Get unique characters
                if character not in unique_characters:
                    unique_characters.append(character)

            word_len_sum += len(word)

            # Iteratively calculate longest word
            if len(word) > longest_word_length:
                longest_word_length = len(word)
                longest_word = word
        
        word_count += len(words)

    frequency = np.zeros(len(unique_characters))
    for line in lines:
        for word in line:
            for char in word : 
                if char in unique_characters :
                    index = unique_characters.index(char)
                    frequency[index] = frequency[index] + 1
            
    
    average_word_length = word_len_sum / word_count

    return word_count, unique_characters, frequency, longest_word_length, longest_word, average_word_length

def plotting(symbols, frequency, fileName) :
    # Plotting Frequency Analysisimport matplotlib.pyplot as plt
    freq = plot.figure()
    plot.bar(symbols, frequency)
    plot.xlabel("Character")
    plot.ylabel("Number of Occurences")
    plot.title("Frequency Analysis of " + fileName + ".txt")
    plot.savefig("./figures/" + fileName +"_freq_analysis.png")

def get_input():
    parser = argparse.ArgumentParser(description="Voynich Manuscript Frequency Analyser", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("file_path", help="The path to the file to be analysed. The file must be a .txt file.")
    parser.add_argument("--voynich", action="store_true", help="Apply Voynich specific analysis rules.")
    args = parser.parse_args()
    input = vars(args)
    return input

if __name__ == "__main__":
    main()