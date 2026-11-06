# 🤖 LangChain OpenAI, Google Gemini, and Groq-LLM Provider Integration

A clean, modular Python project demonstrating how to integrate and switch between leading Large Language Model (LLM) providers—**OpenAI**, **Google Gemini**, and **Groq**—using the unified **LangChain** ecosystem.

Designed with production best practices, strict environment variable isolation, and clean repository structure.

---

## 🌟 Features

- **Multi-Provider Architecture:** Seamlessly query models from OpenAI, Google GenAI, and Groq via LangChain integrations (`langchain-openai`, `langchain-google-genai`, `langchain-groq`).
- **Unified Interface:** Standardized invocation syntax using LangChain's `ChatModel` interface (`llm.invoke()`).
- **Security-First Design:** Full separation of source code and sensitive API credentials via `.env` configuration and `.gitignore` rules.
- **Isolated Environments:** Clean dependency isolation using standard Python virtual environments (`.venv`).

---

## Demo

<img width="1589" height="822" alt="Langchain_Groq_Intergration" src="https://github.com/user-attachments/assets/be8ab141-7550-48a0-9a55-ac78bc8fe4d8" />
<img width="1588" height="819" alt="Langchain_Gemini_Intergration" src="https://github.com/user-attachments/assets/83219557-4dd8-4c49-beff-d0f7842dd9ac" />
<img width="1589" height="818" alt="Langchain_OpenAI_Intergration" src="https://github.com/user-attachments/assets/9687fac5-1a8b-4eee-a1d3-a99458cd4b57" />

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.10+
- **Orchestration Framework:** LangChain (`langchain-core`)
- **LLM Provider Integrations:**
  - `langchain-openai`
  - `langchain-google-genai`
  - `langchain-groq`
- **Environment & Configuration:** `python-dotenv`
- **IDE & Tooling:** VS Code, PowerShell

---

## 📁 Project Structure

```text
python-langchain-openai-gemini-groq-llm-integration/
├── .venv/                   # Python virtual environment (git-ignored)
├── notebooks/               # Executable LLM script workflows
│   ├── gemini_llm.py        # LangChain + Google Gemini integration
│   ├── groq_llm.py          # LangChain + Groq integration
│   └── openai_llm.py        # LangChain + OpenAI integration
├── .env                     # Local API keys & secrets (git-ignored)
├── .gitignore               # Excludes secrets, cache, and virtual environments
├── README.md                # Project documentation
└── requirement.txt          # Project package dependencies
```

---

## ⚙️ Getting Started & Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/chanchal-kumar-mandal/python-langchain-openai-gemini-groq-llm-integration.git
cd python-langchain-openai-gemini-groq-llm-integration
```

### 2. Create and Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the root directory of the project and add your API credentials:

```env
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

> **Note:** Obtain your keys directly from provider dashboards:
> - [Google AI Studio](https://aistudio.google.com/api-keys)
> - [OpenAI Platform](https://platform.openai.com/api-keys)
> - [Groq Console](https://console.groq.com/keys)

---

## 🚀 Execution & Usage

Navigate to the `notebooks/` directory and execute any provider script:

### Google Gemini Script (`gemini_llm.py`)
```bash
cd notebooks
python gemini_llm.py
```

### Groq Script (`groq_llm.py`)
```bash
python groq_llm.py
```

### OpenAI Script (`openai_llm.py`)
```bash
python openai_llm.py
```

---

## 🛡️ Best Practices & Troubleshooting

* **Import Collision Prevention:** Avoid naming local Python files after installed libraries (e.g., use `groq_llm.py` or `gemini_llm.py` instead of `langchain_groq.py` or `langchain_google_genai.py`).
* **Secret Protection:** Never commit `.env` or sensitive API keys to version control. Ensure `.env` is listed in your `.gitignore` file before pushing commits.
```