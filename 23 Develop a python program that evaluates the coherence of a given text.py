def calculate_coherence(text):
    words = text.split()
    word_lengths = [len(word) for word in words]

    # Calculate average word length
    average_length = sum(word_lengths) / len(word_lengths)

    return average_length

# Example text
text = "This is a simple example text with some words of different lengths."

# Calculate coherence
coherence_score = calculate_coherence(text)

# Print result
print("Coherence Score:", coherence_score)
