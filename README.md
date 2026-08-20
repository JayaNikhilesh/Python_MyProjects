# Python_MyProjects

A collection of multi-agent AI systems built with [CrewAI](https://github.com/crewAIInc/crewAI), each solving a different content-processing problem — from live web research to meeting transcript summarization.

Both projects share the same underlying pattern: **agents with narrowly defined roles, connected in sequence, each handing off structured output to the next stage** — rather than one agent trying to do everything at once.

## Projects

### [Veritas AI](./Veritas%20AI) — 3-agent research & content pipeline
Give it a topic. A researcher agent finds trending keywords and articles via live web search, a writer agent drafts a blog post from that research, and an editor agent refines it for readability and SEO — each stage's output saved to disk along the way.

**Agents:** Researcher → Writer → Editor
**Key integration:** Exa search API for live web research

### [Lumina](./Lumina) — single-agent transcript summarizer
Give it a meeting transcript. One agent reads it and produces a structured summary — key decisions, deadlines, action items with owners, and open questions — split into clearly labeled sections.

**Agents:** Summarizer
**Key integration:** File-based transcript ingestion

## Why these are structured this way

Both pipelines are built around the same core discipline: **narrow agent roles + explicit task instructions + rate/iteration limits**, rather than one broad "do everything" agent. Each agent has:
- A single, specific job (research *or* write *or* edit — not all three)
- Explicit constraints in its task description (what counts as a valid output, what to avoid, how to handle edge cases like missing data or sensitive information)
- Capped reasoning iterations (`max_iter=1`) and per-agent rate limits, so runs stay fast and predictable instead of looping indefinitely

This structure came out of real debugging — earlier versions of these pipelines had issues like agents re-reasoning far more than needed, or one misconfigured parameter silently controlling two unrelated things. The current structure reflects those fixes.

## Common stack across both

- Python
- [CrewAI](https://github.com/crewAIInc/crewAI) — multi-agent orchestration
- LLM access via [OpenRouter](https://openrouter.ai/)
- `python-dotenv` for environment configuration

## Setup

Each project is self-contained with its own `requirements.txt` and `.env` configuration — see the individual READMEs linked above for exact setup steps. General pattern:

```bash
cd "Veritas AI"        # or cd Lumina
pip install -r requirements.txt
# create a .env file with the required API keys (see project README)
python main.py
```

## About

Built by Koutharapu Jaya Nikhilesh, B.Tech Information Technology, as part of ongoing work in AI agent development and multi-agent system design.
