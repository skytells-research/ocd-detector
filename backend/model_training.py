
from transformers import RobertaTokenizer, RobertaForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

def train_model(train_file: str, test_file: str):
    tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
    model = RobertaForSequenceClassification.from_pretrained("roberta-base", num_labels=2)

    datasets = load_dataset("csv", data_files={"train": train_file, "test": test_file})

    def preprocess(example):
        return tokenizer(example["text"], truncation=True, padding=True, max_length=512)

    tokenized_datasets = datasets.map(preprocess, batched=True)

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir="./logs",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
    )

    trainer.train()
    model.save_pretrained("./fine_tuned_roberta")
    tokenizer.save_pretrained("./fine_tuned_roberta")
