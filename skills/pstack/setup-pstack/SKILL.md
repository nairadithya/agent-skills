---
name: setup-pstack
description: Configure Pi subagent models and reasoning levels for pstack roles. Use for `/skill:setup-pstack` or when changing pstack's model routing.
---

# Set up pstack models in Pi

Configure `subagents.agentOverrides` in `~/.pi/agent/settings.json`. Pi project settings in `.pi/settings.json` override user settings for that project.

## Check available models and current settings

1. Read `~/.pi/agent/settings.json` and the current project's `.pi/settings.json`, if present. Preserve unrelated settings.
2. Run `pi --list-models` to confirm model availability. Use fully qualified IDs in `provider/model` form.
3. Run `/subagents-models` in Pi to inspect the effective live role mapping. Settings changes apply after Pi reloads or starts a new session.

## Use these pstack role defaults

| Pi agent | Model | Thinking | Work |
|---|---|---|---|
| `scout` | `openai/gpt-6-luna` | `low` | Recon and bounded lookup |
| `worker` | `openai/gpt-6-luna` | `medium` | Routine implementation and approved nested fan-out |
| `delegate` | `openai/gpt-6-luna` | `medium` | Small bounded handoff |
| `poteto-agent` | `openai/gpt-6-luna` | `medium` | Full pstack-style task with nested fan-out |
| `comment-sicko` | `openai/gpt-6-luna` | `medium` | Scoped comment audit |
| `researcher` | `openai/gpt-6-luna` | `medium` | Focused research |
| `reviewer` | `openai/gpt-6.1-sol` | `high` | Read-only inspection of code and verification receipts |
| `verifier` | `openai/gpt-6-luna` | `medium` | Executes project checks with shell and available ambient project tools; does not post verdicts |
| `oracle` | `openai/gpt-6.1-sol` | `xhigh` | Rare, difficult read-only critique |

Use `gpt-6-luna` for routine, well-scoped work. Use `gpt-6.1-sol` for the primary independent review and difficult reasoning. Keep `xhigh` for a bounded oracle task, not routine implementation. These are defaults, not claims that one model wins every task.

## Nested fan-out grants

Only the workflow-owning `worker` and `poteto-agent` roles may fan out. The built-in `worker` grant is `allowNestedSubagents: true` in `subagents.agentOverrides`; `poteto-agent` declares the same flag in its user agent file at `~/.pi/agent/skills/pstack/agents/poteto-agent.md`. All other roles remain without a nesting grant. This supplies the child-safe `subagent` runtime without replacing the built-in worker's normal tool allowlist.

Keep pi-subagents' default `maxSubagentDepth` of 2. A root can launch one owner, and that owner can fan out once; descendants cannot recurse past the inherited cap. Do not raise the global depth unless a concrete workflow needs a deeper chain and has an explicit safety review. Higher-priority project policy or runtime ceilings can still deny nesting.

## Add model-family diversity per run

Keep the persistent role defaults above. For a second opinion or model race, use the `model` per-run override on the `runs.run`/`runs.all` item; do not replace the default `reviewer` mapping or silently change models after launch. Explicitly suffix every alternate model with `:medium`. A child otherwise inherits the selected role's thinking level, so this suffix prevents a DeepSeek reviewer from inheriting `high` or another role from inheriting its own setting. If the provider rejects the explicit level, report the launch failure; do not silently retry without it.

Use `opencode-go/deepseek-v4.1-flash:medium` for frequent second opinions and exploration. Use `opencode-go/minimax-m3:medium` for alternate implementation or design candidates. Use `opencode-go/kimi-k2.7-code:medium` for additional independent review. Reserve `opencode-go/kimi-k3:medium` for occasional difficult comparisons given its lower supplied request allowance. These are starting routing choices, not measured quality rankings. Use only these four OpenCode models unless the operator changes the pool. Preserve `openai/gpt-6.1-sol` as the primary reviewer.

### Operator-approved OpenCode pool

The operator supplied these estimated requests per five hours on October 19, 2026. They are not measured throughput, verified prices, or quality scores. Multiple values are retained without assigning plan tiers because the pasted table did not identify the tiers unambiguously. Promotional multipliers, regional restrictions, and allowances can change. Confirm the account's allowance before scheduling substantial work.

| Exact model ID | Supplied request estimates per five hours |
|---|---:|
| `opencode-go/deepseek-v4.1-flash` | 34,670; 69,330 |
| `opencode-go/minimax-m3` | 3,200; 9,600 |
| `opencode-go/kimi-k2.7-code` | 1,350; 4,050 |
| `opencode-go/kimi-k3` | 110; 440 |

Add these exact IDs to `enabledModels` alongside the existing OpenAI entries to make the pool selectable. `enabledModels` controls startup selection and model cycling. It does not assign subagent roles or enforce a provider allowlist. Keep `subagents.agentOverrides` unchanged unless the operator also requests new default roles. Listing a model in the registry does not prove authentication works. Resolve a reported expired OpenCode API key before launching provider probes or alternate-model work.

## Write the settings

Merge the role values into the existing `subagents.agentOverrides` object. Do not overwrite the rest of the settings file. Use this shape:

```json
{
  "subagents": {
    "defaultThinking": "medium",
    "agentOverrides": {
      "scout": { "model": "openai/gpt-6-luna", "thinking": "low" },
      "worker": { "model": "openai/gpt-6-luna", "thinking": "medium", "allowNestedSubagents": true },
      "delegate": { "model": "openai/gpt-6-luna", "thinking": "medium" },
      "poteto-agent": { "model": "openai/gpt-6-luna", "thinking": "medium" },
      "comment-sicko": { "model": "openai/gpt-6-luna", "thinking": "medium" },
      "researcher": { "model": "openai/gpt-6-luna", "thinking": "medium" },
      "reviewer": { "model": "openai/gpt-6.1-sol", "thinking": "high" },
      "verifier": { "model": "openai/gpt-6-luna", "thinking": "medium" },
      "oracle": { "model": "openai/gpt-6.1-sol", "thinking": "xhigh" }
    }
  }
}
```

Keep project-specific changes in `.pi/settings.json` only when the project needs different routing. Do not claim that skill instructions switch models automatically.

## Verify

Run `/subagents-models` after reloading Pi. Confirm each role resolves to the configured provider, model, and thinking level. If a role is unavailable or a model fails to resolve, report the exact error and do not silently substitute another model.
