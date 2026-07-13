from pathlib import Path
from typing import Literal
import joblib

import matplotlib.pyplot as plt
import pandas as pd
from loguru import logger
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from xevi.utils.text import preprocess, strip_tones


def load_dataset(filepath: Path):
    """Load csv file, preprocess text columns and return features and labels."""
    label_mapping = {
        "positive": 1,
        "neutral": 0,
        "negative": 2
    }
    try:
        dataset = pd.read_csv(filepath, usecols=["fongbe", "labels"])
    except Exception as e:
        logger.error(f"Erreur lors de la lecture du fichier CSV : {e}")
        raise e

    dataset = dataset.dropna(subset=["fongbe", "labels"])
    x = dataset["fongbe"].apply(lambda t: preprocess(strip_tones(t)))
    y = dataset["labels"].map(label_mapping)
    logger.success("Dataset loaded and preprocessed successfully.")
    return train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)


def get_pipeline(model_type: Literal["naive_bayes", "random_forest"] = "naive_bayes") -> Pipeline:
    """Create a scikit-learn pipeline with TF-IDF and a classifier."""
    logger.info(f"Creating pipeline: {model_type}")
    vectorizer = TfidfVectorizer(ngram_range=(1, 3), lowercase=True, token_pattern=r"\b\w+\b|[?.!,¿]")
    if model_type == "naive_bayes":
        classifier = MultinomialNB(alpha=0.1)
    elif model_type == "random_forest":
        classifier = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1, verbose=2)
    else:
        logger.error(f"Invalid model type: {model_type}. Choose 'naive_bayes' or 'random_forest'.")
        raise ValueError(f"Invalid model type: {model_type}")

    return Pipeline([
        ("vectorizer", vectorizer),
        ("classifier", classifier)
    ])


def train(model: Pipeline, x_train, y_train):
    """train choosen model and return the trained model"""
    logger.info(f"Model training started...")
    model.fit(x_train, y_train)
    logger.success(f"Model training completed...")
    return model


def evaluate(model: Pipeline, x_val, y_val):
    """get performance metrics of the trained model"""
    logger.info(f"Getting performance metrics")
    y_pred = model.predict(x_val)
    report = classification_report(y_val, y_pred)
    return report


def plot_metrics(model: Pipeline, x_val, y_val):
    y_pred = model.predict(x_val)
    cm = confusion_matrix(y_val, y_pred)

    classes = model.classes_
    display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)

    display.plot(cmap=plt.cm.Blues)
    plt.title("Matrice de Confusion")
    plt.show()


def predict(model: Pipeline, sentence: str):
    """predict sentiment of the given sentence"""
    logger.info(f"Predicting sentiment for sentence")
    cleaned_sentence = preprocess(strip_tones(sentence))
    prediction = model.predict([cleaned_sentence])
    label_inverse = {1: "Positive", 0: "Neutral", 2: "Negative"}
    return label_inverse[prediction[0]]


def save_model(model: Pipeline, filepath: Path) -> None:
    """Save the trained pipeline (vectorizer + classifier) to a file."""
    logger.info(f"Save model to :{filepath}")
    try:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, filepath, compress=3)
        logger.success(f"Model saved successfully")
    except Exception as e:
        logger.error(f"Error while saving model: {e}")
        raise e


def load_model(filepath: Path) -> Pipeline:
    """Load the trained pipeline from a file."""
    logger.info(f"Load model from :{filepath}")
    try:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        model = joblib.load(filepath)
        logger.success(f"Model loaded successfully")
        return model
    except Exception as e:
        logger.error(f"Error while loading model: {e}")
        raise e