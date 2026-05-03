# AI Code Fixer Agent

A Python-based AI agent that uses the Gemini API to analyze, debug, and refactor code within a local directory. This agent has the ability to read files, run Python scripts to check for errors, and apply fixes automatically.

## Features

- **Automated Debugging**: Identifies logical and syntax errors in Python code.
- **Function Calling**: Utilizes specialized tools to interact with the filesystem and the Python interpreter.
- **Iterative Refinement**: Runs code after making changes to ensure the fix works as intended.

## Technologies Used

- Python
- Google Gemini API (Generative AI)
- `subprocess` and `os` modules for system interaction

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set up your environment variables:
Create a .env file and add your Gemini API key:
```bash
API_KEY=your_gemini_api_key_here
```
## Usage
Run the agent by executing the main script:

python main.py

## Security Warning
Use with caution. This agent has the authority to execute Python code and modify files on your local machine. Never run this agent on a sensitive codebase without a backup or version control (Git) in place.