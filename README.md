# ⚖️ Risk-Aware Legal Document Simplification and Explainability System

An NLP and deep-learning based system for **analyzing, simplifying, classifying, and explaining legal documents at the clause level**.

Legal documents such as Terms of Service, privacy policies, and service agreements often contain lengthy sentences, technical terminology, obligations, financial conditions, liability clauses, and data-related provisions that are difficult for non-legal users to understand.

This project addresses that problem by converting an uploaded legal document into a structured, readable analysis where every identified clause can be examined through its:

* Original legal text
* Simplified explanation
* Predicted clause category
* BERT confidence
* Risk Probability Score (RPS)
* Risk level
* Reason for the assigned risk

The system also provides filtering, evaluation, and analytics features through an interactive Streamlit interface.

---

## 📌 Project Overview

The proposed system follows a **clause-level analysis approach** rather than treating the entire document as one piece of text.

A legal document is first converted into usable text. The text is cleaned and divided into individual clauses. Each clause is then passed through the processing pipeline for simplification, classification, risk assessment, and explanation.

The overall pipeline can be represented as:

```text
                Legal Document
                     │
             ┌───────┴────────┐
             │                │
           PDF              Text
             │                │
             └───────┬────────┘
                     │
              Text Extraction
                     │
              Text Cleaning
                     │
             Clause Segmentation
                     │
          ┌──────────┼───────────┐
          │          │           │
          ▼          ▼           ▼
    Simplification  BERT      Risk Analysis
          │       Classifier       │
          │          │             │
          │     Clause Type    RPS / Risk
          │     + Confidence      Level
          └──────────┼─────────────┘
                     │
               Explainability
                     │
                     ▼
             Interactive UI
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Analyze     Evaluation    Analytics
```

---

# 🎯 Problem Being Addressed

Legal agreements are important, but their language is generally optimized for legal precision rather than everyday readability.

Users may therefore:

* skip lengthy agreements,
* misunderstand contractual obligations,
* overlook financial conditions,
* fail to notice liability-related clauses,
* miss data and privacy implications, or
* accept terms without understanding their practical consequences.

A simple summarizer is not sufficient for this problem.

The system therefore attempts to answer four questions for each clause:

> **What does this clause say?**

> **What type of legal clause is it?**

> **How much attention should the user give it?**

> **Why has the system assigned that level of risk?**

---

# 💡 Proposed Solution

The project combines traditional NLP techniques with a transformer-based deep-learning model.

The major components are:

1. **Document Processing**
2. **Text Cleaning and Normalization**
3. **Clause Segmentation**
4. **Legal Text Simplification**
5. **BERT-based Clause Classification**
6. **Risk Probability Scoring**
7. **Risk Categorization**
8. **Clause-level Explanation**
9. **Interactive Filtering**
10. **Evaluation and Analytics**

Instead of presenting only a single document-level prediction, the system provides a detailed result for individual clauses.

---

# 🧠 BERT Integration

A major component of the project is the use of **BERT (Bidirectional Encoder Representations from Transformers)** for clause classification.

BERT is a transformer-based language model capable of understanding the contextual relationship between words in a sentence.

In this project, BERT is used to determine the semantic category of a legal clause.

The classifier can identify categories such as:

* Legal Liability
* User Obligation
* Data & Privacy
* Financial Terms
* Intellectual Property
* General Information

The model produces a probability distribution over the available classes. The class with the highest probability is selected as the predicted clause type.

The corresponding probability is also retained as the model's confidence for that prediction.

This makes the BERT component different from the rule-based risk system: **BERT determines what the clause is about, while the risk layer determines how much attention the clause may require.**

---

# 📊 Risk Probability Score (RPS)

The project uses a **Risk Probability Score (RPS)** to represent the potential importance of an individual clause.

RPS is not intended to represent a legal judgment. It is an analytical score designed to help users identify clauses that deserve closer attention.

The risk assessment considers signals such as:

* clause category,
* risk-related language,
* user obligations,
* financial conditions,
* liability-related content,
* privacy/data-related conditions,
* intellectual-property provisions, and
* textual complexity.

The resulting score is mapped to interpretable levels:

```text
Very Low
Low
Medium
High
Very High
```

This allows users to quickly scan a long agreement and focus on clauses that may require greater attention.

---

# 📝 Legal Text Simplification

Legal language can contain terminology and sentence structures that are difficult for general users.

The simplification component attempts to make the clause easier to understand while retaining its original intent.

For example:

```text
Original:
If you pre-order Content, you will be charged when the
Content is delivered to you unless you cancel prior to
the Content's availability.

Simplified:
If you pre-order content, you will be charged when it is
delivered unless you cancel before it becomes available.
```

The purpose of simplification is **not to rewrite the legal agreement** or provide legal advice.

It is intended to provide an easier-to-read interpretation alongside the original clause.

---

# 🔍 Explainability

Simply displaying:

```text
Risk: High
```

does not tell the user why the system reached that result.

Therefore, the system includes a **"Why this risk?"** section.

The explanation is connected to the actual content and detected characteristics of the clause.

Examples of explanations include:

* User is required to follow specified conditions
* Clause includes payment or financial obligations
* Clause defines ownership or intellectual-property rights
* Clause concerns collection or use of personal information
* Clause defines potential liability or responsibility

This makes the output more interpretable than a classification label alone.

---

# 📄 Input Formats

The application supports two input modes:

### 1. Text

Users can directly enter legal text into the application.

### 2. PDF

Users can upload a legal PDF.

The application extracts the text from the uploaded document and processes it through the same analysis pipeline.

The interface also provides feedback during PDF processing so that the user can see when the document is being uploaded and processed.

---

# 🖥️ Application Interface

The application is built using **Streamlit**.

The interface contains:

### Settings Panel

Users can configure:

* Input type
* Risk filters
* Clause-type filters

### Analyze

The Analyze section presents clause-level results including:

* Original clause
* Risk
* Simplified explanation
* BERT confidence
* RPS
* Clause type
* Reason for risk

### Evaluation

The Evaluation section provides document-level and clause-level analysis, including:

* Total number of clauses
* Number of high-risk clauses
* Average RPS
* Detailed clause table

### Analytics

The analytics component provides an overview of the processed document and its risk distribution.

---

# 🔎 Filtering

The application allows users to filter results according to:

### Risk

* Very High
* High
* Medium
* Low
* Very Low

### Clause Type

* Legal Liability
* User Obligation
* Data & Privacy
* Financial Terms
* Intellectual Property
* General Information

This is useful when a user is interested in only one particular aspect of an agreement.

For example, selecting **Data & Privacy** allows the user to focus on clauses related to data handling instead of manually searching the entire agreement.

If the selected filter does not match any analyzed clause, the system is designed to indicate that no matching clause was found rather than displaying unrelated clauses.

---

# 📈 Evaluation

The project separates the concepts of **model confidence** and **risk score**.

### BERT Confidence

Represents how strongly the BERT classifier favors the predicted clause category.

### RPS

Represents the risk-oriented score assigned by the risk-analysis component.

These two values serve different purposes and should not be interpreted as the same metric.

For proper model evaluation, the classification component can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

For a multi-class legal clause classifier, the **F1-score**, particularly macro-F1, is useful because it considers performance across individual classes instead of relying only on overall accuracy.

Actual evaluation values should be reported only after running the model against a labelled test set.

---

# 🏗️ Project Architecture

The project is organized into separate modules so that document processing, prediction, risk assessment, simplification, and visualization can be maintained independently.

A typical development structure is:

```text
RAELS-Net/
│
├── data/
│   └── labeled.csv
│
├── models/
│   ├── risk_bert/
│   ├── risk_classifier/
│   ├── risk_model.pkl
│   └── vectorizer.pkl
│
├── src/
│   ├── bert_predictor.py
│   ├── evaluation.py
│   ├── explainability.py
│   ├── pipeline.py
│   ├── preservation.py
│   ├── risk_model.py
│   ├── segmenter.py
│   ├── simplifier.py
│   └── visualization.py
│
├── app.py
├── run.py
├── train_bert.py
├── labeled.csv
├── requirements.txt
└── README.md
```

---

# 📂 Important Files

| File                | Purpose                                                     |
| ------------------- | ----------------------------------------------------------- |
| `app.py`            | Main Streamlit application and user interface               |
| `train_bert.py`     | Training pipeline for the BERT-based classifier             |
| `run.py`            | Application execution entry point                           |
| `bert_predictor.py` | Loads the trained BERT model and performs clause prediction |
| `evaluation.py`     | Evaluation-related functionality                            |
| `explainability.py` | Generates interpretable reasons for model/risk outputs      |
| `pipeline.py`       | Connects different processing stages                        |
| `preservation.py`   | Helps preserve important text information during processing |
| `segmenter.py`      | Divides legal text into clauses                             |
| `simplifier.py`     | Performs legal text simplification                          |
| `risk_model.py`     | Risk scoring and risk-level calculation                     |
| `visualization.py`  | Visualization and analytics functionality                   |
| `labeled.csv`       | Labelled data used by the classification pipeline           |
| `requirements.txt`  | Python dependencies                                         |

---

# 🛠️ Technologies Used

## Python

The primary programming language used to implement the complete processing pipeline.

Used for:

* NLP processing
* machine learning
* deep learning
* document processing
* data manipulation
* application logic

---

## BERT / Transformers

Used for contextual representation and clause classification.

BERT helps the system understand the relationship between words based on their surrounding context instead of treating each word independently.

---

## PyTorch

Used as the deep-learning framework supporting the BERT model and inference process.

---

## Hugging Face Transformers

Used to load and work with:

* BERT tokenizer
* BERT sequence classification model
* pretrained/model-specific transformer components

---

## Scikit-learn

Used for machine-learning utilities and evaluation functionality.

It can support:

* preprocessing
* label encoding
* traditional classification components
* evaluation metrics

---

## TextBlob / NLP Utilities

Used where applicable for natural-language processing and text handling.

---

## Streamlit

Used to create the interactive web application.

It provides the interface for:

* PDF uploading
* text input
* filtering
* analysis
* evaluation
* analytics
* result visualization

---

## PDF Processing

PDF extraction functionality is used to convert uploaded legal documents into text before clause-level processing.

---

# 🔄 End-to-End Workflow

The complete processing flow is:

```text
1. User uploads PDF or enters text
                 ↓
2. Text extraction
                 ↓
3. Cleaning and normalization
                 ↓
4. Clause segmentation
                 ↓
5. Clause preservation / correction
                 ↓
6. Text simplification
                 ↓
7. BERT classification
                 ↓
8. Confidence calculation
                 ↓
9. Risk analysis
                 ↓
10. RPS calculation
                 ↓
11. Risk-level assignment
                 ↓
12. Explanation generation
                 ↓
13. Filtering and visualization
                 ↓
14. Analyze / Evaluation / Analytics
```

---

# 🧪 Dataset

The project uses labelled legal-clause data for training/evaluating the classification component and real-world Terms of Service documents for document-level analysis.

The legal documents used during development include agreements such as Terms of Service from major digital service providers.

The dataset should be described in the research paper using the **actual number of samples, classes, training examples, validation examples, and test examples obtained from the final experiment**.

No fabricated performance values are included in this README.

---

# 🚀 Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Risk-Aware-Legal-Document-Simplification-Explainability-System
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

or, if the project entry point is configured through `run.py`:

```bash
python run.py
```

The application will open in the browser.

---

# 🤖 Training the BERT Model

The BERT training script is provided separately:

```bash
python train_bert.py
```

The trained model is then stored in the project's model directory and loaded by the prediction component during inference.

The exact training configuration should be kept consistent with the final experiment used for reporting evaluation results.

---

# 📌 Example Output

For each clause, the application presents information similar to:

```text
Original:
If you pre-order Content, you will be charged when the
Content is delivered to you...

Risk:
Very Low

Explanation:
This clause means that if you pre-order content, you will
be charged when the content is delivered...

Confidence (BERT):
0.50

RPS:
0.08

Type of Clause:
General Information

Why this risk:
• Clause contains a specified contractual condition
```

The actual values depend on the document and model prediction.

---

# 🌟 Key Features

* 📄 PDF document processing
* 📝 Direct text input
* ✂️ Clause-level segmentation
* 🧹 Text cleaning and normalization
* 🔤 Legal text simplification
* 🧠 BERT-based clause classification
* 🎯 BERT confidence estimation
* ⚠️ Risk Probability Score
* 🚦 Five-level risk categorization
* 🔍 Clause-level explanations
* 🎛️ Risk filtering
* 🏷️ Clause-type filtering
* 📊 Evaluation table
* 📈 Analytics
* 🖥️ Interactive Streamlit interface
* 🔎 Original-versus-interpreted clause view

---

# ⚠️ Important Limitation

This system is an **analytical and educational tool**, not a replacement for a qualified legal professional.

The risk level generated by the system should be interpreted as an indication of which clauses may deserve closer attention. It should not be treated as a legal opinion, legal advice, or a definitive assessment of contractual enforceability.

Similarly, the simplified explanation is intended to improve readability and should not be considered a substitute for the original legal wording.

---

# 🔮 Future Improvements

Several extensions can further improve the system:

### 1. Legal-domain Transformer

A model specifically trained on legal corpora, such as Legal-BERT or another legal-domain transformer, could improve classification performance.

### 2. Larger Annotated Dataset

Increasing the number and diversity of labelled clauses would help the classifier generalize across different types of legal agreements.

### 3. Neural Text Simplification

A domain-specific neural simplification model could be explored alongside the current controlled simplification approach.

### 4. Better Risk Calibration

The RPS could be calibrated against human annotations from legal experts rather than relying primarily on engineered risk signals.

### 5. Multilingual Support

The system could be extended to support legal documents written in multiple languages.

### 6. Human-in-the-Loop Evaluation

Future versions could allow legal professionals to review and correct classifications and risk assessments, creating feedback for subsequent model improvement.

---

# 📚 Research Contribution

The main contribution of this project is the integration of several components into a single clause-level legal document analysis workflow.

Rather than producing only a summary or a classification label, the system combines:

```text
Legal Document
      ↓
Clause Identification
      ↓
Simplification
      ↓
Semantic Classification
      ↓
Risk Assessment
      ↓
Explanation
      ↓
Interactive Interpretation
```

This makes the system useful not only for identifying what a clause represents, but also for helping a non-expert user understand why a particular clause may deserve attention.

---

# 👩‍💻 Author

**Vaishnavi Shivhare**

B.Tech — Artificial Intelligence and Data Science
Madhav Institute of Technology and Science (MITS), Gwalior, India

---

# 📜 License

This project is developed for academic and research purposes.

Please add an appropriate open-source license if the repository is intended for public reuse.

---

## ⭐ Acknowledgement

This project was developed as an academic/research-oriented implementation exploring the application of Natural Language Processing, transformer-based deep learning, explainability, and risk-aware analysis to legal documents.
