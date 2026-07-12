# CodeAlpha_FAQ_Chatbot
# FAQ Chatbot using NLP 🤖

## Project Description

FAQ Chatbot is an AI-based chatbot that automatically answers frequently asked questions.

The chatbot uses Natural Language Processing (NLP) techniques to understand the user's question and finds the most similar question from the FAQ dataset to provide the correct answer.

This project was developed as part of the CodeAlpha Artificial Intelligence Internship.

---

## Problem Statement

Users often have common questions related to products and services. Answering the same questions repeatedly requires time and effort.

This project aims to build an intelligent chatbot that can automatically respond to user queries using NLP and Machine Learning techniques.

---

## Objectives

- Collect FAQ questions and answers.
- Process text data using NLP techniques.
- Compare user questions with stored FAQs.
- Find the best matching question.
- Display the appropriate answer.

---

## Technologies Used

### Backend
- Python

### Framework
- Flask

### NLP Libraries
- NLTK

### Machine Learning Library
- Scikit-learn

### Frontend
- HTML
- CSS
- JavaScript

---

## NLP Techniques Used

- Text preprocessing
- Lowercase conversion
- Removing punctuation
- Tokenization
- Stopword removal
- Lemmatization

---

## Machine Learning Technique

### TF-IDF Vectorization

TF-IDF converts text questions into numerical vectors so that they can be compared mathematically.

### Cosine Similarity

Cosine similarity is used to find the similarity between the user's question and stored FAQ questions.

The question with the highest similarity score is selected and its answer is displayed.

---

## Project Structure

```
FAQ_Chatbot/

│
├── app.py
│       Flask backend application
│
├── faqs.json
│       FAQ questions and answers dataset
│
├── templates/
│       └── index.html
│           Chatbot user interface
│
├── static/
│       ├── style.css
│       │       Chatbot styling
│       │
│       └── script.js
│               Frontend functionality
│
└── README.md
        Project documentation
```

---

## Working Process

1. User enters a question in the chatbot interface.

2. The question is preprocessed:
   - Converted into lowercase.
   - Punctuation is removed.
   - Words are tokenized.
   - Stopwords are removed.
   - Words are lemmatized.

3. The processed question is converted into a vector using TF-IDF.

4. Cosine similarity compares the user question with FAQ questions.

5. The chatbot returns the answer of the most similar FAQ.

---

## Features

- Interactive chatbot interface
- NLP-based question matching
- Automatic FAQ answering
- Fast response generation
- Easy FAQ dataset modification

---

## Dataset

The chatbot uses a JSON file (`faqs.json`) containing questions and answers.


---

## Installation

Install required libraries:

```
pip install flask nltk scikit-learn
```

---

## Running the Project

Run the Flask application:

```
python3 app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Sample Questions

You can ask:

- What is your return policy?
- How can I track my order?
- Do you provide free shipping?
- How can I contact customer support?

---

## Future Improvements

- Add voice input support
- Add multilingual chatbot support
- Use advanced deep learning models
- Deploy the chatbot online
- Connect with databases

---

## Author

Your Name

---

## Internship

CodeAlpha Artificial Intelligence Internship
