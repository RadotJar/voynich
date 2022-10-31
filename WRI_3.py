import os
import statistics
import numpy as np
import argparse
import math
import statistics
import matplotlib.pyplot as plott

def main() :
    #input = get_input()
    directory = ["voynich-manuscript.txt_formatted", "voynich-manuscript_Language_A.txt_formatted", "voynich-manuscript_Language_B.txt_formatted"]
    #directory = ["test3", "WRI_2", "test_WRI"]
    #fileName = os.path.basename(filePath)


    #change name of file for WRI plot, basically good to call it a category 
    type_of_plots = "Voynich"
    
    #"/texts/"

    filePath1 = os.getcwd() + "/texts/" + directory[0] + ".txt"
    text1 = format_text(filePath1)

    filePath2 = os.getcwd() + "/texts/" + directory[1] + ".txt"
    text2 = format_text(filePath2)

    filePath3 = os.getcwd() + "/texts/" + directory[2] + ".txt"
    text3 = format_text(filePath3)

    spacings_list1 = [] # for a single text
    string_recurring1 = [] # for single text

    spacings_list2 = [] 
    string_recurring2 = []

    spacings_list3 = []
    string_recurring3 = []

    # list of lists for all word spacings (1 text)
    spacings_list1, string_recurring1, characters_recurring1 = word_spacings_all(text1)
    spacings_list2, string_recurring2, characters_recurring2 = word_spacings_all(text2)
    spacings_list3, string_recurring3, characters_recurring3 = word_spacings_all(text3)

    print("Spacings: ")
    for i in range(len(spacings_list1)) :
        print(string_recurring1[i] + " " + str(spacings_list1[i]))
        
    print("")
    print("Recurring Characters")
    print(characters_recurring1)

    # list_of_spacings_list.append(spacings_list1)
    # list_of_recurring_characters.append(characters_recurring1)

    results(type_of_plots, directory, spacings_list1, spacings_list2, spacings_list3, characters_recurring1, characters_recurring2, characters_recurring3)


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

def results(fileName, directory, spacings1, spacings2, spacings3, WR_characters1 :dict, WR_characters2 :dict, WR_characters3 :dict) :
    #first text
    std_norm1 = []

    for space in spacings1 :
        print(space)
        ave = statistics.mean(space)
        std = statistics.stdev(space)
        #print(ave,std)
        std_norm1.append(std/ave)
    
    # print("")
    # print("average:")
    # print(ave)
    # print("")
    # print("normalised standard deviation")
    # print(std_norm1)

    std_norm1.sort(reverse=True)
    characters1, WRC_val1 = [], []

    characters1 = sorted(WR_characters1, key=WR_characters1.get)

    for c in characters1 :
        if(WR_characters1[c] > 0):
            WRC_val1.append(WR_characters1[c])

    print(characters1)
    print(WRC_val1, len(WRC_val1))

    #first text
    std_norm2 = []

    for space in spacings2 :
        print(space)
        ave = statistics.mean(space)
        std = statistics.stdev(space)
        #print(ave,std)
        std_norm2.append(std/ave)
    
    # print("")
    # print("average:")
    # print(ave)
    # print("")
    # print("normalised standard deviation")
    # print(std_norm2)

    std_norm2.sort(reverse=True)
    characters2, WRC_val2 = [], []

    characters2 = sorted(WR_characters2, key=WR_characters2.get)

    for c in characters2 :
        if(WR_characters2[c] > 0):
            WRC_val2.append(WR_characters2[c])

    # print(characters2)
    # print(WRC_val2, len(WRC_val2))

    #third text
    std_norm3 = []

    for space in spacings3 :
        print(space)
        ave = statistics.mean(space)
        std = statistics.stdev(space)
        #print(ave,std)
        std_norm3.append(std/ave)
    
    # print("")
    # print("average:")
    # print(ave)
    # print("")
    # print("normalised standard deviation")
    # print(std_norm3)

    std_norm3.sort(reverse=True)
    characters3, WRC_val3 = [], []

    characters3 = sorted(WR_characters3, key=WR_characters3.get)

    for c in characters3 :
        if(WR_characters3[c] > 0):
            WRC_val3.append(WR_characters3[c])

    print(characters3)
    print(WRC_val3, len(WRC_val3))

    #first plot
    plott.bar(characters1, WRC_val1, width=0.5, color = 'red')
    plott.xlabel("Recurring Characters")
    plott.ylabel("Number of ocurrences")
    plott.title("Most Recurring Characters in " + directory[0])
    plott.savefig(os.getcwd() + "/WRC_figures/" + directory[0] +"_WRC.png")  
    plott.clf()

    #second plot
    plott.bar(characters2, WRC_val2, width=0.5, color='green')
    plott.xlabel("Recurring Characters")
    plott.ylabel("Number of ocurrences")
    plott.title("Most Recurring Characters in " + directory[1])
    plott.savefig(os.getcwd() + "/WRC_figures/" + directory[1] +"_WRC.png")  
    plott.clf()

    #third plot
    plott.bar(characters3, WRC_val3, width=0.5) # Eng
    plott.xlabel("Recurring Characters")
    plott.ylabel("Number of ocurrences")
    plott.title("Most Recurring Characters in " + directory[2])
    plott.savefig(os.getcwd() + "/WRC_figures/" + directory[2] +"_WRC.png") 
    plott.clf()

    print("1:", std_norm1)
    print("2:", std_norm2)
    print("3:", std_norm3)

    plott.plot(range(len(std_norm1)), std_norm1, label=directory[0], color='black')
    plott.plot(range(len(std_norm2)), std_norm2, label= directory[1], color='black', linestyle='dotted')
    plott.plot(range(len(std_norm3)), std_norm3, label = directory[2], color='black', linestyle='dashed')
    plott.legend()
    plott.xlabel("Rank of Recurring Words Based on Standard Deviation (log)")
    plott.ylabel("Scaled Standard Deviation")
    plott.xscale('log')
    plott.title("Scaled Standard deviation of Recurring Words VS Most Varied Intervals")
    plott.savefig(os.getcwd() + "/WRI_figures/" + fileName +"_WRI.png")


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


def get_input():
    parser = argparse.ArgumentParser(description="Hidden Markov Model Text Analyser.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("text_path", help="The path to the directory of text to analyse.")
    args = parser.parse_args()
    input = vars(args)
    return input

if __name__ == "__main__":
    main()
