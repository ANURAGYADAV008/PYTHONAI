# PYTHONAI Project

A Python-based AI project for chat models and prompt generation.

## Prerequisites

- Python 3.8 or higher
- Ollama (for local AI model inference)

## Installation

### 1. Install Ollama

Ollama allows you to run large language models locally on your machine.

1. Download Ollama from the official website: [https://ollama.ai/download](https://ollama.ai/download)
2. Run the installer for your operating system (Windows, macOS, or Linux).
3. After installation, open a terminal and verify Ollama is installed by running:
   ```
   ollama --version
   ```
4. Pull a model (e.g., Llama 3.2):
   ```
   ollama pull llama3.2
   ```

### 2. Set Up the Python Environment

1. Clone or download this repository to your local machine.

2. Navigate to the project directory:
   ```
   cd PYTHONAI
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

6. Create a `.env` file in the root directory and add your Hugging Face token:
   ```
   HF_TOKEN=your_hugging_face_token_here
   ```
   (Get your token from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens))

## Usage

### Running the Chat Model

Execute the chat model script:
```
python ChatMOdel/chatmodel.py
```

### Using Prompt Generation

Run the prompt UI:
```
python Prompt/promptui.py
```

### GPU Detection

Check GPU availability:
```
python getgpu.py
```

## Project Structure

- `getgpu.py`: GPU detection script
- `ChatMOdel/chatmodel.py`: Chat model implementation using Hugging Face transformers
- `Prompt/`: Prompt generation and UI components
  - `promptgen.py`: Prompt generation logic
  - `promptui.py`: Prompt UI
  - `template.json`: Prompt templates
- `requirements.txt`: Python dependencies

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the MIT License.