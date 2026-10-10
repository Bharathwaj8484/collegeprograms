import copy
def initialize_hypotheses(n):
    hypotheses = []
    specific_hypothesis = ['0'] * n
    general_hypothesis = ['?'] * n
    hypotheses.append(specific_hypothesis)
    hypotheses.append(general_hypothesis)
    return hypotheses
def candidate_elimination(training_data):
    num_attributes = len(training_data[0]) - 1
    hypotheses = initialize_hypotheses(num_attributes)
    for example in training_data:
        if example[-1] == 'Yes':  
            for i in range(num_attributes):
                if hypotheses[0][i] != '0' and hypotheses[0][i] != example[i]:
                    hypotheses[0][i] = '?'
                for h in hypotheses[1:]:
                    if h[i] != '?' and h[i] != example[i]:
                        hypotheses.remove(h)
        else:  
            temp_hypotheses = copy.deepcopy(hypotheses)
            for h in temp_hypotheses:
                if h[:-1] != example[:-1] + ['?']:
                    hypotheses.remove(h)
                for i in range(num_attributes):
                    if example[i] != h[i] and h[i] != '?':
                        new_hypothesis = copy.deepcopy(h)
                        new_hypothesis[i] = '?'
                        if new_hypothesis not in hypotheses:
                            hypotheses.append(new_hypothesis)

    return hypotheses
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Weak', 'Cool', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]
result_hypotheses = candidate_elimination(training_data)
print("Result Hypotheses:")
for h in result_hypotheses:
    print(h)
