import os
import numpy as np
import matplotlib.pyplot as plot
import codecs

def plotting(symbols, frequency) :
# Plotting Frequency Analysisimport matplotlib.pyplot as plt
	#freq = plot.figure()
	plot.bar(symbols, frequency)
	#freq.xticks(len(symbols), frequency)
	plot.xlabel("Symbols")
	plot.ylabel("Frequency")
	plot.title("Frequency Analysis of Text")
	plot.show()

	plot.savefig("freq_analysis.png")


file_loc = os.getcwd() + "/English_test/test.txt"

file = open(file_loc, 'r')
text = file.readlines()
file.close()

#print(text)

# Characteristics
symbols = []
average_word_length = 0
longest_word_length = 0
word_count = 0

# Creating array for unique symbols
text = text[0]
text_for_symbols = text.replace(" ", "")
text_for_average = text.split(" ")
#print(text_for_average)
#print(text_for_symbols)

for line in text_for_symbols :
	for char in line:
		if char not in symbols :
			symbols.append(char)

# Finding word count
word_count = len(text_for_average)

# Average word cound and longest word

for word in text_for_average :
	if len(word) > longest_word_length:
		longest_word_length = len(word)
		longest_word = word

	average_word_length = average_word_length + len(word)
	# print(len(word))

average_word_length = average_word_length/word_count


# Frequency Analysis
frequency = np.zeros(len(symbols))

for line in text_for_symbols :
	for char in line : 
		if char in symbols :
			index = symbols.index(char)
			frequency[index] = frequency[index] + 1

# print(frequency)
# print(symbols)
# print(len(frequency), len(symbols))
# print("average: ", average_word_length)
print("Averae Length:", average_word_length)
print("Longest Word: ", longest_word)


# for i in range(len(frequency)) :
# 	print(frequency[i], (symbols[i]))
#print(type(frequency[0]))
plotting(symbols, frequency)