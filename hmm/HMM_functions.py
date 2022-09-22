import numpy as np
from pomegranate import *
import os

def initial_and_transition(classified_text, transition_matrix, initial_prob, string_count, num_transitions, word_transitions, /, states=2) :
#calculate transition matrix probabilities based on data

	total_transitions = len(classified_text)-1
	num_to_num = transition_matrix[0][0]
	num_to_word = transition_matrix[0][1]
	word_to_num = transition_matrix[1][0]
	word_to_word = transition_matrix[1][1]

	transition_matrix = np.zeros([states,states])

	for i in range(total_transitions):

		# initial probabilities
		if (classified_text[i] == "Number") :
			initial_prob[0] += 1
			string_count += 1
		
		else :
			initial_prob[1] += 1
			string_count += 1

		# transition probablities
		if classified_text[i] == "Number" and (classified_text[i+1] == "Word"):
			num_to_word = num_to_word + 1
			num_transitions += 1

		elif classified_text[i] == "Word" and (classified_text[i+1] == "Word"):
			word_to_word = word_to_word + 1
			word_transitions += 1

		elif classified_text[i] == "Word" and (classified_text[i+1] == "Number"):
			word_to_num = word_to_num + 1
			word_transitions += 1

		elif classified_text[i] == "Number" and (classified_text[i+1] == "Number"):
			num_to_num = num_to_num + 1
			num_transitions += 1

		else :
			print("Something Went Wrong")

	transition_matrix[0,0] = num_to_num #num_transitions
	transition_matrix[0,1] = num_to_word #/num_transitions
	transition_matrix[1,0] = word_to_num #/word_transitions
	transition_matrix[1,1] = word_to_word #word_transitions

	return transition_matrix, initial_prob, string_count, num_transitions, word_transitions


def make_model(voynich, transition, emission, start, list_of_lengths) :

	observations, vm_text = observe_vm(voynich)

	num_dist = {}
	word_dist = {}

	print(emission)
	#print(emission[1][1])

	observed_sizes = list(range(1, max(list_of_lengths)+1))
	print(len(emission[0]))
	# print("obs: ", observed_sizes)
	#obserable_vals = list(map(chr,observed_sizes))
	print("obs: ", chr(observed_sizes[0]))

	for i in range(len(emission[0])) :
		num_dist.update({str(observed_sizes[i]): emission[0][i]})
		word_dist.update({str(observed_sizes[i]): emission[1][i]})

	print(num_dist)
	print(word_dist)

	d1 = DiscreteDistribution(num_dist)
	d2 = DiscreteDistribution(word_dist)

	state1_n = State(d1, name="Number")
	state2_w = State(d2, name="Word")

	model = HiddenMarkovModel('Model')
	model.add_states([state1_n, state2_w])
	model.add_transition(model.start, state1_n, start[0])
	model.add_transition(model.start, state2_w, start[1])

	model.add_transition(state1_n, state1_n, transition[0][0])
	model.add_transition(state1_n, state2_w, transition[0][1])

	model.add_transition(state2_w, state1_n, transition[1][0])
	model.add_transition(state2_w, state2_w, transition[1][1])
	
	model.bake()

	#print(observations)

	print(", ".join(state.name for i, state in model.viterbi(list(observations))[1]))
	result_states_string = (", ".join(state.name for i, state in model.viterbi(list(observations))[1]))

	result_states = result_states_string.split(", ")
	result_states.pop(0)

	return result_states, vm_text

def observe_vm(voynich) :
# analyses the unknown text based on the model and notes what should be a number based on the sequence
	vm_text = format_text(voynich)
	observations = ''
	print('text:')
	#print(vm_text)
	# for line in vm_text:
	for string in vm_text :
		observations = observations + (str(len(string)))

	#print(observations)
	return observations, vm_text

def analyse_vm(model_states, vm_text) :

	possible_numbers = []

	for string in range(len(vm_text)) :
		if (model_states[string] == "Number" and vm_text[string] not in possible_numbers) :
			possible_numbers.append(vm_text[string])

	return possible_numbers

def classify(all_strings, numbers, num_count, word_count) :
	classification = []
	list_of_lengths = []

	for string in all_strings :
		list_of_lengths.append(len(string))

		for character in string :
			num_flag = 0
			if character in numbers :
				num_flag = 1
				# print(character, num_flag)
				break
		# print("/n")
		if num_flag == 1 :
			num_count = num_count + 1
			classification.append("Number")

		else :
			word_count = word_count + 1
			classification.append("Word")
	
	longest_length = max(list_of_lengths)

	return classification, longest_length, list_of_lengths, num_count, word_count

def find_conditional_prob(classification, conditional_matrix, list_of_lengths, length_longest_word, number_count, word_count) :
# calculates conditional probability based on length of words and their states
	#word_cond, number_cond = [0] * len(length_longest_word)
	#conditional_matrix = np.zeros([2, len(length_longest_word)])

	if length_longest_word > len(conditional_matrix) :
		conditional_matrix = np.resize(conditional_matrix, (2, length_longest_word))

	# loops through and counts the number of words and numbers with a certain length
	for strings in range(len(list_of_lengths)) :

		if (classification[strings] == "Number"):
			conditional_matrix[0][list_of_lengths[strings] -1 ] = conditional_matrix[0][list_of_lengths[strings] -1] + 1

		elif (classification[strings] == "Word"):
			conditional_matrix[1][list_of_lengths[strings] -1 ] = conditional_matrix[1][list_of_lengths[strings] -1] + 1

	#word_cond/word_count
	#number_cond/number_count

	return conditional_matrix

def store_model(start_prob_dir, transition_dir, emisssion_dir, start_prob, transition_prob, emission_prob):
# saves matrix to txt file to allow to store currently trained model

    with open(start_prob_dir,'wb') as initial:
        for line in start_prob:
            np.savetxt(initial, line, fmt='%.2f')

    with open(transition_dir,'wb') as transition:
        for line in transition_prob:
            np.savetxt(transition, line, fmt='%.2f')

    with open(emisssion_dir,'wb') as emission:
        for line in emission_prob:
            np.savetxt(transition, line, fmt='%.2f')


def load_model(start_prob_dir, transition_dir, emisssion_dir):

    with open(start_prob_dir, 'r') as sp:
        start_prob = np.array([[float(num) for num in line.split(' ')] for line in sp])

    with open(transition_dir, 'r') as t:
        transition_prob = np.array([[float(num) for num in line.split(' ')] for line in t])

    with open(emisssion_dir, 'r') as e:
        emission_prob = np.array([[float(num) for num in line.split(' ')] for line in e])

    return start_prob, transition_prob, emission_prob

def final_prob(initial_prob, transition_matrix, emission_prob, string_count, num_transitions, word_transitions, num_count, word_count) :

	# converts count to probabilities
	transition_matrix[0,0] = transition_matrix[0,0]/num_transitions
	transition_matrix[0,1] = transition_matrix[0,1]/num_transitions
	transition_matrix[1,0] = transition_matrix[1,0]/word_transitions
	transition_matrix[1,1] = transition_matrix[1,1]/word_transitions

	initial_prob = initial_prob/string_count

	emission_prob[0,:] = emission_prob[0,:]/num_count
	emission_prob[1,:] = emission_prob[1,:]/word_count

	return initial_prob, transition_matrix, emission_prob

def format_text(input_directory) :

	# makes sure text is in a format for easy analysis. single list where each element is a string

	formatted, formatted_text = [], []
	file = open(input_directory, 'r')
	text = file.readlines()
	file.close()

	for line_no in range(len(text)):
		formatted.append(text[line_no].replace("\n",""))
		formatted[line_no] = formatted[line_no].split(" ")

	for line in formatted : 
		for string in line:
			formatted_text.append(string) 
		
	return formatted_text