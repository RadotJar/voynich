import HMM_functions
import numpy as np
import os
from pomegranate import *
import argparse

#dir = os.getcwd()+'/HMM_model/model.txt'
dir = os.getcwd()+'/texts/The-Medicinal-Plants-of-the-Philippines.txt'
VM = os.getcwd() + '/texts/voynich-manuscript.txt_formatted.txt'

#test read
file = open(dir, 'r')
text = file.readlines()
file.close()
formatted_l = []

file = open(dir, 'r')
text = file.readlines()
file.close()

########################################## test all
numbers = ['0','1','2','3','4','5','6','7','8','9']
string_count, num_transitions, word_transitions = 0, 0, 0
num_count, word_count = 0,0
text = HMM_functions.format_text(dir)
#print(text)
classification, longest_length, list_of_lengths, num_count, word_count = HMM_functions.classify(text, numbers, num_count, word_count)
#print(classification, longest_length, list_of_lengths, num_count, word_count)
#print(list_of_lengths)

transition_matrix = np.zeros([2,2])
initial_prob = np.zeros([2])
conditional_matrix = np.zeros([2,longest_length])

transition_matrix, initial_prob, string_count, num_transitions, word_transitions = HMM_functions.initial_and_transition(classification, transition_matrix, initial_prob, string_count, num_transitions, word_transitions)
conditional_matrix = HMM_functions.find_conditional_prob(classification,conditional_matrix, list_of_lengths, longest_length, num_count, word_count)


classification, longest_length, list_of_lengths, num_count, word_count = HMM_functions.classify(text, numbers, num_count, word_count)
transition_matrix, initial_prob, string_count, num_transitions, word_transitions = HMM_functions.initial_and_transition(classification, transition_matrix, initial_prob, string_count, num_transitions, word_transitions)
#print(transition_matrix, initial_prob, string_count, num_transitions, word_transitions)
conditional_matrix = HMM_functions.find_conditional_prob(classification,conditional_matrix, list_of_lengths, longest_length, num_count, word_count)

#print(conditional_matrix)

#print(conditional_matrix, num_count, word_count)

initial_prob, transition_matrix, conditional_matrix = HMM_functions.final_prob(initial_prob, transition_matrix, conditional_matrix, string_count, num_transitions, word_transitions, num_count, word_count)
#print(initial_prob)
#print(transition_matrix) 
#print(conditional_matrix)


results, vm_text = HMM_functions.make_model(VM, transition_matrix, conditional_matrix, initial_prob, list_of_lengths)
#print("restults: ")
print(results)
PN = HMM_functions.analyse_vm(results, vm_text)
print(PN)

formatted = []
file = open(dir, 'r')
text = file.readlines()
file.close()

for line_no in range(len(text)):
	formatted.append(text[line_no].replace("\n",""))
	formatted[line_no] = formatted[line_no].split(" ")
#print(formatted)

d1 = DiscreteDistribution({'1' : 0.35, '2' : 0.20, '3' : 0.45})
d2 = DiscreteDistribution({'1' : 0.25, '2' : 0.25, '3' : 0.5})
d3 = DiscreteDistribution({'1' : 0.25, '2' : 0.25, '3' : 0.5})

s1 = State(d1, name="s1")
s2 = State(d2, name="s2")
s3 = State(d3, name="s3")

emission =  np.array([d1,d2, d3])
trans_mat = np.array([[0.7, 0.3, 0.0],
                             [0.1, 0.7, 0.2],
                             [0.3, 0.3, 0.4]])
starts = np.array([0.4, 0.4, 0.2])

model = HiddenMarkovModel.from_matrix(trans_mat, emission, starts)
#print(model)
#dists = [NormalDistribution(5, 1), NormalDistribution(1, 7), NormalDistribution(8,2)]
#print("model: ", model)

######### convert int to char list for sequence of sizes
xs = ['1', '2', '3', '2']
xp = [1, 2, 3]
y = list(map(chr, xp))

#print(y)

### Test make model another way
# d1 = DiscreteDistribution({'1' : 0.35, '2' : 0.20, '3' : 0.45})
# d2 = DiscreteDistribution({'1' : 0.25, '2' : 0.25, '3' : 0.5})
#d3 = DiscreteDistribution({'1' : 0.25, '2' : 0.25, '3' : 0.5})
x = [0.35, 0.65, 0.73, 0.27]
y = ['1', '2']

dict1 = {}
dict1.update({y[0]: x[0]})
#print(dict1)

################ test model
d1 = DiscreteDistribution({'1' : 0.35, '2' : 0.65})
d2 = DiscreteDistribution({'1' : 0.73, '2' : 0.27})

s1 = State(d1, name="Num")
s2 = State(d2, name="Word")
#s3 = State(d3, name="Whatever")

trans_mat = np.array([[0.3, 0.0],
                             [0.7, 0.2],
                             [0.3, 0.4]])

#print((trans_mat).shape)

model = HiddenMarkovModel()
model.add_states([s1, s2])
model.add_transition(model.start, s1, 0.4)
model.add_transition(model.start, s2, 0.6)
#model.add_transition(model.start, s3, 0.35)

model.add_transition(s1, s1, 0.30)
model.add_transition(s1, s2, 0.70)
#model.add_transition(s1, s3, 0.30)

model.add_transition(s2, s1, 0.55)
model.add_transition(s2, s2, 0.45)
#model.add_transition(s2, s3, 0.20)

# model.add_transition(s3, s1, 0.70)
# model.add_transition(s3, s2, 0.10)
# model.add_transition(s3, s3, 0.20)
model.bake()
#print(list('12'))
xy = (", ".join(state.name for i, state in model.viterbi(list('122'))[1]))

states = xy.split(", ")
states.pop(0)
#print(states)

#print(", ".join(state.name for i, state in model.viterbi(list('122'))[1]))

# sequence = xs
# pred = model.predict(sequence, algorithm='viterbi')
# print("pred: ", pred)

x_dict = {}
#x_dict.update({emission[i]: emission[i]})
x = DiscreteDistribution()
#print("x: ", x)

y_dict = {}
y = DiscreteDistribution()
#print("y: ", y)

num_state = State(x, name="Number")
word_state = State(y, name="Word")

# formatted_l.append(text[0].replace("\n",""))
# formatted_l[0] = formatted_l[0].split(" ")

# print(formatted_l)

for line_no in range(len(text)):
    formatted_l.append(text[line_no].replace("\n",""))
    formatted_l[line_no] = formatted_l[line_no].split(" ")

#print("hi:", '\n')
#print(formatted_l)

input_text = []
numbers = ['0','1','2','3','4','5','6','7','8','9']

# for line_no in range(len(text)):
# 	input_text= input_text + (text[line_no].split())
# 	input_text[line_no] = input_text[line_no].replace("\n","")

#print(input_text)

# print(text)
# print(formatted_l)

#classification, longest_length, list_of_lengths, num_count, word_count = HMM_functions.classify(formatted_l, numbers)
#print("Classification:", classification)

#tr = HMM_functions.initial_and_transition(classification)
#cl = HMM_functions.initial_and_transition(classification)
#print(tr)

# cond = HMM_functions.find_conditional_prob(classification, list_of_lengths, longest_length, num_count, word_count)
# print(cond)

test=np.matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
test2=np.matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])


# with open(dir,'wb') as f:
#     for line in test:
#         np.savetxt(f, line)


#reads matric from txt file to allow loading currently trained model

# with open(dir, 'r') as f:
#     model_in = np.array([[float(num) for num in line.split(' ')] for line in f])

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


def load_model(start_prob_start_prob_dir, transition_dir, emisssion_dir):

    with open(start_prob_start_prob_dir, 'r') as sp:
        start_prob = np.array([[float(num) for num in line.split(' ')] for line in sp])

    with open(transition_dir, 'r') as t:
        transition_prob = np.array([[float(num) for num in line.split(' ')] for line in t])

    with open(emisssion_dir, 'r') as e:
        emission_prob = np.array([[float(num) for num in line.split(' ')] for line in e])

    return start_prob, transition_prob, emission_prob