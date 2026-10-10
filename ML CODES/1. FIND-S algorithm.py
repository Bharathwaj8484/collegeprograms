def find_s_algorithm(training_data):
    hypothesis = training_data[0][:-1] 

    for example in training_data:
        if example[-1] == 'Yes':  
            for i in range(len(hypothesis)):
                
                if example[i] != hypothesis[i]:
                    hypothesis[i] = '?'

    return hypothesis
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Weak', 'Cool', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]
result_hypothesis = find_s_algorithm(training_data)
print("Result Hypothesis:", result_hypothesis)
