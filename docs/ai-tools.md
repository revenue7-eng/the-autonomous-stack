---
title: "AI Tools"
nav_order: 3
---

# AI Tools

AI is where autonomy gets lost fastest — and where the difference between control and dependence is one architectural decision. Every tool below can run without sending your data to someone else's server.

Most AI tools exist in two modes: hosted (convenient, dependent) and self-hosted (requires effort, sovereign). TAS scores both. A low score is not a criticism — it is a measurement of what you trade for convenience.

Training a model costs millions. Companies need to recoup that investment — hosted APIs are how. That's not a flaw, it's economics. But **you** should know exactly what you're paying: money, or control.

{: .note }
> Unlike most software categories, AI gives you a real choice. The same model that runs behind a $20/month API can often run on your own hardware for free. TAS makes that difference visible.

---

## Choose Your Level

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:24px 0;">

<div style="border:2px solid #2ea043;border-radius:12px;padding:20px;">
<div style="font-size:20px;margin-bottom:8px;">🟢 Use Local Models</div>
<div style="font-size:14px;color:#666;">Install Ollama or LM Studio. Run open-weight models on your own machine. Your prompts never leave your device. No account needed.</div>
</div>

<div style="border:2px solid #d29922;border-radius:12px;padding:20px;">
<div style="font-size:20px;margin-bottom:8px;">🟡 Self-Host the Stack</div>
<div style="font-size:14px;color:#666;">Run Ollama + Open WebUI on your server. Add Whisper for speech, SearXNG for search. Multi-user, full control, ChatGPT-like experience.</div>
</div>

<div style="border:2px solid #da3633;border-radius:12px;padding:20px;">
<div style="font-size:20px;margin-bottom:8px;">🔴 Full Sovereign AI</div>
<div style="font-size:14px;color:#666;">Air-gapped inference. No internet. Models on local storage, custom fine-tuning, own hardware. Maximum autonomy — requires GPU investment.</div>
</div>

</div>

---

## The Two-Mode Problem

Almost every AI product exists in two configurations — and the TAS score changes dramatically between them:

| Tool | Self-hosted | Hosted |
|------|------------|--------|
| MiroThinker | A3/T2 (open weights, run locally) | A1/T1 (hosted app, account required) |
| Ollama models | A3/T2 (your hardware) | — |
| ChatGPT | — | A0/T0 (cloud-only, proprietary) |
| Whisper | A3/T2 (run locally) | A0/T0 (OpenAI API) |
| Stable Diffusion | A3/T2 (ComfyUI local) | A0/T0 (cloud services) |

This is not a bug — it's the core insight. **The same intelligence, radically different autonomy.**

---

## Inference Engines

The runtime that loads and serves models on your hardware.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin:16px 0;">

<a href="{{ '/docs/catalog/ollama' | relative_url }}.html" style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;text-decoration:none;color:inherit;">
<div style="font-size:16px;font-weight:600;">Ollama</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: ChatGPT, Claude API</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">One-command install, OpenAI-compatible API. The Docker of LLMs. Pull a model, run it, done.</div>
</a>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">llama.cpp</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: cloud inference APIs</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">The foundation. C++ inference engine that runs on CPU and GPU. Maximum control, minimum abstraction.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">vLLM</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: hosted inference APIs</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Production-grade GPU serving with PagedAttention. High throughput for multi-user deployments.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">LocalAI</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: OpenAI API</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Drop-in OpenAI API replacement. Supports text, image, audio generation. One binary, no GPU required.</div>
</div>

</div>

---

## Chat Interfaces

Give your local models a usable frontend.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin:16px 0;">

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">Open WebUI</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: ChatGPT interface</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Self-hosted ChatGPT-like UI. Connects to Ollama or any OpenAI-compatible API. Multi-user, RAG, web search built in.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">LM Studio</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: ChatGPT desktop</div>
<div style="font-size:13px;color:#58a6ff;font-weight:600;">A3/T1</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Desktop app for running local models. Beautiful UI, model discovery, chat. Free but closed-source.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">Jan</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: ChatGPT desktop</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Open-source desktop AI. Runs models locally, no internet needed. AGPL-3.0 licensed.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">GPT4All</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: ChatGPT</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Desktop app from Nomic. Local chat, document Q&A. Optimized for consumer hardware.</div>
</div>

</div>

---

## Reasoning & Research Models

Open-weight models designed for deep reasoning and agentic research.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin:16px 0;">

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">MiroThinker</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: OpenAI Deep Research</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2 (self-hosted) · A1/T1 (hosted)</div>
<div style="font-size:13px;color:#666;margin-top:6px;">30B/235B reasoning model from MiroMind. Verification-centric architecture. Open weights on HuggingFace, run via vLLM/SGLang. Hosted app exists but requires account.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">DeepSeek-R1</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: o1, Claude reasoning</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2 (self-hosted) · A1/T1 (hosted)</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Open-weight reasoning model. Chain-of-thought visible. Run locally via Ollama (distilled versions) or through DeepSeek API.</div>
</div>

</div>

---

## Speech & Audio

Local speech-to-text and text-to-speech.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin:16px 0;">

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">Whisper.cpp</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: Google Speech-to-Text, Otter.ai</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">OpenAI's Whisper model, ported to C++. Runs on CPU. Transcribe audio locally — no data leaves your machine.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">Piper</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: Google TTS, ElevenLabs</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Fast local text-to-speech. Multiple languages, natural voices. Runs on Raspberry Pi.</div>
</div>

</div>

---

## Image Generation

Local image generation and editing.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin:16px 0;">

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">ComfyUI</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: Midjourney, DALL-E</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Node-based UI for Stable Diffusion and other image models. Full local workflow — generate, edit, upscale. No cloud.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;">
<div style="font-size:16px;font-weight:600;">AUTOMATIC1111</div>
<div style="font-size:12px;color:#888;margin:4px 0;">→ Replaces: Midjourney, DALL-E</div>
<div style="font-size:13px;color:#2ea043;font-weight:600;">A3/T2</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Web UI for Stable Diffusion. The original self-hosted image generation interface. Huge extension ecosystem.</div>
</div>

</div>

---

## Hosted Services (for comparison)

These are the services that self-hosted AI replaces. Included for contrast — not as recommendations.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin:16px 0;">

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;opacity:0.7;">
<div style="font-size:16px;font-weight:600;">ChatGPT / OpenAI API</div>
<div style="font-size:13px;color:#da3633;font-weight:600;">A0/T0</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Cloud-only. Proprietary models. All prompts and data processed on OpenAI servers. Cannot self-host. Cannot export model.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;opacity:0.7;">
<div style="font-size:16px;font-weight:600;">Claude API</div>
<div style="font-size:13px;color:#da3633;font-weight:600;">A0/T0</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Cloud-only. Proprietary models by Anthropic. No self-hosted option. Data processed on Anthropic/cloud infrastructure.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;opacity:0.7;">
<div style="font-size:16px;font-weight:600;">Google Gemini</div>
<div style="font-size:13px;color:#da3633;font-weight:600;">A0/T0</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Cloud-only. Google infrastructure. Gemma models are open-weight (A3/T2 when self-hosted), but Gemini API is not.</div>
</div>

<div style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;opacity:0.7;">
<div style="font-size:16px;font-weight:600;">Midjourney</div>
<div style="font-size:13px;color:#da3633;font-weight:600;">A0/T0</div>
<div style="font-size:13px;color:#666;margin-top:6px;">Cloud-only image generation. Discord-based interface. No self-hosted option. No open model.</div>
</div>

</div>

---

## What's Next

Set up local AI? Here's where to go deeper:

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:16px 0;">

<a href="{{ '/docs/recommended-stack' | relative_url }}.html" style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;text-decoration:none;color:inherit;">
<div style="font-size:14px;font-weight:600;">Recommended Server Stack</div>
<div style="font-size:12px;color:#666;">→ build the full backend</div>
</a>

<a href="{{ '/docs/recipes/' | relative_url }}" style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;text-decoration:none;color:inherit;">
<div style="font-size:14px;font-weight:600;">All Recipes</div>
<div style="font-size:12px;color:#666;">→ deploy complete stacks</div>
</a>

<a href="{{ '/docs/audit' | relative_url }}.html" style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;text-decoration:none;color:inherit;">
<div style="font-size:14px;font-weight:600;">Audit Your Setup</div>
<div style="font-size:12px;color:#666;">→ score any technology</div>
</a>

<a href="{{ '/docs/catalog/' | relative_url }}" style="display:block;border:1px solid #d0d7de;border-radius:10px;padding:16px;text-decoration:none;color:inherit;">
<div style="font-size:14px;font-weight:600;">Full Catalog</div>
<div style="font-size:12px;color:#666;">→ 122+ technologies evaluated</div>
</a>

</div>

<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:24px;">
<a href="{{ '/docs/recommended-stack' | relative_url }}.html" style="font-size:13px;font-weight:500;color:#333;background:#f4f4f2;border:1px solid #e0e0e0;border-radius:6px;padding:8px 16px;text-decoration:none;">Recommended Stack →</a>
<a href="{{ '/docs/recipes/' | relative_url }}" style="font-size:13px;font-weight:500;color:#333;background:#f4f4f2;border:1px solid #e0e0e0;border-radius:6px;padding:8px 16px;text-decoration:none;">Recipes →</a>
<a href="{{ '/docs/catalog/' | relative_url }}" style="font-size:13px;font-weight:500;color:#333;background:#f4f4f2;border:1px solid #e0e0e0;border-radius:6px;padding:8px 16px;text-decoration:none;">Full catalog →</a>
<a href="{{ '/docs/card-builder' | relative_url }}.html" style="font-size:13px;font-weight:500;color:#333;background:#f4f4f2;border:1px solid #e0e0e0;border-radius:6px;padding:8px 16px;text-decoration:none;">Suggest a technology →</a>
</div>
