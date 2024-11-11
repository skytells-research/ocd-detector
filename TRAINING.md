
# Training Guide

## Training with Custom Dataset
1. Place your training and testing datasets in `backend/datasets/`.
2. Run the training script:
   ```bash
   python backend/train_with_dataset.py --train_file backend/datasets/train.csv --test_file backend/datasets/test.csv
   ```

## Fine-Tuning
1. Edit `config.json` to customize training parameters.
2. Run the fine-tuning script:
   ```bash
   python backend/train_with_dataset.py --train_file <path-to-train.csv> --test_file <path-to-test.csv>
   ```

## Exporting to CoreML
Convert the trained model to CoreML format:
```bash
python utils/convert_to_coreml.py
```

