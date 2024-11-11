
import React, { useState } from 'react';
import axios from 'axios';

const TextInput = ({ endpoint }) => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!text) return alert("Please enter some text");
    try {
      const response = await axios.post(endpoint, { chat_text: text });
      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Error analyzing text.");
    }
  };

  return (
    <div>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter chat text here..."
        rows="5"
        cols="50"
      />
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

export default TextInput;
