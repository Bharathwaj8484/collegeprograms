import numpy as np
def candidate_elimination(examples):
    specific_hypothesis = examples[0][:-1].copy()
    general_hypothesis = [['?' for _ in range(len(specific_hypothesis))] for _ in range(len(specific_hypothesis))]
 
    for example in examples:
        if example[-1] == 'Yes':  
            for i in range(len(specific_hypothesis)):
                if example[i] != specific_hypothesis[i]:
                    specific_hypothesis[i] = '?'
                    general_hypothesis[i][i] = '?'
        elif example[-1] == 'No':  
            for i in range(len(specific_hypothesis)):
                if example[i] != specific_hypothesis[i]:
                    general_hypothesis[i][i] = specific_hypothesis[i]
                else:
                    general_hypothesis[i][i] = '?'
    
    return specific_hypothesis, general_hypothesis
examples = [
    ['Small', 'Red', 'Circle', 'No'],
    ['Small', 'Red', 'Triangle', 'No'],
    ['Big', 'Red', 'Circle', 'Yes'],
    ['Small', 'Blue', 'Circle', 'No'],
    ['Big', 'Blue', 'Circle', 'Yes'],
]
specific, general = candidate_elimination(examples)
print("Specific Hypothesis:", specific)
print("General Hypothesis:", general)
