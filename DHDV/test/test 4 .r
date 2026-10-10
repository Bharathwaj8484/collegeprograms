library(textTinyR)
library(wordcloud)

# Sample data
id <- c(1, 2, 3, 4, 5)
age <- c(29, 35, 43, 31, 47)
score <- c(4, 5, 3, 4, 5)

# Perform sentiment analysis
sentiment <- classify_emotion(as.character(score))
print(sentiment)

# Create a word cloud based on 'score'
wordcloud(words = as.character(score), main = "Word Cloud of Scores", scale = c(3, 0.5), colors = brewer.pal(8, "Dark2"))
