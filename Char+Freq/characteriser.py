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
text_for_symbols = []
text_for_average = []

# Creating array for unique symbols
#print(text)
temp_count = 0

for line_no in range(len(text)):
	text_for_symbols.append(text[line_no].replace(" ", ""))
	text_for_symbols[line_no] = text_for_symbols[line_no].replace("\n","")
	#print(text_for_symbols)
	
	text_for_average.append(text[line_no].replace("\n",""))
	text_for_average[line_no] = (text_for_average[line_no].split(" "))

#print(text_for_average)
#print(text_for_symbols)

for line in text_for_symbols :
	for char in line:
		if char not in symbols :
			symbols.append(char)

# Finding word count
word_count = 0

# Average word cound and longest word

for line in text_for_average :
	for word in line :
		#print(word)
		if len(word) > longest_word_length:
			longest_word_length = len(word)
			longest_word = word

		word_count	 = word_count + 1

		average_word_length = average_word_length + len(word)
	# print(len(word))

#print(word_count)
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
print("Average Length:", average_word_length)
print("Longest Word: ", longest_word)
print("Word Count: ", word_count)
print("Symbols: ", symbols)
print("Frequency: ", frequency)


# for i in range(len(frequency)) :
# 	print(frequency[i], (symbols[i]))
#print(type(frequency[0]))
plotting(symbols, frequency)