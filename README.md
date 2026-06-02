# 🏥 PrescriptiLens

> AI-powered prescription reader that extracts handwritten/printed text from prescription images and answers medical queries using Google Gemini.

---

## 🔴 The Problem

Prescription readability is a genuine patient safety issue. Handwritten prescriptions from doctors are notoriously difficult to read — for patients, pharmacists, and caregivers alike. Misread prescriptions contribute to medication errors worldwide.

Beyond readability, patients often have follow-up questions about their prescriptions:
- *What is this medication for?*
- *What are the side effects?*
- *Can I take this with food?*

Traditionally, answering these requires calling the clinic, waiting for a callback, or wading through unreliable sources online.

---

## ✅ The Solution

**PrescriptiLens** is a two-stage AI pipeline that:

1. **Reads** the prescription image using a multimodal vision model (Gemini 1.5 Flash)
2. **Answers** the patient's question about it using a language model (Gemini Pro), grounded in the extracted prescription text

The result: upload your prescription, ask your question, get a detailed medical response — in seconds.

---

## 🏗️ Architecture

```
User
 │
 ▼
┌─────────────────────────────┐
│      Streamlit Frontend      │
│  - Image Upload              │
│  - Question Input            │
│  - Result Display            │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Stage 1: Vision Extraction │
│   Model: Gemini 1.5 Flash    │
│   Input:  Prescription Image │
│   Output: Extracted Text     │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Stage 2: Medical QA        │
│   Model: Gemini Pro          │
│   Input:  Extracted Text     │
│           + User Question    │
│           + Safety Prompt    │
│   Output: Medical Answer     │
└─────────────────────────────┘
```

**Flow in plain terms:**

- The image is passed directly to Gemini 1.5 Flash (multimodal) which reads whatever is written on it
- The extracted text, user's question, and a safety system prompt are concatenated and sent to Gemini Pro
- Gemini Pro responds only to medically relevant queries; for anything off-topic it responds with "I don't know"

---

## 🤔 Why I Chose What I Chose

### Gemini 1.5 Flash — for vision
Flash is Google's lightweight multimodal model. It handles image + text input natively, which is exactly what prescription OCR requires. I chose Flash over Pro for this stage because:
- It's faster and cheaper for a single extraction task
- Prescription reading doesn't require deep reasoning, just accurate OCR-level understanding
- The output just needs to be clean text, not a structured response

### Gemini Pro — for QA
The extracted text + question gets passed to Gemini Pro for the reasoning layer. Pro is better at nuanced, detailed responses which is what you want for medical queries. The safety prompt constrains it to medical topics only, reducing hallucination risk on off-domain questions.

### Streamlit — for the UI
This is a demo/portfolio project. Streamlit lets you build a functional, shareable web UI in under 50 lines of Python. No frontend code needed. For a production version, this would be replaced with a proper React/FastAPI setup.

### LangChain in requirements (not yet in logic)
LangChain is imported but not actively used in the core pipeline — the direct `google-generativeai` SDK handles both calls. LangChain was included for future extensibility (e.g. adding memory, chaining, or retrieval).

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A [Google AI Studio](https://aistudio.google.com/app/apikey) API key

### Installation

```bash
git clone https://github.com/Touseeq99/PrescriptiLens.git
cd PrescriptiLens
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the root directory:

```env
Google_API_key=your_api_key_here
```

> ⚠️ **Never commit your `.env` file.** Add it to `.gitignore`.

### Run

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 📸 Usage

1. Upload a prescription image (JPG or PNG)
2. Type your question (e.g. *"What is amoxicillin used for?"*)
3. Click **Result**
4. Read the AI-generated medical response

---

## 📁 Project Structure

```
PrescriptiLens/
├── app.py              # Main application — vision extraction + QA pipeline
├── requirements.txt    # Python dependencies
├── .env                # API keys (never commit this)
└── README.md
```

---

## ⚠️ Disclaimer

PrescriptiLens is a **research/demo project**. It is not a substitute for professional medical advice. Always consult a licensed healthcare provider for medical decisions. The AI responses are generated and may contain errors.

---

## 🛠️ Built With

- [Google Gemini API](https://ai.google.dev/) — Vision + Language models
- [Streamlit](https://streamlit.io/) — Web UI
- [Pillow](https://pillow.readthedocs.io/) — Image handling
- [LangChain](https://langchain.com/) — (Scaffolded for future use)

---

## 👤 Author

**Touseeq Ahmed**  
AI Engineer | [GitHub](https://github.com/Touseeq99)
