# HMM Program
from mimetypes import init
from pomegranate import *
import os
import numpy as np
import argparse
import HMM_functions

def main():

	input = get_input()
	print(input)

	longest_length_word, num_count, word_count = 0

	# initialise counts, lengths, probabilities
	word_count, number_count, longest_length_word = 0
	numbers = ['0','1','2','3','4','5','6','7','8','9']

	start_prob_dir = input["model_path"] + "/start_prob.txt"
	transition_prob_dir = input["model_path"] + "/transition_prob.txt"
	emission_prob_dir = input["model_path"] + "/emission_prob.txt"

	# if train true, go to train directory and train on all texts, else just use model stored in current_model.txt
	directory = os.listdir(input["training_path"])

	for	file in directory :
		classified_text, list_of_lengths, longest_length_word, num_count, word_count = HMM_functions.classify(file)
		initial_prob, transition_prob, string_count, num_transitions, word_transitions = HMM_functions.initial_and_transition(classified_text, string_count, num_transitions, word_transitions)
		emission_prob = HMM_functions.find_conditional_prob(classified_text)

	initial_prob, transition_prob, emission_prob = HMM_functions.final_prob(initial_prob, transition_prob, emission_prob, string_count, num_transitions, word_transitions, num_count, word_count)
	HMM_functions.store_model(start_prob_dir, transition_prob_dir, emission_prob_dir, initial_prob, transition_prob, emission_prob)	
	observed_states = HMM_functions.make_model(initial_prob, transition_prob, emission_prob)
	HMM_functions.observe_vm(voynich, observed_states)

def get_input():
	parser = argparse.ArgumentParser(description="Hidden Markov Model Text Analyser.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("model_path", help="The path to the directory to save the HMM model in.")
	parser.add_argument("training_path", help="The path to the directory containing the training data.")
	args = parser.parse_args()
	input = vars(args)
	return input

if __name__ == "__main__":
	main()