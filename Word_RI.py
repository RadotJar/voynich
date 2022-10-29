import os
import statistics
import numpy as np
import argparse
import math
import statistics
import matplotlib.pyplot as plott

def main() :
    #input = get_input()
    filePath = "test3"
    #fileName = os.path.basename(filePath)

    text = format_text(filePath + ".txt")
     #change the title
    name_of_file = "Botanical Texts 2"
    #Dummy
    x = True

    list_of_spacings_list = [] #for all texts
    spacings_list = [] # for a single text
    string_recurring = []

    # list of lists for all word spacings (1 text)
    if (x == True) :
        spacings_list, string_recurring, characters_recurring = word_spacings_all(text)

        print("Spacings: ")
        for i in range(len(spacings_list)) :
            print(string_recurring[i] + " " + str(spacings_list[i]))
        
        print("")
        print("Recurring Characters")
        print(characters_recurring)

        list_of_spacings_list.append(spacings_list)

        results(name_of_file, spacings_list, characters_recurring)

    # Works for all texts
    else :
        spacings_list = word_spacings_all(text)
        list_of_spacings_list.append(spacings_list)
        #plot_multiple(list_of_spacings_list)


def word_spacings_all(text : list) :
    unique_strings = []
    interval_current = 0
    spacings_all = []
    intervals = []
    characters_recurring = {}
    strings_recurring = []

    for i in range(len(text)):
        if (text[i] not in unique_strings) and (i != len(text)-1):
            unique_strings.append(text[i])

            for j in range(i+1, len(text)):
                #print(text[j], text[i])
                if text[j] == text[i]:
                    intervals.append(interval_current)
                    interval_current = 0

                    # find characters that exist in recurring words
                    for char in text[j] :
                        if char not in characters_recurring :
                            characters_recurring[char] = 1
                        else :
                            characters_recurring[char] += 1
                elif ((j == len(text)-1) and (text[j] != text[i])) :
                    interval_current = 0

                else :
                    interval_current += 1
        
                if ((j == len(text)-1) and (len(intervals) > 1)) :
                    spacings_all.append(intervals)
                    intervals = []
                    strings_recurring.append(text[i])

    return spacings_all, strings_recurring, characters_recurring

def results(fileName, spacings, WR_characters :dict) :
    std_norm = []

    for space in spacings :
        print(space)
        ave = statistics.mean(space)
        std = statistics.stdev(space)
        #print(ave,std)
        std_norm.append(std/ave)
    
    print("")
    print("average:")
    print(ave)
    print("")
    print("normalised standard deviation")
    print(std_norm)

    std_norm.sort(reverse=True)
    characters, WRC_val = [], []

    characters = sorted(WR_characters, key=WR_characters.get)

    for c in characters :
        WRC_val.append(WR_characters[c])

    print(characters)
    print(WRC_val, len(WRC_val))

    plott.bar(characters, WRC_val, width=0.5)
    plott.xlabel("Recurring Characters")
    plott.ylabel("Number of ocurrences")
    #plott.xticks(range(len(WRC_val)), label=characters)
    plott.title("Most Recurring Characters in " + fileName)
    plott.savefig(os.getcwd() + "/WRC_figures/" + fileName +"_WRC.png")    

    plott.clf()
    plott.plot(range(len(std_norm)), std_norm)
    plott.xlabel("Rank of Recurring Words Based on Standard Deviation (log)")
    plott.ylabel("Normalised Standard Deviation")
    plott.xscale('log')
    plott.title("Standard deviation of Recurring Words VS Most Varied Intervals")
    plott.savefig(os.getcwd() + "/WRI_figures/" + fileName +"_WRI.png")


# def plot_multiple(directory, spacings) :

#     std_norm = []
#     for space in spacings :
#         ave = statistics.mean(space)
#         std = statistics.stdev(space)
#         std_norm.append(std/ave)
    
#     std_norm.sort(reverse=True)
   
#     plott.plot(range(len(std_norm)), std_norm)
#     plott.xlabel("Rank of Recurring Words")
#     plott.ylabel("Normalised Standard Deviation")
#     plott.set_xscale('log')
#     plott.title("Standard deviation of Recurring Words VS Most Varied Intervals")
#     plott.legend()
#     plott.savefig("./WRI_figures/" + fileName +"_WRI.png") 

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


def get_input():
    parser = argparse.ArgumentParser(description="Hidden Markov Model Text Analyser.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("text_path", help="The path to the directory of text to analyse.")
    args = parser.parse_args()
    input = vars(args)
    return input

if __name__ == "__main__":
    main()