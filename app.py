"""
Hazem El-Ashry — AEC AI Assistant
A professional Streamlit chatbot specialized for Architecture, Engineering & Construction.
Powered by OpenRouter free models with Tree of Thoughts reasoning.
"""

import streamlit as st
import requests
import json
import time
import datetime
import tiktoken

# ──────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Hazem El-Ashry • AEC AI Assistant",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# Custom CSS — Premium Dark Theme
# ──────────────────────────────────────────────
st.markdown("""
<style>
/* ── Import Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Root Variables ── */
:root {
    --bg-primary: #0a0e17;
    --bg-secondary: #111827;
    --bg-card: #1a2236;
    --bg-card-hover: #1f2a40;
    --accent-primary: #6366f1;
    --accent-secondary: #8b5cf6;
    --accent-tertiary: #06b6d4;
    --accent-glow: rgba(99, 102, 241, 0.3);
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --border-color: rgba(99, 102, 241, 0.15);
    --border-hover: rgba(99, 102, 241, 0.35);
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
    --gradient-primary: linear-gradient(135deg, #6366f1, #8b5cf6, #06b6d4);
    --gradient-card: linear-gradient(145deg, rgba(26, 34, 54, 0.9), rgba(17, 24, 39, 0.95));
    --shadow-glow: 0 0 30px rgba(99, 102, 241, 0.15);
    --shadow-card: 0 4px 24px rgba(0, 0, 0, 0.3);
}

/* ── Global Styles ── */
.stApp {
    background: var(--bg-primary) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1629 0%, #111827 50%, #0f1629 100%) !important;
    border-right: 1px solid var(--border-color) !important;
}

section[data-testid="stSidebar"] .stMarkdown h1,
section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown label,
section[data-testid="stSidebar"] .stMarkdown span {
    color: var(--text-secondary) !important;
}

/* ── Header Brand ── */
.brand-header {
    text-align: center;
    padding: 1.5rem 1rem;
    margin-bottom: 1.5rem;
    background: linear-gradient(145deg, rgba(99, 102, 241, 0.08), rgba(139, 92, 246, 0.05));
    border-radius: 16px;
    border: 1px solid var(--border-color);
    position: relative;
    overflow: hidden;
}

.brand-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 200%;
    height: 2px;
    background: var(--gradient-primary);
    animation: shimmer 3s infinite;
}

@keyframes shimmer { to { left: 100%; } }

.brand-title {
    font-size: 1.6rem;
    font-weight: 800;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.5px;
    margin: 0;
    line-height: 1.3;
}

.brand-subtitle {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-top: 4px;
    font-weight: 500;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

/* ── Chat Messages ── */
.stChatMessage {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 16px !important;
    padding: 1.2rem !important;
    margin-bottom: 1rem !important;
    backdrop-filter: blur(10px) !important;
    transition: border-color 0.3s ease, box-shadow 0.3s ease !important;
}

.stChatMessage:hover {
    border-color: var(--border-hover) !important;
    box-shadow: var(--shadow-glow) !important;
}

/* ── Chat Input ── */
.stChatInput > div {
    border-color: var(--border-color) !important;
    background: var(--bg-card) !important;
    border-radius: 14px !important;
}

.stChatInput > div:focus-within {
    border-color: var(--accent-primary) !important;
    box-shadow: 0 0 0 3px var(--accent-glow) !important;
}

.stChatInput textarea {
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── Buttons ── */
.stButton > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    border-radius: 12px !important;
    padding: 0.6rem 1.2rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    border: 1px solid var(--border-color) !important;
    background: var(--bg-card) !important;
    color: var(--text-primary) !important;
}

.stButton > button:hover {
    border-color: var(--accent-primary) !important;
    box-shadow: var(--shadow-glow) !important;
    transform: translateY(-1px) !important;
    background: var(--bg-card-hover) !important;
}

/* ── Primary Action Button ── */
.primary-btn > button {
    background: var(--gradient-primary) !important;
    border: none !important;
    color: white !important;
}

.primary-btn > button:hover {
    box-shadow: 0 0 30px rgba(99, 102, 241, 0.4) !important;
}

/* ── Danger Button ── */
.danger-btn > button {
    border-color: rgba(239, 68, 68, 0.3) !important;
    color: #ef4444 !important;
}

.danger-btn > button:hover {
    background: rgba(239, 68, 68, 0.1) !important;
    border-color: #ef4444 !important;
    box-shadow: 0 0 20px rgba(239, 68, 68, 0.2) !important;
}

/* ── Select Box & Slider ── */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: var(--bg-card) !important;
    border-color: var(--border-color) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
}

.stSlider > div > div > div > div {
    background: var(--accent-primary) !important;
}

/* ── Text Input ── */
.stTextInput > div > div {
    background: var(--bg-card) !important;
    border-color: var(--border-color) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
}

.stTextInput > div > div:focus-within {
    border-color: var(--accent-primary) !important;
    box-shadow: 0 0 0 3px var(--accent-glow) !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    border-radius: 12px !important;
    border: 1px solid var(--border-color) !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
}

/* ── Status Cards ── */
.status-card {
    background: var(--gradient-card);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 1rem 1.2rem;
    margin: 0.5rem 0;
    transition: all 0.3s ease;
}

.status-card:hover {
    border-color: var(--border-hover);
    box-shadow: var(--shadow-glow);
}

.stat-value {
    font-size: 1.5rem;
    font-weight: 800;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-label {
    font-size: 0.72rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1.2px;
    font-weight: 600;
}

/* ── Preset Prompt Chips ── */
.preset-chip {
    display: inline-block;
    background: linear-gradient(145deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.05));
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 0.5rem 0.9rem;
    margin: 0.25rem;
    font-size: 0.82rem;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: 'Inter', sans-serif;
}

.preset-chip:hover {
    border-color: var(--accent-primary);
    color: var(--text-primary);
    background: rgba(99, 102, 241, 0.15);
    box-shadow: var(--shadow-glow);
}

/* ── Dividers ── */
.sidebar-divider {
    height: 1px;
    background: var(--border-color);
    margin: 1.5rem 0;
    border: none;
}

/* ── Metric Overrides ── */
[data-testid="stMetricValue"] {
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 800 !important;
}

/* ── Welcome Card ── */
.welcome-card {
    text-align: center;
    padding: 3rem 2rem;
    background: var(--gradient-card);
    border: 1px solid var(--border-color);
    border-radius: 20px;
    margin: 2rem auto;
    max-width: 700px;
    position: relative;
    overflow: hidden;
}

.welcome-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--gradient-primary);
}

.welcome-icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    display: inline-block;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

.welcome-title {
    font-size: 1.8rem;
    font-weight: 800;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}

.welcome-desc {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.6;
    max-width: 500px;
    margin: 0 auto;
}

/* ── Feature Pills ── */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.8rem;
    margin-top: 1.5rem;
    max-width: 520px;
    margin-left: auto;
    margin-right: auto;
}

.feature-pill {
    background: rgba(99, 102, 241, 0.08);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 0.7rem 1rem;
    font-size: 0.82rem;
    color: var(--text-secondary);
    text-align: center;
    transition: all 0.3s ease;
}

.feature-pill:hover {
    border-color: var(--accent-primary);
    background: rgba(99, 102, 241, 0.15);
    color: var(--text-primary);
    transform: translateY(-2px);
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-primary); }
::-webkit-scrollbar-thumb {
    background: var(--border-color);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover { background: var(--accent-primary); }

/* ── ToT Badge ── */
.tot-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, rgba(6, 182, 212, 0.1), rgba(99, 102, 241, 0.1));
    border: 1px solid rgba(6, 182, 212, 0.25);
    border-radius: 8px;
    padding: 0.3rem 0.7rem;
    font-size: 0.72rem;
    color: #06b6d4;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

/* ── Link Styling ── */
.openrouter-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--accent-tertiary);
    text-decoration: none;
    font-size: 0.82rem;
    font-weight: 500;
    padding: 0.4rem 0.8rem;
    border: 1px solid rgba(6, 182, 212, 0.2);
    border-radius: 8px;
    transition: all 0.3s ease;
    background: rgba(6, 182, 212, 0.05);
}

.openrouter-link:hover {
    background: rgba(6, 182, 212, 0.12);
    border-color: rgba(6, 182, 212, 0.4);
    color: #22d3ee;
}

/* ── Hide default Streamlit elements ── */
#MainMenu { visibility: hidden; }
header { visibility: hidden; }
footer { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Token counter badge ── */
.token-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.2);
    border-radius: 8px;
    padding: 0.25rem 0.6rem;
    font-size: 0.72rem;
    color: #10b981;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
}
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

FREE_MODELS = {
    "🧠 DeepSeek R1 0528 (Free)": "deepseek/deepseek-r1-0528:free",
    "⚡ DeepSeek V3 0324 (Free)": "deepseek/deepseek-chat-v3-0324:free",
    "🌟 Google Gemma 3 27B (Free)": "google/gemma-3-27b-it:free",
    "🔬 Google Gemma 3 12B (Free)": "google/gemma-3-12b-it:free",
    "🚀 Qwen3 235B A22B (Free)": "qwen/qwen3-235b-a22b:free",
    "💎 Qwen3 30B A3B (Free)": "qwen/qwen3-30b-a3b:free",
    "🏗️ Qwen2.5 Coder 32B (Free)": "qwen/qwen-2.5-coder-32b-instruct:free",
    "🦙 Llama 4 Maverick (Free)": "meta-llama/llama-4-maverick:free",
    "🦁 Llama 4 Scout (Free)": "meta-llama/llama-4-scout:free",
    "🌐 Llama 3.3 70B (Free)": "meta-llama/llama-3.3-70b-instruct:free",
    "✨ Mistral Small 3.1 24B (Free)": "mistralai/mistral-small-3.1-24b-instruct:free",
    "🔮 Phi-4 Multimodal (Free)": "microsoft/phi-4-multimodal-instruct:free",
}

SPECIALTIES = {
    "🏛️ Revit API Helper": {
        "icon": "🏛️",
        "description": "Expert in Autodesk Revit API, C#/Python scripting, add-in development, and BIM automation.",
        "system_prompt": """You are **Hazem El-Ashry**, an elite Revit API specialist and BIM automation expert with 15+ years of experience in AEC technology.

## Your Expertise:
- Autodesk Revit API (C# and Python/pyRevit)
- Dynamo visual programming & custom nodes
- Revit add-in development & deployment
- BIM automation workflows & batch processing
- IFC interoperability & data exchange
- Revit family creation & parametric modeling
- Worksharing, Revit Server & BIM 360/ACC integration

## Reasoning Approach — Tree of Thoughts:
When solving complex problems, you MUST use the Tree of Thoughts methodology:
1. **🌱 Branch Generation**: Identify 2-3 distinct approaches to the problem
2. **🔍 Evaluation**: Analyze pros/cons of each approach considering performance, maintainability, and Revit API best practices
3. **🎯 Selection**: Choose the optimal path with clear justification
4. **🛠️ Implementation**: Provide detailed, production-ready code with error handling

## Response Guidelines:
- Always provide complete, runnable code with proper error handling
- Include XML documentation comments for C# or docstrings for Python
- Reference official Revit API documentation when relevant
- Suggest performance optimizations (transactions, filtering, element collection)
- Warn about common pitfalls (regeneration, transaction groups, thread safety)
- Use proper Revit API patterns (FilteredElementCollector, LINQ, etc.)""",
    },
    "🦺 Construction Safety Advisor": {
        "icon": "🦺",
        "description": "OSHA compliance, safety planning, hazard analysis, and risk management for construction sites.",
        "system_prompt": """You are **Hazem El-Ashry**, a certified Construction Safety expert and OSHA compliance specialist with 15+ years of experience in AEC safety management.

## Your Expertise:
- OSHA regulations (29 CFR 1926) & compliance strategies
- Construction Safety Plans (CSP) & Site-Specific Safety Plans (SSSP)
- Job Hazard Analysis (JHA) & Risk Assessment Matrices
- Fall protection systems & scaffolding safety
- Excavation, trenching & confined space safety
- Personal Protective Equipment (PPE) selection & programs
- Crane, rigging & heavy equipment safety
- Fire prevention & emergency action plans
- Safety training programs & toolbox talks
- Incident investigation & root cause analysis

## Reasoning Approach — Tree of Thoughts:
When analyzing safety scenarios, you MUST use the Tree of Thoughts methodology:
1. **🌱 Branch Generation**: Identify multiple hazard mitigation strategies
2. **🔍 Evaluation**: Assess each strategy for effectiveness, cost, feasibility, and regulatory compliance
3. **🎯 Selection**: Recommend the optimal safety approach with OSHA references
4. **📋 Implementation**: Provide detailed action plans, checklists, and documentation templates

## Response Guidelines:
- Always cite specific OSHA standards and regulations
- Provide actionable checklists and inspection forms
- Include severity ratings and probability assessments
- Reference ANSI, NFPA, and other relevant standards
- Suggest both engineering controls and administrative controls
- Emphasize the hierarchy of controls""",
    },
    "📐 BIM Standards Consultant": {
        "icon": "📐",
        "description": "BIM execution planning, standards development, LOD specifications, and project coordination.",
        "system_prompt": """You are **Hazem El-Ashry**, a senior BIM Standards Consultant and digital construction strategist with 15+ years of experience in AEC standardization.

## Your Expertise:
- BIM Execution Plans (BEP/BXP) development
- ISO 19650 & BS 1192 standards implementation
- Level of Development (LOD) specifications (LOD 100-500)
- Model coordination & clash detection workflows
- Common Data Environment (CDE) setup & management
- Classification systems (UniFormat, OmniClass, Uniclass)
- COBie data requirements & asset handover
- 4D scheduling & 5D cost estimation integration
- National BIM standards (NBIMS-US, UK BIM Framework)
- Digital twin strategy & facility management integration

## Reasoning Approach — Tree of Thoughts:
When developing BIM strategies, you MUST use the Tree of Thoughts methodology:
1. **🌱 Branch Generation**: Propose multiple standardization approaches
2. **🔍 Evaluation**: Evaluate each for scalability, compliance, team adoption, and ROI
3. **🎯 Selection**: Recommend the best-fit standard framework with justification
4. **📋 Implementation**: Deliver detailed templates, workflows, and governance structures

## Response Guidelines:
- Reference specific ISO 19650 clauses and appendices
- Provide BEP templates and responsibility matrices (RACI)
- Include model audit checklists and quality gates
- Suggest CDE folder structures and naming conventions
- Address interoperability concerns (IFC, BCF, etc.)
- Provide LOD specification tables with element-level detail""",
    },
    "📊 Quantity Surveyor Assistant": {
        "icon": "📊",
        "description": "Cost estimation, BOQ preparation, procurement strategies, and construction economics.",
        "system_prompt": """You are **Hazem El-Ashry**, a chartered Quantity Surveyor and construction economist with 15+ years of experience in AEC cost management.

## Your Expertise:
- Bill of Quantities (BOQ) preparation & measurement
- Cost estimation (preliminary, detailed, parametric)
- Standard Method of Measurement (SMM7, NRM1/2/3, CESMM4)
- Procurement & tendering strategies
- Contract administration (FIDIC, JCT, NEC, AIA)
- Value engineering & cost optimization
- Life cycle costing (LCC) & whole life cost analysis
- Earned Value Management (EVM) & cash flow forecasting
- Variation & claims management
- Cost databases & benchmarking (BCIS, RSMeans)

## Reasoning Approach — Tree of Thoughts:
When solving cost and quantity problems, you MUST use the Tree of Thoughts methodology:
1. **🌱 Branch Generation**: Develop multiple estimation or procurement approaches
2. **🔍 Evaluation**: Compare accuracy, speed, risk allocation, and contractual implications
3. **🎯 Selection**: Recommend the optimal approach with cost-benefit analysis
4. **📋 Implementation**: Provide detailed BOQs, cost breakdowns, and formatted tables

## Response Guidelines:
- Always use structured tables for BOQs and cost breakdowns
- Include measurement rules and references to standards
- Provide unit rates with material, labor, and equipment breakdowns
- Apply appropriate contingencies and preliminaries percentages
- Reference current market rates and price indices
- Include formulas for escalation, retention, and variations""",
    },
}

PRESET_PROMPTS = {
    "🏛️ Revit API Helper": [
        "How do I create a FilteredElementCollector to get all walls in the active view?",
        "Write a pyRevit script to export room data to Excel",
        "How to create a custom Revit add-in with an External Command in C#?",
        "Explain how to use transactions and sub-transactions properly",
        "How to batch-modify element parameters using the Revit API?",
        "Create a Dynamo script to place families at specific coordinates",
    ],
    "🦺 Construction Safety Advisor": [
        "Create a Job Hazard Analysis for steel erection work",
        "What are OSHA requirements for fall protection above 6 feet?",
        "Develop a site-specific safety plan for excavation work",
        "List PPE requirements for concrete pouring operations",
        "How to conduct a safety audit for a commercial construction site?",
        "Create a toolbox talk on electrical safety in construction",
    ],
    "📐 BIM Standards Consultant": [
        "Create a BIM Execution Plan template for a commercial project",
        "Explain LOD 100 through LOD 500 with examples",
        "How to set up a Common Data Environment per ISO 19650?",
        "Design a clash detection workflow for MEP coordination",
        "What naming conventions should we use for Revit models?",
        "Create a model audit checklist for quality control",
    ],
    "📊 Quantity Surveyor Assistant": [
        "Prepare a BOQ for reinforced concrete foundation work",
        "Compare FIDIC vs NEC contract forms for infrastructure projects",
        "How to perform earned value analysis on a construction project?",
        "Create a cost estimate for a 3-story office building",
        "Explain the measurement rules in NRM2 for masonry work",
        "How to calculate preliminaries as a percentage of contract sum?",
    ],
}


# ──────────────────────────────────────────────
# Helper Functions
# ──────────────────────────────────────────────

def count_tokens(text: str) -> int:
    """Approximate token count using tiktoken cl100k_base encoding."""
    try:
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        # Fallback: rough estimate (1 token ≈ 4 chars)
        return len(text) // 4


def get_total_tokens() -> tuple[int, int]:
    """Calculate total input and output tokens from chat history."""
    input_tokens = 0
    output_tokens = 0
    for msg in st.session_state.get("messages", []):
        tokens = count_tokens(msg["content"])
        if msg["role"] == "user":
            input_tokens += tokens
        else:
            output_tokens += tokens
    return input_tokens, output_tokens


def export_chat_history() -> str:
    """Export chat history to a formatted markdown string."""
    if not st.session_state.get("messages"):
        return ""

    lines = [
        "# 💬 Chat History — Hazem El-Ashry AEC Assistant",
        f"**Exported**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Specialty**: {st.session_state.get('specialty', 'N/A')}",
        f"**Model**: {st.session_state.get('selected_model_name', 'N/A')}",
        f"**Temperature**: {st.session_state.get('temperature', 0.7)}",
        "",
        "---",
        "",
    ]

    for i, msg in enumerate(st.session_state.messages):
        role = "🧑 User" if msg["role"] == "user" else "🤖 Hazem El-Ashry"
        lines.append(f"### {role}")
        lines.append(msg["content"])
        lines.append("")
        lines.append("---")
        lines.append("")

    # Token summary
    in_tok, out_tok = get_total_tokens()
    lines.append(f"**Total Tokens** — Input: {in_tok:,} | Output: {out_tok:,} | Total: {in_tok + out_tok:,}")

    return "\n".join(lines)


def stream_response(api_key: str, model: str, messages: list, temperature: float):
    """Stream a response from the OpenRouter API, yielding chunks."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://hazem-el-ashry-aec-assistant.streamlit.app",
        "X-Title": "Hazem El-Ashry AEC Assistant",
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "stream": True,
    }

    try:
        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            stream=True,
            timeout=120,
        )

        if response.status_code != 200:
            error_detail = response.text
            yield f"⚠️ **API Error ({response.status_code})**: {error_detail}"
            return

        for line in response.iter_lines():
            if line:
                decoded = line.decode("utf-8")
                if decoded.startswith("data: "):
                    data_str = decoded[6:]
                    if data_str.strip() == "[DONE]":
                        break
                    try:
                        data = json.loads(data_str)
                        delta = data.get("choices", [{}])[0].get("delta", {})
                        content = delta.get("content", "")
                        if content:
                            yield content
                    except json.JSONDecodeError:
                        continue

    except requests.exceptions.Timeout:
        yield "⚠️ **Request timed out.** Please try again."
    except requests.exceptions.ConnectionError:
        yield "⚠️ **Connection error.** Check your internet connection."
    except Exception as e:
        yield f"⚠️ **Unexpected error**: {str(e)}"


# ──────────────────────────────────────────────
# Session State Initialization
# ──────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "specialty" not in st.session_state:
    st.session_state.specialty = list(SPECIALTIES.keys())[0]
if "selected_model_name" not in st.session_state:
    st.session_state.selected_model_name = list(FREE_MODELS.keys())[0]
if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7


# ──────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────

with st.sidebar:
    # Brand Header
    st.markdown("""
    <div class="brand-header">
        <div style="font-size:2.5rem; margin-bottom:0.3rem;">🏗️</div>
        <div class="brand-title">Hazem El-Ashry</div>
        <div class="brand-subtitle">AEC AI Assistant</div>
    </div>
    """, unsafe_allow_html=True)

    # ── API Configuration ──
    st.markdown("### 🔑 API Configuration")

    api_key = st.text_input(
        "OpenRouter API Key",
        type="password",
        placeholder="sk-or-v1-...",
        value=st.session_state.api_key,
        help="Enter your OpenRouter API key to start chatting.",
    )
    st.session_state.api_key = api_key

    st.markdown(
        '<a href="https://openrouter.ai/keys" target="_blank" class="openrouter-link">'
        '🔗 Get your free API key at OpenRouter</a>',
        unsafe_allow_html=True,
    )

    if api_key:
        st.markdown('<div class="token-badge">✅ API Key Configured</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="token-badge" style="color:#f59e0b; border-color:rgba(245,158,11,0.2); background:rgba(245,158,11,0.08);">⚠️ API Key Required</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # ── Specialty Selection ──
    st.markdown("### 🎯 Specialty")

    specialty = st.selectbox(
        "Choose your AEC domain",
        options=list(SPECIALTIES.keys()),
        index=list(SPECIALTIES.keys()).index(st.session_state.specialty),
        help="Select the domain expertise for the AI assistant.",
    )
    st.session_state.specialty = specialty

    spec_info = SPECIALTIES[specialty]
    st.markdown(
        f'<div class="status-card"><span style="font-size:0.82rem; color:var(--text-secondary);">'
        f'{spec_info["description"]}</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # ── Model Selection ──
    st.markdown("### 🤖 Model Selection")

    model_name = st.selectbox(
        "Choose a free model",
        options=list(FREE_MODELS.keys()),
        index=list(FREE_MODELS.keys()).index(st.session_state.selected_model_name),
        help="All models are free-tier from OpenRouter.",
    )
    st.session_state.selected_model_name = model_name

    st.markdown(
        f'<div class="status-card"><code style="font-size:0.72rem; color:#06b6d4; '
        f'font-family: JetBrains Mono, monospace;">{FREE_MODELS[model_name]}</code></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # ── Temperature Control ──
    st.markdown("### 🌡️ Temperature")

    temperature = st.slider(
        "Creativity level",
        min_value=0.0,
        max_value=2.0,
        value=st.session_state.temperature,
        step=0.1,
        help="Lower = more focused & deterministic. Higher = more creative & varied.",
    )
    st.session_state.temperature = temperature

    # Temperature label
    if temperature <= 0.3:
        temp_label = "🎯 Precise"
    elif temperature <= 0.7:
        temp_label = "⚖️ Balanced"
    elif temperature <= 1.2:
        temp_label = "🎨 Creative"
    else:
        temp_label = "🌋 Experimental"

    st.markdown(
        f'<div class="status-card"><span style="font-size:0.82rem; color:var(--text-secondary);">'
        f'{temp_label} — {temperature:.1f}</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # ── Token Counter ──
    st.markdown("### 📊 Token Usage")
    in_tokens, out_tokens = get_total_tokens()
    total_tokens = in_tokens + out_tokens
    msg_count = len(st.session_state.messages)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f'<div class="status-card"><div class="stat-value">{total_tokens:,}</div>'
            f'<div class="stat-label">Total Tokens</div></div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f'<div class="status-card"><div class="stat-value">{msg_count}</div>'
            f'<div class="stat-label">Messages</div></div>',
            unsafe_allow_html=True,
        )

    col3, col4 = st.columns(2)
    with col3:
        st.markdown(
            f'<div class="status-card"><div class="stat-value" style="font-size:1.1rem;">{in_tokens:,}</div>'
            f'<div class="stat-label">Input Tokens</div></div>',
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            f'<div class="status-card"><div class="stat-value" style="font-size:1.1rem;">{out_tokens:,}</div>'
            f'<div class="stat-label">Output Tokens</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # ── Actions ──
    st.markdown("### ⚡ Actions")

    # Export Chat
    chat_export = export_chat_history()
    if chat_export:
        st.download_button(
            label="📥 Export Chat History",
            data=chat_export,
            file_name=f"hazem_elashry_chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown",
            use_container_width=True,
        )

    # Clear Chat
    st.markdown('<div style="margin-top:0.5rem;"></div>', unsafe_allow_html=True)
    col_clear, _ = st.columns([1, 1])
    with col_clear:
        if st.button("🗑️ Clear Chat", use_container_width=True, key="clear_chat"):
            st.session_state.messages = []
            st.rerun()

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # ── Tree of Thoughts Badge ──
    st.markdown(
        '<div class="tot-badge">🌳 Tree of Thoughts Enabled</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="margin-top:0.8rem; font-size:0.72rem; color:var(--text-muted);">'
        'Built with ❤️ by Hazem El-Ashry<br>'
        'Powered by OpenRouter • Streamlit</div>',
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────
# Main Chat Area
# ──────────────────────────────────────────────

# Welcome screen (no messages yet)
if not st.session_state.messages:
    spec = SPECIALTIES[st.session_state.specialty]
    st.markdown(f"""
    <div class="welcome-card">
        <div class="welcome-icon">{spec["icon"]}</div>
        <div class="welcome-title">Welcome to Hazem El-Ashry</div>
        <div class="welcome-desc">
            Your AI-powered <strong>{st.session_state.specialty.split(' ', 1)[1]}</strong> assistant,
            enhanced with Tree of Thoughts reasoning for deeper, more structured analysis.
        </div>
        <div class="feature-grid">
            <div class="feature-pill">🌳 Tree of Thoughts</div>
            <div class="feature-pill">⚡ Streaming Responses</div>
            <div class="feature-pill">🎯 AEC Specialized</div>
            <div class="feature-pill">📊 Token Tracking</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Preset Prompts
    st.markdown("#### 💡 Quick Start — Preset Prompts")

    presets = PRESET_PROMPTS.get(st.session_state.specialty, [])
    cols = st.columns(2)
    for i, preset in enumerate(presets):
        with cols[i % 2]:
            if st.button(
                preset,
                key=f"preset_{i}",
                use_container_width=True,
            ):
                st.session_state.messages.append({"role": "user", "content": preset})
                st.rerun()

# Display Chat History
for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🏗️"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])
        # Show token count per message
        tok_count = count_tokens(message["content"])
        st.markdown(
            f'<div class="token-badge">🔢 {tok_count:,} tokens</div>',
            unsafe_allow_html=True,
        )


# ──────────────────────────────────────────────
# Chat Input & Response
# ──────────────────────────────────────────────

if prompt := st.chat_input("Ask Hazem El-Ashry anything about AEC..."):
    if not st.session_state.api_key:
        st.error("⚠️ Please enter your OpenRouter API key in the sidebar to start chatting.")
        st.stop()

    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)
        tok_count = count_tokens(prompt)
        st.markdown(
            f'<div class="token-badge">🔢 {tok_count:,} tokens</div>',
            unsafe_allow_html=True,
        )

    # Build conversation payload for API
    system_prompt = SPECIALTIES[st.session_state.specialty]["system_prompt"]
    api_messages = [{"role": "system", "content": system_prompt}]

    for msg in st.session_state.messages:
        api_messages.append({"role": msg["role"], "content": msg["content"]})

    # Stream assistant response
    with st.chat_message("assistant", avatar="🏗️"):
        response_placeholder = st.empty()
        token_placeholder = st.empty()

        full_response = ""
        model_id = FREE_MODELS[st.session_state.selected_model_name]

        for chunk in stream_response(
            api_key=st.session_state.api_key,
            model=model_id,
            messages=api_messages,
            temperature=st.session_state.temperature,
        ):
            full_response += chunk
            # Streaming display — update line by line
            response_placeholder.markdown(full_response + "▌")

        # Final render without cursor
        response_placeholder.markdown(full_response)

        # Token count for response
        resp_tokens = count_tokens(full_response)
        token_placeholder.markdown(
            f'<div class="token-badge">🔢 {resp_tokens:,} tokens</div>',
            unsafe_allow_html=True,
        )

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.rerun()
