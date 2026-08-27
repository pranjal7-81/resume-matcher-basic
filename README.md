# Resume Matcher — Basic NLP Project

A **small beginner-level NLP project** built to understand the fundamentals of text preprocessing, TF-IDF, cosine similarity, PDF text extraction, and basic skill matching.

This project is primarily for **learning and experimentation**, not intended as a production-ready recruitment system or a major portfolio project.

## What I Learned

Through this project, I practiced:

* Text preprocessing
* Lowercasing and punctuation removal
* Tokenization
* Stopword removal
* TF-IDF vectorization
* Cosine similarity
* Basic keyword/skill matching
* Extracting text from PDF files
* Building a simple Streamlit application
* Managing Python dependencies with a virtual environment

## How It Works

```text
Resume PDF
    ↓
Extract Text
    ↓
Text Preprocessing
    ↓
TF-IDF
    ↓
Cosine Similarity
    ↓
Text Similarity Score

Resume + Job Description
    ↓
Basic Skill Matching
    ↓
Matched Skills
    ↓
Missing Skills
```

## Technologies Used

* Python
* Scikit-learn
* NLTK
* PyPDF
* Streamlit

## Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd resume-matcher
```

### 2. Create a virtual environment

```bash
python -m venv venv2
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv2\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Download NLTK stopwords

```bash
python -c "import nltk; nltk.download('stopwords')"
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

## Project Structure

```text
resume-matcher/
│
├── app.py
├── resume_matcher.ipynb
├── requirements.txt
├── README.md
├── .gitignore
└── venv2/
```

`venv2/` is excluded from Git using `.gitignore`.

## Limitations

This is intentionally a **very basic implementation**.

* Skill extraction uses a predefined list of keywords.
* It does not understand the semantic meaning of sentences.
* Synonyms and related skills may not be recognized.
* TF-IDF only captures word-level statistical similarity.
* Scanned PDFs may not provide extractable text.
* The scoring system is a simple baseline.
* It is not suitable for real-world recruitment decisions.

## Purpose

The main purpose of this project is to **learn the basic NLP pipeline by building something small from scratch**.

It serves as a starting point for understanding how text can be converted into numerical representations and compared using traditional NLP techniques.

## Possible Future Improvements

If this project is extended later, possible improvements include:

* Sentence embeddings for semantic similarity
* Better skill extraction using NLP techniques
* Skill normalization and synonym handling
* OCR support for scanned resumes
* DOCX support
* Better scoring methodology
* More advanced NLP/ML models

## Author

Pranjal
