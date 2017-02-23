""" CMSC471 01 hw2 spring 2017
    Dominic Rollo, xi02974

    Defines the problem class to solve dog cat problem.  Three possible values
    can be used for the path cost.  steps, scrabble letter values, and word
    frequencies.
"""    

import gzip
import aima.search as a       # AIMA module for search problems

dict_file = "words34.txt.gz"

dictionary = {}

for line in gzip.open(dict_file):
    word, n = line.strip().split('\t')
    dictionary[word] = float(n)

#list of letters with scrabble values
letters = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 
              'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 
              'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 
              'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


class DC(a.Problem):

    def __init__(self, initial='dog', goal='cat', cost='steps'):
        self.initial = initial
        self.goal = goal
        self.cost = cost

    def actions(self, state):
        """can change one of each indivdual letters as long as 
        it makes a legal word"""
        index = -1
        for let in state:
        	index += 1
        	for n in letters:
        		if n != let:
        			result = word_convert(state, index, n)
        			if legal_word(result):
        				yield result, n
		

    def result(self, state, action):
    	###outputs the result of the legal actions
        (result, n) = action
        return result

    def goal_test(self, state):
    	#tests to see if current state is the goal
        goal = self.goal
        test = state
        for a,b in zip(goal, test):
        	if a != b:
        		return False
        return True

    def path_cost(self, c, state1, action, state2):
    	#calculates cost based of steps, scrabble, values, or word path frequency
        if self.cost == 'steps':
        	return c + 1
        elif self.cost == 'scrabble':
        	(a, n) = action
        	return c + letters[n] 
        else:
        	return c + 1 + dictionary[state2]

    def __repr__(self):
        """ returns a string to represent a dc problem """
    	return self.state

    def h(self, node):
        """How many letter are different in the current state to the
        goal """
        result = 0
        for a,b in zip(node.state, self.goal):
        	if a != b:
        		result += 1
        return result

# add more functions here as needed

def word_convert(word, pos, let):
   	#changes one letter at one space in one word
   	word = word[:pos] + let + word[pos + 1:]
   	return word

def legal_word(word):
	#checks if word is legal
	if word in dictionary:
		return True
	else:
		return False