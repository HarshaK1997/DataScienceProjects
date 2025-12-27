# Step 3: Import necessary libraries
import wikipediaapi
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import heapq
from gensim.summarization import summarize
from transformers import pipeline

import nltk
nltk.download("punkt")
nltk.download("stopwords")

def get_wikipedia_page(topic):
    # Step 4: Get text from Wikipedia
    # Initialize Wikipedia API with user agent and language
    wiki = wikipediaapi.Wikipedia(user_agent='NLP_Assignment2_harshak', language='en')
    # Get the Wikipedia page for the given topic
    page = wiki.page(topic)
    if not page.exists():
        print("Wikipedia page not found.")
        return None
    print("\n===== Wikipedia extracted results for given topic =====")
    print("Topic selected: %s" % topic)
    print("Wikipedia page title: %s" % page.title)
    print("Wikipedia URL: %s" % page.fullurl)
    return page

def summarize_with_wikipediaapi(page):
    # Return the summary of the Wikipedia page
    return page.summary

def summarize_manually(text):
    # Manually created summary of the Elephanta Caves
    summary = (
        "The Elephanta Caves are a network of sculpted caves located on Elephanta Island in Mumbai Harbour, "
        "approximately 10 kilometers east of Mumbai, India. These caves are renowned for their rock-cut sculptures "
        "depicting Hindu deities, primarily dedicated to Lord Shiva. The island, originally known as Gharapuri, was "
        "renamed 'Elephanta' by Portuguese explorers in the 16th century due to a large stone elephant statue they found there.\n"
        "Key Features of the Elephanta Caves:\n"
        "1. Main Cave (Cave 1): This is the most significant cave, featuring a large hall with numerous sculptures, "
        "including the famous 7-meter-high Trimurti, a three-headed depiction of Shiva symbolizing his roles as creator, "
        "preserver, and destroyer.\n"
        "2. Other Caves: There are several smaller caves on the island, some of which are incomplete or have deteriorated over time.\n"
        "Historical Significance:\n"
        "The exact origins of the caves are uncertain, but they are believed to have been constructed between the 5th and 8th centuries AD. "
        "The intricate carvings reflect the artistry and religious traditions of the time, providing insight into the cultural history of the region.\n"
        "Preservation Efforts:\n"
        "The caves have faced challenges over the centuries, including damage from natural elements and human activity. Recognizing their cultural importance, "
        "UNESCO designated the Elephanta Caves as a World Heritage Site in 1987, leading to increased conservation efforts to preserve this historical landmark."
    )
    return summary

def preprocess_text(text):
    # Step 5: Preprocessing
    # Remove references like [1], [2] and normalize whitespace
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def summarize_with_nltk(text, num_sentences=5):
    # Step 6: Tokenize sentences
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))

    # Step 7: Create frequency table
    # Create a frequency table of words excluding stop words
    freq_table = {word: words.count(word) for word in words if word not in stop_words}

    # Step 8: Calculate value of each sentence based on step 5
    # Score sentences based on word frequencies
    sentence_scores = {sentence: sum(freq_table.get(word, 0) for word in word_tokenize(sentence.lower())) for sentence in sentences}

    # Step 9: Pick sentences based on step 6 and add to generate summary
    # Select the top num_sentences with the highest scores
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

def summarize_with_gensim(text, ratio=0.2):
    # Summarize the text using the GenSim library. Ratio can be between 0 and 1, with 0 being no summary and 1 being the full text.
    # If ratio is 0.2, the summary will contain 20% of the original text.
    return summarize(text, ratio)

def summarize_with_llm(text, chunk_size=1500, max_length=300, min_length=100):
    # Initialize the summarization pipeline with the Meta's BART model
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    # Split the text into chunks and summarize each chunk
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = [summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
                 for chunk in chunks]
    # Combine the chunk summaries into a final summary
    return " ".join(summaries)

def main():
    # Prompt the user to enter a Wikipedia topic
    topic = input("Enter Wikipedia topic: ")
    # Retrieve the Wikipedia page for the given topic
    page = get_wikipedia_page(topic)
    if not page:
        return

    # Print the summary of the Wikipedia page using Wikipedia API
    print("\n===== Wikipedia Summary =====")
    print(summarize_with_wikipediaapi(page))

    # Print the manually created summary
    print("\n===== Manual Summary =====")
    print(summarize_manually(page))

    # Preprocess the text from the Wikipedia page
    text = preprocess_text(page.text)

    # Print the summary of the text using NLTK
    print("\n===== NLTK Summary =====")
    print(summarize_with_nltk(text, num_sentences=10))

    # Print the summary of the text using GenSim
    print("\n===== GenSim Summary =====")
    print(summarize_with_gensim(text, ratio=0.1))

    # Print the summary of the text using a large language model (LLM)
    print("\n===== LLM Summary =====")
    print(summarize_with_llm(text, chunk_size=1200, max_length=100, min_length=50))

if __name__ == "__main__":
    main()
