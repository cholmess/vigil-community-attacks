# vigil-community-attacks

Community snapshot pack for Vigil prompt-injection and agent-attack testing.

## Contents

- 50 snapshot files (`.bp.json`)
- 7 technique categories
- Deterministic `manifest.json` generation via `generate_manifest.py`

## Snapshot counts

| Technique | Count |
|---|---:|
| `direct_injection` | 11 |
| `indirect_rag` | 10 |
| `prompt_leakage` | 7 |
| `multi_turn` | 6 |
| `jailbreak` | 6 |
| `agent_hijacking` | 5 |
| `tool_injection` | 5 |
| **Total** | **50** |

## Structure

```text
vigil-community-attacks/
├── README.md
├── CONTRIBUTING.md
├── manifest.json
├── generate_manifest.py
└── snapshots/
```

## Usage

```bash
python3 generate_manifest.py
```

`__CURRENT_SYSTEM_PROMPT__` is a required placeholder in each snapshot and is replaced at runtime by Vigil.
