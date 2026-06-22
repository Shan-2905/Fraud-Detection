# Credit Card Fraud Detection using Machine Learning

## Overview

This project aims to detect fraudulent credit card transactions using Machine Learning techniques. The dataset contains anonymized transaction records, and the objective is to classify transactions as either legitimate or fraudulent.

The project includes data preprocessing, exploratory data analysis, fraud detection model development, evaluation metrics, visualizations, and an interactive Power BI dashboard for business insights.

---

## Project Objectives

* Analyze credit card transaction data.
* Clean and preprocess the dataset.
* Remove duplicate records.
* Build a fraud detection model using Machine Learning.
* Evaluate model performance.
* Generate meaningful visualizations.
* Develop an interactive Power BI dashboard.

---

## Dataset Information

The dataset contains credit card transactions with the following attributes:

* Time
* Amount
* V1 to V28 (anonymized features)
* Class

  * 0 = Normal Transaction
  * 1 = Fraudulent Transaction

### Dataset Summary

| Metric                    | Value   |
| ------------------------- | ------- |
| Original Records          | 284,807 |
| Duplicate Records Removed | 1,081   |
| Final Records             | 283,726 |
| Missing Values            | 0       |

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

### Visualization Tool

* Power BI

---

## Project Workflow

### 1. Data Collection

Loaded the credit card transaction dataset.

### 2. Data Exploration

* Displayed first and last records
* Examined dataset shape
* Checked column names
* Generated descriptive statistics

### 3. Data Cleaning

* Checked missing values
* Identified duplicate transactions
* Removed duplicate records

### 4. Exploratory Data Analysis (EDA)

Analyzed transaction patterns and fraud distribution.

### 5. Feature Engineering

Prepared features for model training.

### 6. Model Training

Trained a Machine Learning classification model to detect fraudulent transactions.

### 7. Model Evaluation

Evaluated model performance using:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

### 8. Dashboard Development

Created an interactive Power BI dashboard for fraud monitoring and business analysis.

---

## Machine Learning Results

### Model Accuracy

**99.95%**

### Classification Report

| Metric    | Fraud Class |
| --------- | ----------- |
| Precision | 97%         |
| Recall    | 73%         |
| F1 Score  | 83%         |

The model successfully identifies fraudulent transactions with high accuracy and strong classification performance.

---

## Visualizations

### Fraud Distribution

Displays the proportion of normal and fraudulent transactions.

**File:** `images/fraud_distribution.png`

### Amount Distribution

Shows how transaction amounts are distributed across the dataset.

**File:** `images/amount_distribution.png`

### Confusion Matrix

Visualizes actual versus predicted classifications.

**File:** `images/confusion_matrix.png`

### Correlation Heatmap

Displays relationships among transaction features.

**File:** `images/correlation_heatmap.png`

### Feature Importance

Highlights the most influential features used by the model.

**File:** `images/feature_importance.png`

---

## Power BI Dashboard

An interactive Power BI dashboard was developed to provide business insights and fraud monitoring capabilities.

### Dashboard Features

#### KPI Cards

* Total Transactions
* Normal Transactions
* Fraud Transactions
* Fraud Percentage

#### Visualizations

* Fraud vs Normal Transactions
* Transaction Distribution by Amount Range
* Fraud Distribution Analysis
* Transaction Trend Analysis
* Feature Importance Analysis
* Correlation Heatmap

#### Dashboard Preview

**File:** `images/dashboard.png`

The dashboard helps identify fraud patterns, transaction behavior, and key performance indicators through interactive visualizations.

---

## Project Structure

```text
Fraud-Detection/
│
├── dataset/
│   └── creditcard.csv
│
├── images/
│   ├── dashboard.png
│   ├── amount_distribution.png
│   ├── fraud_distribution.png
│   ├── confusion_matrix.png
│   ├── correlation_heatmap.png
│   └── feature_importance.png
│
├── powerbi/
│   └── Credit Card Fraud Detection.pbix
│
├── main.py
├── requirements.txt
└── README.md
```

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/Shan-2905/Fraud-Detection.git
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python main.py
```

---

## Business Impact

Credit card fraud causes significant financial losses worldwide. This project demonstrates how Machine Learning and Data Analytics can be used to identify suspicious transactions and support fraud prevention strategies.

---

## Future Enhancements

* Real-time fraud detection system
* Streamlit web application
* Automated fraud alert system
* Cloud deployment
* Advanced ensemble models

---

## Author

**Santhosh D**

Data Analytics & Machine Learning Intern
