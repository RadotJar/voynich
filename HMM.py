# HMM Program
from pomegranate import *
import os
import numpy as np
import HMM_functions

training_index = os.getcwd() + "/HMM_training_texts/"
out_location = os.getcwd() + "/HMM_outputs"

################ change these where necessary

name = "test"  # name of the output file
VM = "./testa.txt" # text to analyse against

################

# puts output in text file
out_dir = out_location + "/" + name

# initialise counts, lengths, probabilities
longest_length_word, num_count, word_count = 0, 0, 0
string_count, num_transitions, word_transitions = 0, 0, 0
numbers = ['0','1','2','3','4','5','6','7','8','9']


directory = os.listdir(training_index)
text = HMM_functions.format_text(os.getcwd() + "/HMM_training_texts/" +directory[0])
classification, longest_length, list_of_lengths, num_count, word_count = HMM_functions.classify(text, numbers, num_count, word_count)
	
transition_matrix = np.zeros([2,2])
initial_prob = np.zeros([2])
conditional_matrix = np.zeros([2,longest_length])

transition_matrix, initial_prob, string_count, num_transitions, word_transitions = HMM_functions.initial_and_transition(classification, transition_matrix, initial_prob, string_count, num_transitions, word_transitions)
conditional_matrix = HMM_functions.find_conditional_prob(classification,conditional_matrix, list_of_lengths, longest_length, num_count, word_count)

for file in range(1,len(directory)) :

	text = HMM_functions.format_text(os.getcwd() + "/HMM_training_texts/" +directory[file])
	classification, longest_length, list_of_lengths, num_count, word_count = HMM_functions.classify(text, numbers, num_count, word_count)
	transition_matrix, initial_prob, string_count, num_transitions, word_transitions = HMM_functions.initial_and_transition(classification, transition_matrix, initial_prob, string_count, num_transitions, word_transitions)
	conditional_matrix = HMM_functions.find_conditional_prob(classification,conditional_matrix, list_of_lengths, longest_length, num_count, word_count)

	print(classification)
	print(conditional_matrix)

initial_prob, transition_matrix, conditional_matrix = HMM_functions.final_prob(initial_prob, transition_matrix, conditional_matrix, string_count, num_transitions, word_transitions, num_count, word_count)
results, vm_text = HMM_functions.make_model(VM, transition_matrix, conditional_matrix, initial_prob, list_of_lengths)

#print(results)

PN = HMM_functions.analyse_vm(results, vm_text)
print(PN)

HMM_functions.store_model(directory, out_dir, VM, initial_prob, transition_matrix, conditional_matrix, results, PN)