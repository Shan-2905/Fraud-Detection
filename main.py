import os
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ============================================================
# CREATE IMAGES FOLDER
# ============================================================

os.makedirs("images", exist_ok=True)

# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv("dataset/cleaned_creditcard.csv")

# ============================================================
# FIRST 5 ROWS
# ============================================================

print("=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)
print(df.head())

# ============================================================
# LAST 5 ROWS
# ============================================================

print("\n" + "=" * 60)
print("LAST 5 ROWS")
print("=" * 60)
print(df.tail())

# ============================================================
# SHAPE
# ============================================================

print("\n" + "=" * 60)
print("DATASET SHAPE")
print("=" * 60)
print(df.shape)

# ============================================================
# COLUMN NAMES
# ============================================================

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)
print(df.columns)

# ============================================================
# INFO
# ============================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)
print(df.info())

# ============================================================
# MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)
print(df.isnull().sum())

# ============================================================
# DUPLICATES
# ============================================================

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)
print(df.duplicated().sum())

# ============================================================
# REMOVE DUPLICATES
# ============================================================

df = df.drop_duplicates()

print("\n" + "=" * 60)
print("DATASET SHAPE AFTER CLEANING")
print("=" * 60)
print(df.shape)

print("\n" + "=" * 60)
print("DUPLICATES AFTER CLEANING")
print("=" * 60)
print(df.duplicated().sum())

# ============================================================
# DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)
print(df.describe())

# ============================================================
# FRAUD DISTRIBUTION
# ============================================================

plt.figure(figsize=(6, 5))

sns.countplot(
    x=df["Class"]
)

plt.title("Fraud vs Normal Transactions")

plt.savefig(
    "images/fraud_distribution.png",
    bbox_inches="tight"
)

plt.close()

# ============================================================
# AMOUNT DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Amount"],
    bins=50,
    kde=True
)

plt.title("Transaction Amount Distribution")

plt.savefig(
    "images/amount_distribution.png",
    bbox_inches="tight"
)

plt.close()

# ============================================================
# CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(12, 10))

sns.heatmap(
    df.corr(),
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig(
    "images/correlation_heatmap.png",
    bbox_inches="tight"
)

plt.close()

# ============================================================
# MACHINE LEARNING
# ============================================================

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# ============================================================
# ACCURACY
# ============================================================

print("\n" + "=" * 60)
print("MODEL ACCURACY")
print("=" * 60)
print(accuracy_score(y_test, y_pred))

# ============================================================
# CLASSIFICATION REPORT
# ============================================================

print("\n" + "=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)
print(classification_report(y_test, y_pred))

# ============================================================
# CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.savefig(
    "images/confusion_matrix.png",
    bbox_inches="tight"
)

plt.close()

# ============================================================
# FINISHED
# ============================================================

print("\n✅ Analysis Completed Successfully!")
print("✅ Images saved in images folder.")
# Save cleaned dataset for Power BI

df.to_csv(
    "dataset/cleaned_creditcard.csv",
    index=False
)