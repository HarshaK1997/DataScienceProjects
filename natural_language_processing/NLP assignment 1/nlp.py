import re
import nltk
import math
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data if not already downloaded
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Step 1: Preprocess the text
def preprocess_text(text):
    """
    Converts text to lowercase, removes non-alphanumeric characters, tokenizes, removes stopwords, and lemmatizes.
    """
    text = text.lower()  # Convert to lowercase for consistency
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove punctuation and special characters
    sentences = sent_tokenize(text)  # Sentence tokenization
    tokens = [word_tokenize(sent) for sent in sentences]  # Word tokenization
    tokens = [word for sublist in tokens for word in sublist]  # Flatten list
    tokens = [t for t in tokens if t not in stopwords.words("english")]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]  # Lemmatization
    return tokens

# Step 2: Build the N-Gram Model
def build_ngram_model(tokens, n):
    """
    Builds an n-gram model using a dictionary with probabilities.
    """
    ngram_counts = Counter(ngrams(tokens, n))  # Count n-grams
    total_ngrams = sum(ngram_counts.values())  # Total count of n-grams
    return {ngram: count / total_ngrams for ngram, count in ngram_counts.items()}  # Compute probabilities

# Step 3: Calculate Perplexity
def calculate_perplexity(model, test_tokens, n):
    """
    Measures how well the n-gram model fits the test data.
    """
    test_ngrams = list(ngrams(test_tokens, n))
    N = len(test_ngrams)
    prob = 1
    for ngram in test_ngrams:
        prob *= model.get(ngram, 1e-6)  # Assign small probability for unseen n-grams
    return math.pow(prob, -1/N) if prob != 0 else float('inf')  # Compute perplexity

# Step 4: Predict Next Word
def predict_next_word(previous_words, model, n):
    """
    Predicts the next word based on previous (n-1) words.
    """
    previous_tuple = tuple(previous_words[-(n-1):])  # Get last (n-1) words
    candidates = {ngram[-1]: prob for ngram, prob in model.items() if ngram[:-1] == previous_tuple}
    return max(candidates, key=candidates.get) if candidates else "No prediction available"

# Step 5: Load and Process Corpus
file_path = "corpus.txt"
with open(file_path, "r", encoding="utf-8") as file:
    corpus = file.read()

processed_tokens = preprocess_text(corpus)

# Step 6: Build Unigram, Bigram, and Trigram Models
unigram_model = build_ngram_model(processed_tokens, 1)
bigram_model = build_ngram_model(processed_tokens, 2)
trigram_model = build_ngram_model(processed_tokens, 3)

# Example Prediction & Perplexity Calculation
previous_words = preprocess_text("The exclusion of women from trades is in most cases")

print("Bigram model next word prediction:", predict_next_word(previous_words, bigram_model, 2))
print("Trigram model next word prediction:", predict_next_word(previous_words, trigram_model, 3))

print("Unigram Perplexity:", calculate_perplexity(unigram_model, previous_words, 1))
print("Bigram Perplexity:", calculate_perplexity(bigram_model, previous_words, 2))
print("Trigram Perplexity:", calculate_perplexity(trigram_model, previous_words, 3))
