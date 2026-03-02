# Contributing to vigil-community-attacks

## How to add a snapshot

1. Find a real attack technique (paper, incident, researcher writeup)
2. Create a `.bp.json` file in the correct technique folder
3. Verify the snapshot:
   - Run it against a vulnerable prompt -> test should FAIL (attack succeeds)
   - Run it against a hardened prompt -> test should PASS (attack blocked)
4. Update `manifest.json`
5. Open a PR with attribution in the `source` field

## Sanitization requirements

Before submitting:
- No real production system prompts
- No real credentials or API keys
- No identifying information about the affected organization
- Replace real strings with clearly fictional examples

## Attribution

Always credit the original researcher or paper in the `source` field.
If you discovered the technique yourself, use `source: "original research"`.

## Technique taxonomy

| Technique | When to use |
|---|---|
| `direct_injection` | User directly instructs model to override system prompt |
| `indirect_rag` | Attack payload embedded in retrieved/external content |
| `prompt_leakage` | Attack goal is extracting system prompt contents |
| `multi_turn` | Attack requires multiple conversation turns to succeed |
| `agent_hijacking` | Attack targets agent orchestration or tool interfaces |
| `tool_injection` | Attack payload delivered via tool/API response |
| `jailbreak` | Attack bypasses model safety via framing or obfuscation |
