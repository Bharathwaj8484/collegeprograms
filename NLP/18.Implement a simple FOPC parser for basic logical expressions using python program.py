import nltk

def fopc_parser(expression):
    tokens = nltk.word_tokenize(expression)
    tagged_tokens = nltk.pos_tag(tokens)
    for token, pos in tagged_tokens:
        if pos == 'NNS':
            print(f"Plural noun: {token}")
        elif pos == 'VBZ':
            print(f"Third person singular verb: {token}")
        elif pos == 'JJ':
            print(f"Adjective: {token}")
        elif pos == 'NN':
            print(f"Singular noun: {token}")

# Example usage:
logical_expression = "dogs bark"
fopc_parser(logical_expression)
