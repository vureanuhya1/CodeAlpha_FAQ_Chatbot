from flask import Flask, render_template, request, jsonify
import json
import string
import nltk

from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download tokenizer (only first time)
nltk.download('punkt')

app = Flask(__name__)

# -----------------------------
# Load FAQ data
# -----------------------------
with open("faqs.json", "r") as file:
    faqs = json.load(file)

# -----------------------------
# Text preprocessing function
# -----------------------------
def preprocess(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenize text
    tokens = word_tokenize(text)

    # Join tokens back into a sentence
    return " ".join(tokens)

# -----------------------------
# Prepare FAQ questions
# -----------------------------
questions = [preprocess(faq["question"]) for faq in faqs]

# Convert questions into vectors
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# Chat API
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():

    # Get message from frontend
    user_message = request.json["message"]

    # Clean the message
    cleaned_message = preprocess(user_message)

    # Convert into vector
    user_vector = vectorizer.transform([cleaned_message])

    # Calculate similarity
    similarity = cosine_similarity(user_vector, faq_vectors)

    # Get best matching FAQ
    best_match = similarity.argmax()

    # Highest similarity score
    score = similarity[0][best_match]

    # If similarity is low
    if score < 0.3:
        answer = "Sorry, I couldn't understand your question."

    else:
        answer = faqs[best_match]["answer"]

    return jsonify({
        "reply": answer
    })

# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
