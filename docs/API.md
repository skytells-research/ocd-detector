
# OCD Detector API Documentation

## Overview
This API provides endpoints for detecting Obsessive-Compulsive Disorder (OCD) tendencies using text, image, and voice analysis. It also includes training capabilities and health monitoring.

## Endpoints

### 1. `/` (GET)
- **Description**: Welcome message.
- **Response**:
  ```json
  {
    "message": "Welcome to the enhanced OCD Detector API"
  }
  ```

### 2. `/analyze/text` (POST)
- **Description**: Analyze a given text input for OCD tendencies.
- **Request Payload**:
  ```json
  {
    "chat_text": "string"
  }
  ```
- **Response**:
  ```json
  {
    "text_analysis": {...}
  }
  ```

### 3. `/analyze/image` (POST)
- **Description**: Extract and analyze text from an uploaded image.
- **Request Payload**: An image file.
- **Response**:
  ```json
  {
    "image_analysis": {
      "extracted_text": "string",
      "analysis_result": {...}
    }
  }
  ```

### 4. `/analyze/voice` (POST)
- **Description**: Convert a voice recording to text and analyze it.
- **Request Payload**: An audio file.
- **Response**:
  ```json
  {
    "voice_analysis": {
      "recognized_text": "string",
      "analysis_result": {...}
    }
  }
  ```

### 5. `/train` (POST)
- **Description**: Train the model with custom datasets.
- **Request Payload**:
  ```json
  {
    "train_file": "string",
    "test_file": "string"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Model training completed successfully."
  }
  ```

### 6. `/health` (GET)
- **Description**: Monitor API health and system metrics.
- **Response**:
  ```json
  {
    "status": "healthy",
    "uptime": "string",
    "cpu_usage": "string",
    "memory_usage": "string"
  }
  ```
