import os
import numpy as np
import matplotlib as plot

file_loc = os.getcwd() + "/German_Books/Book1-8/19755-8.txt"

file = codecs.open(file_loc, 'r', 'utf-8')
text = file.readlines()
file.close()

#print(text)

# Characteristics
symbols = []
average_word_length = 0
longest_word_length = 0
word_count = 0

# Creating array for unique symbols

text_for_symbols = text.replace(" ", "")

for line in text_for_symbols :
	for char in line:
		if char not in symbols :
			symbols.append(char)

# Finding word count
word_count = len(text_for_symbols)

# Average word cound and longest word

for word in text_for_symbols :
	if len(word) > longest_word_length:
		longest_word_length = len(word)

	average_word_length = average_word_length + len(word)

average_word_length = average_word_length/word_count


# Frequency Analysis
frequency = np.zeroes(len(symbols))

for line in text_for_symbols :
	for char in line : 
		if char in symbols :
			index = symbols.index(char)
			frequency[index] = frequency[index] + 1


def plotting()
# Plotting Frequency Analysis
plot.bar()

plot.xticks(/len(symbols), frequency, )
plot.xlabel("Symbols")
plot.ylabel("Frequency")
plot.title("Frequency Analysis of Text")