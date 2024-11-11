
from setuptools import setup, find_packages

setup(
    name="ocd_chat_analysis",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "transformers",
        "datasets",
        "torch",
        "scikit-learn",
        "pytesseract",
        "Pillow",
        "speechrecognition",
        "pyaudio",
        "openai",
        "coremltools"
    ],
    entry_points={
        "console_scripts": [
            "ocd_train=backend.train_with_dataset:main"
        ]
    },
)
