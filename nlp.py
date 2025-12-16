import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download only once, then comment out
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('vader_lexicon')

sentence = "Hello, are you feeling very sleepy & tired today?"
words = word_tokenize(sentence)
stop_words = set(stopwords.words('english'))

filtered_words = [w for w in words if w.lower() not in stop_words]

print("Original words:", words)
print("After Removing Stopwords:", filtered_words)

sia = SentimentIntensityAnalyzer()

sentences = [
    "START my wallet today",
    "This is the worst day of my life",
    "This movie is okay, not good but not bad",
    "I feel sleepy & tired"
]

for s in sentences:
    score = sia.polarity_scores(s)
    print("\nSentence:", s)
    print("Sentiment Score:", score)
