# AI System – Environment & Repository Setup (Day 3)

## Objective
Create a professional Python development environment and modular repository foundation for an AI-based recruitment system.

## Folder responsibilities
- `data/`: sample datasets.
- `parsers/`: processes resume text.
- `ats_engine/`: compares resume and job-description keywords.
- `screening_ai/`: applies a basic screening rule.
- `interview_ai/`: generates example interview questions.
- `scoring/`: converts a match score into a rating.
- `utils/`: shared utilities and logging.
- `tests/`: automated pytest scripts.
- `main.py`: runs the demonstration workflow.

**Note:** This is a working starter/demo using rule-based examples. It does not contain a trained AI model and must not make real hiring decisions.

## Requirements
Python 3.10+, VS Code, pip, and optionally Git.

## Setup in VS Code (Windows PowerShell)
1. Open this folder in VS Code using **File → Open Folder**.
2. Open **Terminal → New Terminal**.
3. Create the virtual environment:
   ```powershell
   py -m venv .venv
   ```
4. Activate:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, use Command Prompt:
   ```cmd
   .venv\Scripts\activate.bat
   ```
5. Install dependencies:
   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

## Setup in macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

In VS Code, open Command Palette (Ctrl+Shift+P or Cmd+Shift+P), choose **Python: Select Interpreter**, and select the interpreter inside `.venv`.

## Run
```bash
python main.py
```

## Test
```bash
python -m pytest -v
```

## Logging
`utils/logger.py` creates `logs/ai_system.log` and records application events when the demo runs. The generated logs folder is excluded from Git.

## Formatting
```bash
python -m black .
```

## GitHub (optional)
Create an empty GitHub repository, then run:
```bash
git init
git add .
git commit -m "Day 3 environment and repository setup"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
Replace the placeholder with your own repository URL. Never upload `.venv/`, secrets, or private candidate data.

## Day 3 deliverables
1. Fully working AI repository: modular folders and Python modules.
2. Virtual environment setup: create `.venv` locally and install dependencies from `requirements.txt`.
3. Logging & testing structure: shared logger and pytest tests.
4. README documentation: this file explains the layout and setup, run, test, and formatting commands.

## Limitations / next steps
The parser currently accepts text, not PDF/DOC/DOCX files. The keyword matcher is a simple demonstration, not a validated hiring model. Future work can add document extraction, validated AI models, privacy controls, explainability, and human review.
