
import coremltools as ct
from transformers import RobertaForSequenceClassification

def convert_to_coreml(model_path, output_path):
    """Convert the trained PyTorch model to CoreML."""
    model = RobertaForSequenceClassification.from_pretrained(model_path)
    example_input = {"input_ids": [[1] * 512]}
    traced_model = ct.convert(model, inputs=[ct.TensorType(name="input_ids", shape=example_input["input_ids"])])

    traced_model.save(output_path)
    print(f"CoreML model saved at {output_path}")

if __name__ == "__main__":
    convert_to_coreml("./fine-tuned-roberta", "./utils/ocd_model.mlmodel")
