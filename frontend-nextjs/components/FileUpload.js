
import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = ({ endpoint }) => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) return alert("Please select a file");
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(endpoint, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Error uploading file.");
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Analyze</button>
      {result && (
        <div>
          <h3>Analysis Result:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default FileUpload;
