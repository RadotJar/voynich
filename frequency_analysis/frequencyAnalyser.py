from concurrent.futures import process
import numpy as np
import matplotlib.pyplot as plot
import argparse

def main():
    # Get input from command line
    input = get_input()
    
    # Open file
    file_path = "./texts/" + input["file_name"] + ".txt"
    with open(file_path, "r") as file:
        input_lines = file.readlines()

    # Analyse frequency details
    if (input["voynich"]):
        (characters, frequencies, longest_word_length, longest_word, average_word_length ) = analyse_voynich(input_lines)
    else:
        (characters, frequencies, longest_word_length, longest_word, average_word_length ) = analyse(input_lines)

        plotting( characters, frequencies, input["file_name"] )

        print(longest_word, longest_word_length)
    # Write output
    # output_path = "./texts/" + input["file_name"] + "_formatted.txt"
    # with open(output_path, "w") as file:
    #    for line in output_lines:
    #        file.write(line)

# Performs Voynich Manuscript specific analysis
def analyse_voynich(lines):
    return

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

    return unique_characters, frequency, longest_word_length, longest_word, average_word_length


def plotting(symbols, frequency, fileName) :
    # Plotting Frequency Analysisimport matplotlib.pyplot as plt
    freq = plot.figure()
    plot.bar(symbols, frequency)
    plot.xlabel("Character")
    plot.ylabel("Number of Occurences")
    plot.title("Frequency Analysis of " + fileName + ".txt")
    plot.savefig("./figures/" + fileName +"_freq_analysis.png")

def get_input():
    parser = argparse.ArgumentParser(description="Voynich Manuscript Formatter", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("file_name", help="The name of the file to be formatted. The file must be a .txt file stored in ./texts/, containing a transcription of the Voynich Manuscript written in EVA and formatted in IVTFF.")
    parser.add_argument("--voynich", action="store_true", help="Apply Voynich specific analysis rules.")
    args = parser.parse_args()
    input = vars(args)
    return input

if __name__ == "__main__":
    main()