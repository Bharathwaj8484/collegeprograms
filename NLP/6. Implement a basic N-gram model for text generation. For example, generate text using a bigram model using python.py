import random

def generate_text(corpus, n):
    ngrams = zip(*[corpus[i:] for i in range(n)])
    print(ngrams)
    ngram_dict = {' '.join(ngram[:-1]): ngram[-1] for ngram in ngrams}

    current_word = random.choice(corpus)
    generated_text = [current_word]

    for _ in range(10):  # Generate 10 words
        next_word = ngram_dict.get(current_word, '')
        if next_word:
            generated_text.append(next_word)
            current_word = next_word
        else:
            break

    return ' '.join(generated_text)

corpus = "This is a simple example for a bigram text generation model".split()
generated_text = generate_text(corpus, 2)
print(generated_text)
