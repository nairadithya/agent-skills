---
name: make-bot-ui
description: "Blocked in Pi unless an external bot service supplies a webhook API, authentication contract, and secret-management path. Do not use as an executable Pi workflow yet."
disable-model-invocation: true
---

# Make a bot UI

This workflow is not ported. Its previous implementation depended on an external routine-creation tool, a service-specific webhook URL and authorization scheme, and a secure secret-request UI. Pi and `pi-subagents` do not provide those services.

Do not guess a webhook provider, endpoint, request headers, key flow, or bot wake semantics. To port this workflow, the user must provide or install an integration that documents:

- A supported API to create or select a bot routine.
- The webhook URL and exact request authentication contract.
- A secure way to provision and store the sender key outside the browser and chat.
- A way to receive and validate webhook events.
- The hosting and network-access requirements for the UI.

Until those facts exist, do not claim that a page can wake a bot. Use only a user-provided, independently verified webhook contract for a new implementation.
