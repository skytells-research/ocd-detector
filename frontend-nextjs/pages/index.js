
import React from 'react';
import FileUpload from '../components/FileUpload';
import TextInput from '../components/TextInput';

export default function Home() {
  return (
    <div>
      <h1>OCD Chat Analysis</h1>
      <p>Analyze text or screenshots for OCD tendencies using AI.</p>
      
      <h2>Analyze Text</h2>
      <TextInput endpoint="http://127.0.0.1:8000/analyze_text" />
      
      <h2>Analyze Screenshot</h2>
      <FileUpload endpoint="http://127.0.0.1:8000/analyze_image" />
    </div>
  );
}
