
import React, { useState } from 'react';
import axios from 'axios';

export default function FineTune() {
  const [trainFile, setTrainFile] = useState(null);
  const [testFile, setTestFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e, setFile) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!trainFile || !testFile) return alert("Please upload both training and testing datasets");
    const formData = new FormData();
    formData.append('train_file', trainFile);
    formData.append('test_file', testFile);

    try {
      const response = await axios.post('http://127.0.0.1:8000/fine_tune', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Error fine-tuning the model.");
    }
  };

  return (
    <div>
      <h1>Fine-Tune the Model</h1>
      <div>
        <h3>Upload Training Dataset</h3>
        <input type="file" onChange={(e) => handleFileChange(e, setTrainFile)} />
      </div>
      <div>
        <h3>Upload Testing Dataset</h3>
        <input type="file" onChange={(e) => handleFileChange(e, setTestFile)} />
      </div>
      <button onClick={handleSubmit}>Fine-Tune</button>
      {result && (
        <div>
          <h3>Fine-Tuning Result:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
