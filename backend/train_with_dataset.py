
# Copyright (c) 2024 Skytells Research, Inc.
# All rights reserved.
# https://www.skytells.io

import os
import json
from transformers import RobertaTokenizer, RobertaForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# Load configuration
config_path = "config.json"
if not os.path.exists(config_path):
    raise FileNotFoundError("Configuration file not found.")

with open(config_path, "r") as config_file:
    config = json.load(config_file)

# Load tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained(config["model_name"])
model = RobertaForSequenceClassification.from_pretrained(config["model_name"], num_labels=2)

def load_custom_dataset(train_file, test_file):
    """Load custom datasets."""
    return load_dataset("csv", data_files={"train": train_file, "test": test_file}, column_names=["text", "label"])

def preprocess_function(examples):
    """Tokenize the dataset."""
    return tokenizer(examples["text"], truncation=True, padding=True, max_length=512)

def compute_metrics(eval_pred):
    """Compute metrics for evaluation."""
    logits, labels = eval_pred
    predictions = logits.argmax(axis=-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average="binary")
    acc = accuracy_score(labels, predictions)
    return {"accuracy": acc, "precision": precision, "recall": recall, "f1": f1}

def train_with_dataset(train_file, test_file):
    """Train the model with the given dataset."""
    dataset = load_custom_dataset(train_file, test_file)
    tokenized_datasets = dataset.map(preprocess_function, batched=True)

    training_args = TrainingArguments(**config["training_args"])

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
    )

    # Train the model
    trainer.train()

    # Save the fine-tuned model
    model.save_pretrained(config["fine_tuned_model_path"])
    tokenizer.save_pretrained(config["fine_tuned_model_path"])

    print("Training complete. Model saved to:", config["fine_tuned_model_path"])

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train the model with a dataset.")
    parser.add_argument("--train_file", type=str, required=True, help="Path to the training dataset.")
    parser.add_argument("--test_file", type=str, required=True, help="Path to the testing dataset.")
    args = parser.parse_args()

    train_with_dataset(args.train_file, args.test_file)
