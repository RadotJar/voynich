#HMM Program
from pomegranate import *
import os
import numpy as np

file_location = os.getcwd() + "/"
written_text = read_text(file_location)

emission_matrix = find_conditional_prob(written_text, )
transition_matrix = calculate_transition(written_text, )
HiddenMM = make_model(transition_matrix, emission_matrix)
analyse(Voynich, )


def find_conditional_prob(classified_text, text, states) :
#Calculate conditional probabilities based on sizes

	number_conditions = np.zeroes(states)
	word_conditions = np.zeroes(states)
	total_numbers = 0
	total_words = 0

	for i in range(classified_text.size()) :
		index = text[i].size() - 1

		if classified_text[i] == "Number" :
			number_conditions[index] = number_conditions[index] + 1
			total_numbers = total_numbers + 1

		elif classified_text[i] == "String" :
			word_conditions[index] = word_conditions[index] + 1
			total_words = total_words + 1

		else :
			print("Something Went Wrong")

	number_conditions = number_conditions/total_numbers
	word_conditions = word_conditions/total_words


def calculate_transition(classified_text) :
#calculate transition matrix probabilities based on data

	total_transitions = classified_text.size()-1
	num_to_num = 0
	num_to_string = 0
	string_to_num = 0
	string_to_string = 0

	transition_matrix = np.zeroes(2,2)

		for i in range(classes.size()-1):

			if classes[i+1] == "Number" and (classified_text[i+1] == "String"):
				num_to_string = num_to_string + 1

			elif classes[i+1] == "String" and (classified_text[i+1] == "String"):
				string_to_string = string_to_string + 1

			elif classes[i+1] == "String" and (classified_text[i+1] == "Number"):
				string_to_num = string_to_num + 1

			elif classes[i+1] == "Number" and (classified_text[i+1] == "Number"):
				num_to_num = num_to_num + 1

			else :
				print("Something Went Wrong")

		transition_matrix[0,0] = num_to_num/total_transitions
		transition_matrix[0,1] = num_to_string/total_transitions
		transition_matrix[1,0] = string_to_num/total_transitions
		transition_matrix[1,1] = string_to_string/total_transitions

		return transition_matrix


def make_model(transition, emission) :
#makes HiddenMM model, assumed first 

	HiddenMM = model.HiddenMarkovModel()
	start_prob = 2*[0]
	HiddenMM.add


	HiddenMM.bake()


def analyse(Voynich, ) :
# analyses the unknown text based on the model and notes what should be a number based on the sequence



def classify(text, alphabet, numbers) :
#traverses and classifies each word as either a string or a number

#returns: classification and counter for total numbers and words

	all_words = text.split(" ")
	num_count = 0
	word_count = 0
	classification = []

	for word in all_words :
		for character in word :
			if character in numbers :
				num_flag = 1
				break
		if num_flag == 1 :
			num_count = num_count + 1
			classification.append("Number")

		else :
			word_count = word_count + 1
			classification.append("String")

		num_flag = 0

	return classification, num_count, word_count

def find_conditional_prob(classifcation, list_of_lengths, length_longest, word_count, number_count, bool: extra_state) :
# calculates conditional probability based on length of words and their states
	word_cond, number_cond = [0] * len(length_longest)

	# loops through and counts the number of words and numbers with a certain length
	for words in range(len(list_of_lengths)) :

		if (classification[words] == "Number"):
			number_cond[list_of_lengths[words] -1 ] = number_cond[list_of_lengths[words] -1] + 1


		elif (classification[words] == "Word"):
			word_cond[list_of_lengths[words] -1 ] = number_cond[list_of_lengths[words] -1] + 1


	return word_cond/word_count, number_cond/number_count