"""Data collection and cleaning script for the French-Fongbe parallel corpus.

This script downloads the French-Fongbe dataset from Hugging Face:
https://huggingface.co/datasets/Shads229/french-fongbe-corpus

@author: Victoria <https://github.com/IFRI-AI-Classes/XoNet/blob/main/src/ingestion/fetch_hf_datasets.py>
"""
import csv
from datasets import load_dataset

# download the raw dataset from Hugging Face
dataset3 = load_dataset("Shads229/french-fongbe-corpus")

# extract, clean, and save to a CSV file
with open("data/French_Fongbe_dataset3.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["french", "fongbe"])
    writer.writeheader()
    for objet in dataset3["train"]:
        messages = objet["messages"]
        texte_french = messages[0]["content"]
        clean_french = texte_french.replace("Traduire en fon : ", "")
        texte_fongbe = messages[1]["content"]
        clean_translation = {"french": clean_french, "fongbe": texte_fongbe}
        writer.writerow(clean_translation)