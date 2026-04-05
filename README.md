                                                Hugging Face NLP Projects Collection

Overview

This repository contains multiple Natural Language Processing (NLP) projects implemented using Hugging Face datasets and transformers. Each project demonstrates a different NLP task such as Named Entity Recognition, Text Classification, Question Answering, Summarization, and Machine Translation.

All projects are implemented in Python and use real-world datasets from Hugging Face.


 Project Structure (Order Based on Execution Report)

1.IMDB NER Project

📄 File: `imdb_ner_project.py`

* **Dataset**: rubrix/imdb_spacy-ner

* **Task**: Named Entity Recognition (NER)

* **Model**: SpaCy (`en_core_web_sm`)

* **Description**:
  Extracts entities like PERSON, ORG, DATE, etc. from IMDB movie reviews.

* **Key Output**:

  * Input text
  * Extracted entities

---

2.Fake News Classification

📄 File: `fake_news_classification.py`

* **Dataset**: GonzaloA/fake_news

* **Task**: Text Classification

* **Model**: Default Hugging Face classifier (DistilBERT)

* **Description**:
  Classifies news articles as positive/negative (used here as fake/real approximation).

* **Key Output**:

  * News text
  * Predicted label
  * Actual label

---

3.Question Answering (SQuAD)

📄 File: `squad_qa_english.py`

* **Dataset**: rajpurkar/squad

* **Task**: Question Answering

* **Model**: distilbert-base-cased-distilled-squad

* **Description**:
  Answers questions based on given context paragraphs.

* **Key Output**:

  * Question
  * Context
  * Predicted Answer
  * Actual Answer

---

4.Text Summarization

📄 File: `cnn_summarization_project.py`

* **Dataset**: cestwc/cnn_dailymail-metaeval100

* **Task**: Summarization

* **Model**: facebook/bart-large-cnn

* **Description**:
  Generates concise summaries from long news articles.

* **Key Output**:

  * Original text
  * Generated summary
  * Reference summary

---

5.Machine Translation

📄 File: `translation_project.py`

* **Dataset**: yezhengli9/opus_books_demo

* **Task**: Language Translation (English → French)

* **Model**: Helsinki-NLP/opus-mt-en-fr

* **Description**:
  Translates English sentences into French using MarianMT.

* **Key Output**:

  * English sentence
  * Translated French sentence
  * Actual translation

---

Installation

Install required libraries:

```bash
pip install datasets transformers torch spacy sentencepiece
python -m spacy download en_core_web_sm
```

---

 How to Run

Run each project individually:

```bash
python imdb_ner_project.py
python fake_news_classification.py
python squad_qa_english.py
python cnn_summarization_project.py
python translation_project.py
```

---

 Results

All outputs and execution logs are documented in the project report:

📄 **Huggingface Dataset Task overall Results.pdf**


---

 Key Learnings

* Hands-on experience with Hugging Face datasets
* Understanding of multiple NLP tasks:

  * NER
  * Classification
  * QA
  * Summarization
  * Translation
* Model usage with pipelines
* Handling real-world datasets

---

 Conclusion

This project demonstrates the versatility of Hugging Face in solving diverse NLP problems using pre-trained transformer models. Each task highlights a different real-world application, making this repository a comprehensive NLP learning resource.

---

Author

Nagaraj S A

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
