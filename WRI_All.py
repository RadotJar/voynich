import os
import statistics
from turtle import color
import numpy as np
import argparse
import math
import statistics
import matplotlib.pyplot as plott

def main() :
    #input = get_input()
    directory = ["Species-Plantarum(I-III)", "Die-Epiphytische-Vegetation-Amerikas", "A-Preliminary-Dissertation-on-the-Mechanisms-of-the-Heavens"
    , "voynich-manuscript.txt_formatted", "voynich-manuscript_Herbal.txt_formatted"]
    #directory = ["test3", "WRI_2", "test_WRI"]
    #fileName = os.path.basename(filePath)


    #change name of file for WRI plot, basically good to call it a category 
    type_of_plots = "WRI Analysis on Assorted Texts with Voynich (Herbal)"
    
    #"/texts/"

    filePath1 = os.getcwd() + "/texts/" + directory[0] + ".txt"
    text1 = format_text(filePath1)

    filePath2 = os.getcwd() + "/texts/" + directory[1] + ".txt"
    text2 = format_text(filePath2)

    filePath3 = os.getcwd() + "/texts/" + directory[2] + ".txt"
    text3 = format_text(filePath3)

    filePath4 = os.getcwd() + "/texts/" + directory[3] + ".txt"
    text4 = format_text(filePath4)

    filePath5 = os.getcwd() + "/texts/" + directory[4] + ".txt"
    text5 = format_text(filePath5)

    # filePath6 = os.getcwd() + "/texts/" + directory[5] + ".txt"
    # text6 = format_text(filePath6)

    # filePath7 = os.getcwd() + "/texts/" + directory[6] + ".txt"
    # text7 = format_text(filePath7)

    # filePath8 = os.getcwd() + "/texts/" + directory[7] + ".txt"
    # text8 = format_text(filePath8)

    spacings_list1 = [] # for a single text
    string_recurring1 = [] # for single text

    spacings_list2 = [] 
    string_recurring2 = []

    spacings_list3 = []
    string_recurring3 = []

    spacings_list4 = [] 
    string_recurring4 = []

    spacings_list5 = []
    string_recurring5 = []

    spacings_list6 = [] 
    string_recurring6 = []

    spacings_list7 = []
    string_recurring7 = []

    spacings_list8 = []
    string_recurring8 = []

    # list of lists for all word spacings (1 text)
    spacings_list1, string_recurring1, characters_recurring1 = word_spacings_all(text1)
    spacings_list2, string_recurring2, characters_recurring2 = word_spacings_all(text2)
    spacings_list3, string_recurring3, characters_recurring3 = word_spacings_all(text3)
    spacings_list4, string_recurring4, characters_recurring4 = word_spacings_all(text4)
    spacings_list5, string_recurring5, characters_recurring5 = word_spacings_all(text5)
    # spacings_list6, string_recurring6, characters_recurring6 = word_spacings_all(text6)
    # spacings_list7, string_recurring7, characters_recurring7 = word_spacings_all(text7)
    # spacings_list8, string_recurring8, characters_recurring8 = word_spacings_all(text8)


    # print("Spacings: ")
    # for i in range(len(spacings_list1)) :
    #     print(string_recurring1[i] + " " + str(spacings_list1[i]))
        
    # print("")
    # print("Recurring Characters")
    # print(characters_recurring1)

    # list_of_spacings_list.append(spacings_list1)
    # list_of_recurring_characters.append(characters_recurring1)

    results(type_of_plots, directory, spacings_list1, spacings_list2, spacings_list3,
        spacings_list4, spacings_list5, spacings_list6, spacings_list7, spacings_list8, 
        characters_recurring1, characters_recurring2, characters_recurring3, characters_recurring4, 
        characters_recurring5)


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

def results(fileName, directory, spacings1, spacings2, spacings3, spacings4, spacings5, spacings6, spacings7, spacings8,
     WR_characters1 :dict, WR_characters2 :dict, WR_characters3 :dict, WR_characters4, 
     WR_characters5 :dict) :
  
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

    # print(characters1)
    # print(WRC_val1, len(WRC_val1))


    #second text
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

    # print(characters3)
    # print(WRC_val3, len(WRC_val3))

    #Fourth text
    std_norm4 = []

    for space in spacings4 :
        print(space)
        ave = statistics.mean(space)
        std = statistics.stdev(space)
        #print(ave,std)
        std_norm4.append(std/ave)
    
    # print("")
    # print("average:")
    # print(ave)
    # print("")
    # print("normalised standard deviation")
    # print(std_norm3)

    std_norm4.sort(reverse=True)
    characters4, WRC_val4 = [], []

    characters4 = sorted(WR_characters4, key=WR_characters4.get)

    for c in characters4 :
        if(WR_characters4[c] > 0):
            WRC_val4.append(WR_characters4[c])

    #Fifth text
    std_norm5 = []

    for space in spacings5 :
        print(space)
        ave = statistics.mean(space)
        std = statistics.stdev(space)
        #print(ave,std)
        std_norm5.append(std/ave)
    
    # print("")
    # print("average:")
    # print(ave)
    # print("")
    # print("normalised standard deviation")
    # print(std_norm3)

    std_norm5.sort(reverse=True)
    characters5, WRC_val5 = [], []

    characters5 = sorted(WR_characters5, key=WR_characters5.get)

    for c in characters5 :
        if(WR_characters5[c] > 0):
            WRC_val5.append(WR_characters5[c])

    # #sixth text
    # std_norm6 = []

    # for space in spacings6 :
    #     #print(space)
    #     ave = statistics.mean(space)
    #     std = statistics.stdev(space)
    #     #print(ave,std)
    #     std_norm6.append(std/ave)
    
    # # print("")
    # # print("average:")
    # # print(ave)
    # # print("")
    # # print("normalised standard deviation")
    # # print(std_norm3)

    # std_norm6.sort(reverse=True)
    # characters6, WRC_val6 = [], []

    # characters6 = sorted(WR_characters6, key=WR_characters6.get)

    # for c in characters6 :
    #     if(WR_characters6[c] > 0):
    #         WRC_val6.append(WR_characters6[c])

    # #seventh text
    # std_norm7 = []

    # for space in spacings7 :
    #     #print(space)
    #     ave = statistics.mean(space)
    #     std = statistics.stdev(space)
    #     #print(ave,std)
    #     std_norm7.append(std/ave)
    
    # # print("")
    # # print("average:")
    # # print(ave)
    # # print("")
    # # print("normalised standard deviation")
    # # print(std_norm3)

    # std_norm7.sort(reverse=True)
    # characters7, WRC_val7 = [], []

    # characters7 = sorted(WR_characters7, key=WR_characters7.get)

    # for c in characters7 :
    #     if(WR_characters7[c] > 0):
    #         WRC_val7.append(WR_characters7[c])

    # #seventh text
    # std_norm8 = []

    # for space in spacings8 :
    #     #print(space)
    #     ave = statistics.mean(space)
    #     std = statistics.stdev(space)
    #     #print(ave,std)
    #     std_norm8.append(std/ave)
    
    # # print("")
    # # print("average:")
    # # print(ave)
    # # print("")
    # # print("normalised standard deviation")
    # # print(std_norm3)

    # std_norm8.sort(reverse=True)
    # characters8, WRC_val8 = [], []

    # characters8 = sorted(WR_characters8, key=WR_characters8.get)

    # for c in characters8 :
    #     if(WR_characters8[c] > 0):
    #         WRC_val8.append(WR_characters8[c])

    #first plot
    plott.bar(characters1, WRC_val1, width=0.5, color='red')
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
    plott.bar(characters3, WRC_val3, width=0.5)
    plott.xlabel("Recurring Characters")
    plott.ylabel("Number of ocurrences")
    plott.title("Most Recurring Characters in " + directory[2])
    plott.savefig(os.getcwd() + "/WRC_figures/" + directory[2] +"_WRC.png") 
    plott.clf()

    #fourth plot
    plott.bar(characters4, WRC_val4, width=0.5 , color='black')
    plott.xlabel("Recurring Characters")
    plott.ylabel("Number of ocurrences")
    plott.title("Most Recurring Characters in " + directory[3])
    plott.savefig(os.getcwd() + "/WRC_figures/" + directory[3] +"_WRC.png") 
    plott.clf()

    #fifth plot
    plott.bar(characters5, WRC_val5, width=0.5, color='black')
    plott.xlabel("Recurring Characters")
    plott.ylabel("Number of ocurrences")
    plott.title("Most Recurring Characters in " + directory[4])
    plott.savefig(os.getcwd() + "/WRC_figures/" + directory[4] +"_WRC.png") 
    plott.clf()

    # #sixth plot
    # plott.bar(characters6, WRC_val6, width=0.5, color='black')
    # plott.xlabel("Recurring Characters")
    # plott.ylabel("Number of ocurrences")
    # plott.title("Most Recurring Characters in " + directory[5])
    # plott.savefig(os.getcwd() + "/WRC_figures/" + directory[5] +"_WRC.png") 
    # plott.clf()

    # #seventh plot
    # plott.bar(characters7, WRC_val7, width=0.5, color='purple')
    # plott.xlabel("Recurring Characters")
    # plott.ylabel("Number of ocurrences")
    # plott.title("Most Recurring Characters in " + directory[6])
    # plott.savefig(os.getcwd() + "/WRC_figures/" + directory[6] +"_WRC.png") 
    # plott.clf()

    # #Eigth plot
    # plott.bar(characters8, WRC_val8, width=0.5)
    # plott.xlabel("Recurring Characters")
    # plott.ylabel("Number of ocurrences")
    # plott.title("Most Recurring Characters in " + directory[7])
    # plott.savefig(os.getcwd() + "/WRC_figures/" + directory[7] +"_WRC.png") 
    # plott.clf()

    # print("1:", std_norm1)
    # print("2:", std_norm2)
    # print("3:", std_norm3)

    plott.plot(range(len(std_norm1)), std_norm1, label=directory[0], color='green')
    plott.plot(range(len(std_norm2)), std_norm2, label= directory[1], color='red')
    plott.plot(range(len(std_norm3)), std_norm3, label = directory[2], linestyle='dashed')
    plott.plot(range(len(std_norm4)), std_norm4, label = directory[3],  linestyle='dashed', color='black')
    plott.plot(range(len(std_norm5)), std_norm5, label = directory[4], linestyle='dotted', color='black')
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
