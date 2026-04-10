# 🏗️ Hazem El-Ashry — AEC AI Assistant

<div align="center">

**A professional AI chatbot specialized for Architecture, Engineering & Construction (AEC)**

Built with Streamlit • Powered by OpenRouter (Free Models) • Tree of Thoughts Reasoning

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-6366F1?style=for-the-badge&logo=openai&logoColor=white)](https://openrouter.ai)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

</div>

---

## ✨ Features

### Core Features
- 🎯 **4 AEC Specialties** — Revit API Helper, Construction Safety Advisor, BIM Standards Consultant, Quantity Surveyor Assistant
- 🤖 **12+ Free AI Models** — DeepSeek R1, Gemma 3, Qwen 3, Llama 4, Mistral, Phi-4 and more via OpenRouter
- 🌳 **Tree of Thoughts Reasoning** — Multi-path analysis for deeper, structured problem-solving
- ⚡ **Streaming Responses** — Real-time line-by-line response streaming
- 💬 **Chat History** — Full conversation memory within session
- 🌡️ **Temperature Control** — Adjust creativity from Precise (0.0) to Experimental (2.0)
- 🗑️ **Clear Chat** — One-click conversation reset

### Bonus Features
- 📥 **Export Chat History** — Download conversations as formatted Markdown files
- 💡 **Preset Prompts** — Quick-start templates for each specialty
- 📊 **Token Counter** — Real-time token tracking (input, output, per-message)
- 🔑 **Secure API Key Input** — Password-masked input with direct link to get a free key

### Design
- 🎨 **Premium Dark Theme** — Glassmorphism, gradients, and micro-animations
- 📱 **Responsive Layout** — Works on desktop and mobile
- ✏️ **Custom Typography** — Inter + JetBrains Mono fonts
- 🌈 **Animated Elements** — Shimmer effects, floating icons, smooth transitions

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- An OpenRouter API key (free) — [Get one here](https://openrouter.ai/keys)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/hazem-el-ashry-aec-assistant.git
cd hazem-el-ashry-aec-assistant
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your OpenRouter API key
```

5. **Run the application**
```bash
streamlit run app.py
```

6. **Open in browser** — Navigate to `http://localhost:8501`

---

## 🔑 Getting Your API Key

1. Visit [OpenRouter Keys Page](https://openrouter.ai/keys)
2. Sign up or log in (free)
3. Click **"Create Key"**
4. Copy the key (starts with `sk-or-v1-...`)
5. Paste it in the sidebar of the app

> 💡 **Tip:** All models in this app are free-tier, so no payment is needed!

---

## 🏛️ Specialties

| Specialty | Description |
|-----------|-------------|
| 🏛️ **Revit API Helper** | Revit API, C#/Python scripting, Dynamo, BIM automation |
| 🦺 **Construction Safety Advisor** | OSHA compliance, JHA, safety plans, risk management |
| 📐 **BIM Standards Consultant** | ISO 19650, BEP, LOD specs, CDE setup, coordination |
| 📊 **Quantity Surveyor Assistant** | BOQ, cost estimation, procurement, contract admin |

---

## 🤖 Available Free Models

| Model | Provider | ID |
|-------|----------|----|
| DeepSeek R1 0528 | DeepSeek | `deepseek/deepseek-r1-0528:free` |
| DeepSeek V3 0324 | DeepSeek | `deepseek/deepseek-chat-v3-0324:free` |
| Gemma 3 27B | Google | `google/gemma-3-27b-it:free` |
| Gemma 3 12B | Google | `google/gemma-3-12b-it:free` |
| Qwen3 235B A22B | Qwen | `qwen/qwen3-235b-a22b:free` |
| Qwen3 30B A3B | Qwen | `qwen/qwen3-30b-a3b:free` |
| Qwen2.5 Coder 32B | Qwen | `qwen/qwen-2.5-coder-32b-instruct:free` |
| Llama 4 Maverick | Meta | `meta-llama/llama-4-maverick:free` |
| Llama 4 Scout | Meta | `meta-llama/llama-4-scout:free` |
| Llama 3.3 70B | Meta | `meta-llama/llama-3.3-70b-instruct:free` |
| Mistral Small 3.1 24B | Mistral | `mistralai/mistral-small-3.1-24b-instruct:free` |
| Phi-4 Multimodal | Microsoft | `microsoft/phi-4-multimodal-instruct:free` |

---

## 🌳 Tree of Thoughts (ToT)

The assistant uses a **Tree of Thoughts** reasoning approach:

1. **🌱 Branch Generation** — Identifies 2-3 distinct approaches
2. **🔍 Evaluation** — Analyzes pros/cons of each approach
3. **🎯 Selection** — Chooses the optimal path with justification
4. **🛠️ Implementation** — Provides detailed, actionable output

This ensures more thorough, well-reasoned responses compared to standard single-path reasoning.

---

## 📁 Project Structure

```
hazem-el-ashry-aec-assistant/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io) with custom CSS
- **AI API**: [OpenRouter](https://openrouter.ai) (OpenAI-compatible)
- **Token Counting**: [tiktoken](https://github.com/openai/tiktoken) (cl100k_base)
- **Fonts**: Google Fonts (Inter, JetBrains Mono)

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ by Hazem El-Ashry**

*Empowering AEC professionals with AI*

</div>
