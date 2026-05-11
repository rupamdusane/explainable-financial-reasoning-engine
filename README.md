# Explainable Financial Reasoning Engine

An early-stage explainable AI prototype that analyses financial and business text using concept-level reasoning instead of simple positive/negative sentiment classification.

The project extracts financial concepts from text, normalises them into meaningful concept groups, maps them to symbolic categories, detects concept interactions, and generates an interpretable reasoning path with a market signal.

---

## Why this project?

Traditional sentiment analysis systems often return only a label such as:

```text
Positive
Negative
Neutral
```

This is useful, but it does not explain **why** the model reached that conclusion.

Financial and business text is often more complex. A sentence can contain both positive and negative signals:

```text
The company reported strong profit growth but faces inflation risk and potential layoffs.
```

A basic sentiment model may struggle to explain this mixed context.

This project aims to go beyond basic sentiment classification by producing:

- extracted financial concepts
- concept categories
- polarity signals
- concept interactions
- reasoning paths
- market interpretation
- human-readable summary

---

## Project Objective

The goal is to build a lightweight explainable financial reasoning system that can analyse business or financial news text and provide structured, interpretable insights.

Instead of only answering:

```text
What is the sentiment?
```

the system attempts to answer:

```text
What are the key financial concepts?
How do they interact?
Why is the final sentiment bullish, bearish, or uncertain?
```

---

## Core Idea

The project follows a concept-level reasoning approach:

```text
Financial Text
    ↓
Raw Concept Extraction
    ↓
Concept Normalisation
    ↓
Concept Category Mapping
    ↓
Concept Polarity Mapping
    ↓
Interaction Detection
    ↓
Reasoning Path Generation
    ↓
Market Signal + Summary
```

---

## Example

### Input

```text
The company announced an acquisition and revenue growth, but market volatility and interest rate hikes created investor concern.
```

### Output

```text
NORMALIZED CONCEPTS:
['market concern', 'interest rate hike', 'market volatility', 'revenue growth', 'acquisition']

CONCEPT ANALYSIS:
- market concern: polarity=-0.5, category=market_psychology
- interest rate hike: polarity=-0.8, category=macroeconomic
- market volatility: polarity=-0.7, category=macroeconomic
- revenue growth: polarity=0.8, category=company_performance
- acquisition: polarity=0.5, category=corporate_action

INTERACTIONS:
- interest rate hike, market volatility:
  tightening monetary conditions may amplify market volatility

- acquisition, revenue growth:
  corporate expansion and revenue growth support positive business momentum

OVERALL:
Base Sentiment Score: -0.14
Interaction Score: -0.05
Final Sentiment Score: -0.19
Sentiment Label: mixed
Market Signal: uncertain

SUMMARY:
The text shows mixed sentiment. Positive signals such as revenue growth, acquisition are balanced against negative signals such as market concern, interest rate hike, market volatility. The reasoning layer highlights this tension through interactions such as corporate expansion and revenue growth support positive business momentum; tightening monetary conditions may amplify market volatility.
```

---

## Key Features

### 1. Concept Extraction

Uses NLP techniques to extract financial and business concepts from input text.

Examples:

```text
profit growth
inflation risk
interest rate hike
market volatility
investor confidence
regulatory pressure
```

---

### 2. Concept Normalisation

Normalises different phrase variations into consistent concepts.

Examples:

```text
interest rate hikes → interest rate hike
rising investor confidence → investor confidence
potential layoffs → layoff
investor concern → market concern
```

---

### 3. Symbolic Concept Categories

Each concept is mapped to a financial category.

Examples:

```text
profit growth → company_performance
inflation risk → macroeconomic
layoff → employment_risk
market concern → market_psychology
regulatory pressure → policy_risk
```

---

### 4. Concept Polarity Mapping

Each known concept is assigned a polarity score.

Examples:

```text
revenue growth → +0.8
investor confidence → +0.7
inflation risk → -0.7
interest rate hike → -0.8
layoff → -0.9
```

---

### 5. Interaction Detection

The engine identifies meaningful concept interactions.

Examples:

```text
profit growth + inflation risk
→ positive company performance is being challenged by inflation-related risk

interest rate hike + market volatility
→ tightening monetary conditions may amplify market volatility

earnings decline + layoff
→ weak earnings and workforce reduction indicate structural company weakness
```

---

### 6. Reasoning Path

The system generates a step-by-step explanation showing how the final interpretation was formed.

Example:

```text
- revenue growth is a positive signal linked to company performance.
- interest rate hike is a negative signal linked to macroeconomic conditions.
- market volatility is a negative signal linked to macroeconomic conditions.
- The combination of interest rate hike and market volatility suggests increased uncertainty.
```

---

## How this differs from basic sentiment analysis

| Basic Sentiment Analysis | This Project |
|---|---|
| Predicts positive/negative/neutral | Produces sentiment plus reasoning |
| Often black-box | Interpretable and structured |
| Works mostly at word/sentence level | Works at concept level |
| No interaction modelling | Detects concept interactions |
| Output is usually a label | Output includes concepts, reasoning path, and summary |

---

## Tech Stack

- Python
- spaCy
- pandas
- NumPy
- Pydantic
- FastAPI-ready project structure

Current version runs as a local Python prototype. FastAPI and UI layers can be added later.

---

## Project Structure

```text
explainable-financial-reasoning-engine/
│
├── app/
│   ├── api/
│   ├── knowledge/
│   │   ├── concept_categories.py
│   │   ├── concept_polarity.py
│   │   ├── explanation_templates.py
│   │   └── interaction_rules.py
│   │
│   ├── models/
│   │   ├── result_builder.py
│   │   └── schemas.py
│   │
│   ├── pipeline/
│   │   ├── concept_extractor.py
│   │   ├── concept_normalizer.py
│   │   ├── concept_classifier.py
│   │   ├── sentiment_mapper.py
│   │   ├── interaction_engine.py
│   │   ├── reasoning_engine.py
│   │   ├── summary_generator.py
│   │   └── orchestrator.py
│   │
│   └── utils/
│
├── data/
│   └── sample_inputs.json
│
├── tests/
├── run_demo.py
├── requirements.txt
└── README.md
```

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone <https://github.com/rupamdusane/explainable-financial-reasoning-engine.git>
cd explainable-financial-reasoning-engine
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

On Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Download spaCy English model

```bash
python -m spacy download en_core_web_sm
```

### 6. Run demo

```bash
python run_demo.py
```

---

## Current Demo Cases

The project currently tests multiple financial text scenarios:

1. Mixed company performance and inflation risk
2. Bullish revenue growth and investor confidence
3. Bearish earnings decline, debt, and layoffs
4. Mixed acquisition growth and macroeconomic risk
5. Macroeconomic pressure from inflation and interest rate hikes

These examples are stored in:

```text
data/sample_inputs.json
```

---

## Current Limitations

This is an early-stage prototype and has some limitations:

- Concept rules are manually defined
- Polarity scores are heuristic
- No transformer model is currently integrated
- No financial time-series prediction is included
- No large-scale evaluation has been performed yet
- Outputs depend on the quality of concept extraction and normalisation

The project intentionally avoids stock price prediction in the current version because financial markets are affected by many external factors beyond text sentiment alone.

---

## Future Improvements

Planned improvements include:

- Add FastAPI endpoint for external usage
- Add Streamlit or React-based user interface
- Integrate transformer-based financial sentiment models
- Add evaluation on financial news datasets
- Improve concept normalisation using embeddings
- Add confidence scoring for extracted concepts
- Expand symbolic knowledge base
- Add report generation for analysed financial text
- Compare symbolic reasoning output against standard sentiment classifiers

---

## Research Inspiration

This project is inspired by the broader direction of explainable AI, concept-level sentiment analysis, and neurosymbolic reasoning.

The aim is not only to classify financial text, but to make the reasoning process more transparent and interpretable.

---

## Status

Current status: **Working prototype**

Completed:

- Concept extraction
- Concept normalisation
- Polarity mapping
- Category mapping
- Interaction rules
- Reasoning path generation
- Summary generation
- Multi-example demo execution

Next step:

- API layer
- UI layer
- Evaluation and model integration

## Copyright

© 2026 Rupam Dusane. All rights reserved.

This project is shared for educational, portfolio, and research demonstration purposes.  
Please do not copy, redistribute, or reuse substantial parts of this project without permission.