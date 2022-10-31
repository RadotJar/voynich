from pomegranate import *

num_dist = {'1':0.35, '2':0.65}
word_dist = {'1':0.73, '2':0.27}

d1 = DiscreteDistribution(num_dist)
d2 = DiscreteDistribution(word_dist)

state1_n = State(d1, name="Number")
state2_w = State(d2, name="Word")

model = HiddenMarkovModel('Model')
model.add_states([state1_n, state2_w])
model.add_transition(model.start, state1_n, 0.4)
model.add_transition(model.start, state2_w, 0.6)

model.add_transition(state1_n, state1_n, 0.3)
model.add_transition(state1_n, state2_w, 0.7)
model.add_transition(state2_w, state1_n, 0.55)
model.add_transition(state2_w, state2_w, 0.45)
	
model.bake()

result_states_string = (", ".join(state.name for i, state in model.viterbi(['1','2','2'])[1]))
result_states = result_states_string.split(", ")
result_states.pop(0)

print(result_states)