# AEC AI Assistant

A Streamlit chat interface for Architecture, Engineering, and Construction (AEC) questions. It sends streamed chat-completion requests to OpenRouter using an API key supplied by the user.

## Features

- Four selectable prompt profiles: Revit API Helper, Construction Safety Advisor, BIM Standards Consultant, and Quantity Surveyor Assistant.
- A source-defined menu of 12 OpenRouter model IDs.
- Streamed responses in the chat interface.
- Temperature control and session-local conversation history.
- Preset prompts for each AEC profile.
- Clear-chat and Markdown export controls.
- Approximate input and output token counts using `tiktoken`, with a character-count fallback.
- Password-masked OpenRouter API-key input.

## How it works

```text
User-provided OpenRouter key
            │
            v
Streamlit UI -> selected specialty prompt + session messages
            │
            v
OpenRouter chat-completions API (streaming)
            │
            v
Rendered response + approximate local token count
```

The specialty profiles are prompt templates, not separate reasoning engines or connected professional knowledge bases. Responses can be incomplete or incorrect and should be checked against current project requirements, official documentation, regulations, standards, and qualified professional advice.

## Setup

Prerequisites:

- A Python environment compatible with the versions in `requirements.txt`.
- An [OpenRouter API key](https://openrouter.ai/keys) supplied by the user.

Clone and install:

```bash
git clone https://github.com/hazzemmohammed33-cmd/aec-ai-assistant.git
cd aec-ai-assistant
python -m venv .venv
```

Activate the environment for your shell, then run:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Paste your OpenRouter API key into the password-masked field in the sidebar. The current application reads the key from that field; `.env.example` documents the variable name but `app.py` does not automatically load a `.env` file.

## Model availability and pricing

The model IDs in `app.py` are configuration choices, not availability or pricing guarantees. OpenRouter controls model access, routing, rate limits, and pricing, and those details can change. Review the current model page and account settings on OpenRouter before use. The user is responsible for provider terms and any charges.

## Project structure

```text
aec-ai-assistant/
├── app.py                  Streamlit application and prompt configuration
├── requirements.txt        Python dependencies
├── .env.example            API-key variable example
├── .streamlit/config.toml  Streamlit theme and server settings
├── .gitignore              Local environment and secret exclusions
└── README.md               Project documentation
```

## Security and limitations

- Never commit an OpenRouter API key. `.env` and `.streamlit/secrets.toml` are ignored by Git.
- The key is used by the Streamlit process to authenticate requests to OpenRouter.
- Conversation history is stored only in the current Streamlit session and is cleared when the session resets.
- Exported token counts are local approximations, not provider billing or usage records.
- The repository currently has no automated test suite or CI workflow.
- Model output is not a substitute for project-specific validation or professional review.

## Technology

- Python
- Streamlit
- OpenRouter chat-completions API
- Requests
- tiktoken

## Roadmap

Planned work:

- Add automated coverage for prompt selection, session-state migration, API payload construction, streaming responses, and error handling.
- Add continuous integration for syntax, lint, and test checks.
- Review configured model IDs periodically and improve handling for provider-side availability changes without promising access or pricing.
- Document optional deployment and secret-management workflows after they are implemented and verified.

## Author

Hazem Mohamed

- [GitHub](https://github.com/hazzemmohammed33-cmd)
- [LinkedIn](https://www.linkedin.com/in/hazem-mohamed-aec/)
