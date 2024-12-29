Question Answering System Based on BERT for Cancer Data
=======================================================

Overview
--------

This project focuses on developing a **Question Answering (QA) System** for cancer-related data using the **BERT (Bidirectional Encoder Representations from Transformers)** model. The system aims to bridge the knowledge gap regarding cancer symptoms, prevention measures, and treatment options, providing accurate answers to questions from the general public and medical practitioners.

* * * * *

Abstract
--------

A QA system is an information retrieval mechanism that delivers direct answers to queries instead of a list of references. By fine-tuning the pre-trained BERT model, this system provides straightforward, accurate answers. The application is particularly useful for identifying preliminary cancer symptoms, potentially saving lives through early diagnosis.

* * * * *

Features
--------

-   Covers five cancer types: **Breast Cancer**, **Prostate Cancer**, **Lung Cancer**, **Colorectal Cancer**, and **Skin Cancer**.
-   Uses **BERT-large**, fine-tuned with datasets like SQuAD for question-answering tasks.
-   Processes questions categorized by cancer type and context (e.g., Causes, Symptoms, Prevention, Treatment).
-   Evaluates performance using **BLEU** and **ROUGE** metrics.

* * * * *

Methodology
-----------

### Steps:

1.  **Information Extraction**:

    -   Data collected via web scraping from trusted sources like Mayo Clinic.
    -   Data stored in text files for preprocessing.
    -   Stop words retained to preserve context for bidirectional learning.
2.  **Topic Modeling**:

    -   Used **Latent Dirichlet Allocation (LDA)** to classify cancer data into topics.
    -   Topics organized by cancer types and their properties.
3.  **Question Preparation**:

    -   Manually crafted diverse questions for testing across all cancer types.
    -   Stored questions in JSON format, specifying the type of cancer and query property.
4.  **Implementing BERT QA System**:

    -   Leveraged Hugging Face's Transformers library.
    -   Fine-tuned **BERT-large** on datasets like SQuAD, NER, and MLNI.
    -   System tokenizes input queries and paragraphs for precise answer extraction.
5.  **Evaluation**:

    -   Applied **BLEU** and **ROUGE** metrics to measure precision, recall, and summarization accuracy.

* * * * *

Sample Workflow
---------------

### Input:

**Question**: What are less common symptoms of lung cancer?\
**Paragraph**: (Relevant text from extracted data)

### Output:

**Answer**: Swelling in the face or neck, Difficulty swallowing, Changes in the appearance of fingers (finger clubbing).

* * * * *

Tools and Technologies
----------------------

-   **Language Model**: BERT (Bidirectional Encoder Representations from Transformers)
-   **Libraries**:
    -   Hugging Face Transformers
    -   Python (NLTK, NumPy, Pandas)
-   **Data Sources**:
    -   Mayo Clinic
    -   Other trusted public health domains
-   **Evaluation**: BLEU and ROUGE scoring

* * * * *

Future Scope
------------

-   Expand to other diseases and multilingual datasets.
-   Incorporate contextual reasoning for more complex questions.
-   Deploy as a web application or integrate with mobile platforms.

* * * * *

References
----------

1.  *Infusing Disease Knowledge into BERT for Health Question Answering, Medical Inference and Disease Name Recognition* - Yun He et al., 2020.
2.  *BioBERT: A Pre-trained Biomedical Language Representation Model for Biomedical Text Mining* - Jinhyuk Lee et al., 2020.
3.  *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* - Jacob Devlin et al., 2019.

* * * * *

License
-------

This project is open-source and licensed under the MIT License. Feel free to use, modify, and distribute as per the license terms.
