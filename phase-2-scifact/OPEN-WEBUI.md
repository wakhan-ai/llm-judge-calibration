# Open WebUI and OpenRouter setup

## Recorded Windows smoke test

On 26 November 2026, Open WebUI 0.13.5 was available at `http://127.0.0.1:8080` on Windows. An OpenAI-compatible connection pointed to `https://openrouter.ai/api/v1`. Selecting **inclusionAI: Ling 3.2 Flash (free)** and sending a short connectivity prompt produced the reply “OpenRouter connection works.” This records a successful interactive provider round trip. Benchmark inference and API automation still require validation.

## Recreate the local setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and open a fresh PowerShell session.
2. Choose a private persistent data directory and start the pinned WebUI version. Use your existing data directory if it already contains the configured instance. The original installation command and data directory were not recorded with the smoke test.

```powershell
$env:DATA_DIR = Join-Path $env:LOCALAPPDATA 'scifact-open-webui'
uvx --python 3.12 open-webui@0.13.5 serve --host 127.0.0.1 --port 8080
```

3. Open `http://127.0.0.1:8080` and create or sign in to the local administrator account.
4. In the admin panel, open **Settings → Connections**, add an **OpenAI API** connection and select **Chat Completions**. Use `https://openrouter.ai/api/v1` and enter a key created in [OpenRouter](https://openrouter.ai/settings/keys). Add `inclusionai/ling-3.2-flash:free` to the model allowlist. Verify and save the connection.
5. Select that model in a new chat, disable optional tools or knowledge collections, and send `Reply with exactly: OpenRouter connection works`. Record the configured ID, displayed model, WebUI version, time in UTC, response, and any provider metadata available. Free model availability and routing can change. Record any substitution before using it on benchmark cases.
6. Restart with the same data directory to retain the connection. Keep keys, WebUI databases, authentication headers, and private chat exports out of Git. A connection verification error can come from model discovery. Check the allowlist and run a chat smoke test. A 401 suggests checking the key and connection URL, and a 429 calls for checking provider limits and logging the failed attempt.

## Move from chat to a repeatable run

Use the UI to inspect a single example and confirm prompt formatting. For the paired pilot, use stateless API requests. If using Open WebUI as the gateway, enable API keys in the admin settings and create a separate WebUI key under the run account. The WebUI key goes to the local server. The OpenRouter key stays in the provider connection. Read the exposed model ID from `GET /api/v1/models` and call `POST /api/v1/chat/completions` on the same host with that ID and `stream: false`. Verify the API response on one sample and record the effective settings before freezing the pilot.

Prepare the top-five evidence packet once per claim with stable document and sentence IDs. Send the same packet with each prompt condition in a fresh request. Log claim ID, packet hash, prompt hash, requested and returned model identifiers, decoding settings, UTC timestamp, latency, status and raw output. Keep gold labels in a separate scoring file. Apply the protocol’s validity checks and review rules before calculating metrics. Record any provider retry and rate limit separately from judge errors. Follow the [experiment protocol](PROTOCOL.md) for split design, controls and outcome definitions.

References: [Open WebUI installation](https://docs.openwebui.com/getting-started/quick-start/), [provider connections](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible/), [API endpoints](https://docs.openwebui.com/reference/api-endpoints/), [OpenRouter model catalog](https://openrouter.ai/inclusionai).
