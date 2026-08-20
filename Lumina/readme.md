# Lumina

A single-agent CrewAI pipeline that reads a meeting or call transcript and produces a structured summary — decisions made, deadlines mentioned, action items with owners, and open questions.

## Architecture

```
  transcript.txt
        │
        ▼
 ┌──────────────────┐   FileReadTool   ┌──────────────────────────────┐
 │ Summarizer Agent │ ───────────────► │ tasks_outputs/summary.json    │
 └──────────────────┘                  └──────────────────────────────┘
```

A single agent reads the transcript directly off disk via CrewAI's `FileReadTool`, then produces a structured summary in one pass.

## The agent

| Agent | Role | Tools | Job |
|---|---|---|---|
| **Summarizer** | Transcript summarizer | `FileReadTool` | Reads `transcript.txt` and produces a structured summary broken into sections: overview, key decisions, deadlines, action items with owners, and open questions raised during the meeting. |

The agent is explicitly instructed to only summarize what's actually in the transcript — no outside information, no invented details — and to keep sensitive information out of the output.

## Stack

- [CrewAI](https://github.com/crewAIInc/crewAI) — single-agent task execution
- LLM access via [OpenRouter](https://openrouter.ai/)
- `python-dotenv` for configuration

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in this folder:
   ```
   OR_API=your_openrouter_api_key
   model=your_openrouter_model_string
   base_url=https://openrouter.ai/api/v1
   ```
3. Replace the contents of `transcript.txt` with the transcript you want summarized.
4. Run it:
   ```bash
   python main.py
   ```
   The structured summary prints to the console and is saved to `tasks_outputs/summary.json`.

## Reliability details

- The agent is capped at `max_iter=1` (one reasoning pass, no open-ended looping) and `max_rpm=3` to keep API usage predictable on longer transcripts.
- Output is explicitly required to be split into multiple clearly labeled sections (one topic per section) rather than a single unstructured paragraph, so the summary stays scannable regardless of transcript length.

## Possible extensions

Since this reads from a single local `.txt` file, a natural next step would be accepting transcripts from an uploaded file or an API (e.g., a call-recording service) rather than a hardcoded path — turning it from a script into something that could sit behind an endpoint.
