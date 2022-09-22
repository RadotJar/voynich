# HMM Program
from mimetypes import init
from pomegranate import *
import os
import numpy as np
import argparse
import HMM_functions

parser = argparse.ArgumentParser()

model_index = os.getcwd() + "/HMM_model"
training_index = os.getcwd() + "/training_texts"

# directory to the text to train on
# toot refers to "train only one text" and requests the directory
# ta refers to "train all" which goes to the training_texts folder and trains based on all of the text in that folder
parser.add_argument('--ta', type=bool, required=False)
parser.add_argument('--toot', type=str, required=False)

train_or_load = parse.parse_args()

training_index = os.getcwd() + "/training_texts/"
longest_length_word, num_count, word_count = 0

written_text = HMM_functions.format_text(file_location)
#voynich = HMM_functions.format_text(os.getcwd() + "/full_voynich.txt")

# collects model if option selected
start_prob_dir = file_location + "initial_prob/" + train_or_load
transition_dir = file_location + "transition_prob/" + train_or_load
emisssion_dir = file_location + "emission_prob/" + train_or_load

# initialise counts, lengths, probabilities
word_count, number_count, longest_length_word = 0
numbers = ['0','1','2','3','4','5','6','7','8','9']

# classify the text
classified_text, list_of_lengths, longest_length_word, number_count, word_count = HMM_functions.classify(written_text)

# if train true, go to train directory and train on all texts, else just use model stored in current_model.txt
if (train_or_load.ta == True) : 
	directory = os.listdir(training_index)

	for	file in directory :
		classified_text, list_of_lengths, longest_length_word, num_count, word_count = HMM_functions.classify(file)
		initial_prob, transition_prob, string_count, num_transitions, word_transitions = HMM_functions.initial_and_transition(classified_text, string_count, num_transitions, word_transitions)
		emission_prob = HMM_functions.find_conditional_prob(classified_text)

	initial_prob, transition_prob, emission_prob = HMM_functions.final_prob(initial_prob, transition_prob, emission_prob, string_count, num_transitions, word_transitions, num_count, word_count)
	HMM_functions.store_model(start_prob_dir, transition_dir, emisssion_dir, initial_prob, transition_prob, emission_prob)	
	observed_states = HMM_functions.make_model(initial_prob, transition_prob, emission_prob)
	HMM_functions.observe_vm(voynich, observed_states)

elif (train_or_load.ta == False) :
	initial_prob, transition_prob, emission_prob = HMM_functions.load_model(start_prob_dir, transition_dir, emisssion_dir)
	HiddenMM = HMM_functions.make_model(initial_prob, transition_prob, emission_prob) 
	HMM_functions.observe_vm(voynich, observed_states)

else :
	print("Invalid input")

# collect transition and emission matrices
# emission_matrix = HMM_functions.find_conditional_prob(classified_text, list_of_lengths, longest_length_word, number_count, word_count, bool: extra_state)
# transition_matrix = HMM_functions.calculate_transition(classified_text)
# initial_prob = HMM_functions.initial_probability(number_count, word_count)

# # make model
# HiddenMM = make_model(transition_matrix, emission_matrix)
# analyse(voynich, HiddenMM)