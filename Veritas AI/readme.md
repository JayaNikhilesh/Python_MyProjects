# Veritas AI

A 3-agent content pipeline built with **CrewAI**. Give it a topic, and three agents work in sequence — research, write, edit — to produce a publish-ready blog post, with each stage's output saved to disk.

## Architecture

```
   topic (user input)
         │
         ▼
  ┌─────────────┐   EXA Search API   ┌──────────────────────────────┐
  │  Researcher │ ─────────────────► │ tasks_outputs/article_data.md │
  └─────────────┘                    └──────────────────────────────┘
         │
         ▼
  ┌─────────────┐  DocumentWriterTool  ┌────────────────────────┐
  │   Writer    │ ───────────────────► │ tasks_outputs/blogs.md │
  └─────────────┘                      └────────────────────────┘
         │
         ▼
  ┌─────────────┐  DocumentWriter +   ┌──────────────────────────────┐
  │   Editor    │  ContentRefiner     │ tasks_outputs/final_blog.md   │
  └─────────────┘ ──────────────────► └──────────────────────────────┘
```

Each agent receives the previous agent's output as context (`context=[...]` in CrewAI's `Task`), so the pipeline runs as one connected chain rather than three isolated scripts.

## The agents

| Agent | Role | Tools | Job |
|---|---|---|---|
| **Researcher** | Online summarizer | `EXASearchTool` | Finds top trending keywords and articles on the given topic via the Exa search API. Instructed to only use officially confirmed sources and never leak API keys in its output. |
| **Writer** | Blog writer | `DocumentWriterTool` | Turns the researcher's findings into a readable blog post — instructed to keep it factual, engaging, and free of unofficial or unverified claims. |
| **Editor** | Context editor | `DocumentWriterTool`, `ContentRefinerTool` | Refines the draft for readability and keyword density, and adds metadata — the final polish pass before publishing. |

## Custom tools

Two of the tools (`DocumentWriterTool`, `ContentRefinerTool`) are custom `BaseTool` subclasses built specifically for this pipeline, not off-the-shelf CrewAI tools:

- **`DocumentWriterTool`** — formats agent output into structured text for the next stage.
- **`ContentRefinerTool`** — cleans and normalizes raw text before it's finalized.

The third, **`EXASearchTool`**, comes from `crewai-tools` and is configured with an Exa API key for live web search.

## Stack

- [CrewAI](https://github.com/crewAIInc/crewAI) — multi-agent orchestration (sequential process)
- LLM access via [OpenRouter](https://openrouter.ai/)
- [Exa](https://exa.ai/) search API for research
- `python-dotenv` for configuration

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in this folder:
   ```
   OR_API=your_openrouter_api_key
   EXA_API=your_exa_api_key
   model=your_openrouter_model_string
   ```
3. Run it:
   ```bash
   python main.py
   ```
   You'll be prompted for a topic. The crew researches, writes, and edits in sequence — the finished post lands in `tasks_outputs/final_blog.md`, with the intermediate research and draft saved alongside it for inspection.

## Reliability details

- Each agent is capped at `max_iter=1` — one reasoning pass per task, keeping runs fast and predictable rather than letting agents loop indefinitely.
- Per-agent rate limits (`max_rpm`) are tuned individually — the researcher and editor run faster (5 rpm) since their calls are lighter, while the writer is capped lower (2 rpm) since generation calls are heavier.
- `test.py` is a standalone script to confirm your API keys are loading correctly from `.env` *before* running the full crew — useful for catching config issues early instead of mid-run.

## What this isn't (yet)

This pipeline researches and drafts content — it does not cross-reference multiple sources against each other or verify factual claims against a ground truth. That would be a natural next step if the project's scope expands toward genuine fact-checking.
