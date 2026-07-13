# Fon sentiment Classification

A simple baseline project for **sentiment analysis in Fon (Fongbe)**.

This project builds a sentiment classification dataset from a parallel French–Fon corpus by annotating the French sentences and transferring the sentiment labels to their Fon translations. 
It also provides baseline machine learning models for sentiment classification.

### getting started

Install the project dependencies:
```bash
pip install -r requirements.txt
```

### structure

```text
experiments/fon_sentiment_classification/
├── data/
│   ├── French_Fongbe_dataset3.csv          # Cleaned parallel corpus (French-Fongbe)
│   └── French_Fongbe_Sentiment_Dataset.csv # Annotated dataset with sentiment labels
├── hf_dataset.py                           # Downloads and parses raw data from Hugging Face
├── notebooks/
│   ├── annotate_dataset.ipynb              # Automates French-side sentiment tagging
│   └── train_model.ipynb                   # Model exploration, evaluation, and plotting
├── utils.py                                # Shared helper functions for ML pipeline & saving
├── README.md                               # Project documentation
└── requirements.txt                        # Python dependencies
```

### dataset & models

The project is based on the **[French–Fongbe Parallel Corpus](https://huggingface.co/datasets/Shads229/french-fongbe-corpus)**, where sentiment labels are automatically generated for the French sentences and transferred to the corresponding Fon translations.

The current implementation includes two classical machine learning baselines: multinomial naive bayes and random forest.

### contributing

Contributions are welcome. Feel free to open an issue to report bugs, suggest improvements, or discuss new ideas. Pull requests are also appreciated.

