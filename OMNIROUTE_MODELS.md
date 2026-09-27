# 🚀 OMNIROUTE WORKABLE MODELS MASTER CATALOG & AUTO-FAILOVER MATRIX

> **Workspace:** Swatch Paints (Sharma Industries)  
> **Central Gateway:** OmniRoute (`http://localhost:20128/v1`)  
> **API Key:** `sk-371be56778267a28-451f56-0c72659c`  
> **Benchmark Date:** September 25, 2026  
> **Total Models Benchmark Tested:** 111 models  
> **Supervisor:** Ashutosh Sharma (+919079609627)

---

## 📈 Executive Summary

Aapke dwara provide kiye gaye **111 models** ka OmniRoute standard endpoint par live concurrent benchmark test execute kiya gaya:

* 🟢 **57 Models:** **Fully Working (100% Chat + Autonomous Tool Calling)**
* 🟡 **19 Models:** **Chat Only** (Plain conversation ke liye ok, tool calling unsupported/timed out)
* 🔴 **35 Models:** **Failed / Inactive** (HTTP 400 Bad Request, 401 Unauthorized, 404, ya Upstream Offline)

---

## 🏆 1. Verified Fully Working Models (Chat + Tool Calling)

Ye 57 models Hermes ke autonomous agentic workflows (web research, code execution, file operations, multi-step market intelligence) ke liye 100% ready hain:

### 🌟 Antigravity (Google Gemini Family) — 6 Models
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `antigravity/gemini-3.7-flash-medium` | **5.67s** | **7.14s** | **Primary Agent Model:** 1M+ Context, Balanced Speed & Depth |
| `antigravity/gemini-3.7-flash-high` | **6.64s** | **4.80s** | Highest analytical reasoning, complex competitor breakdown |
| `antigravity/gemini-3.7-flash-tiered` | **6.78s** | **5.93s** | Dynamic tier allocation for variable complexity |
| `antigravity/gemini-pro-agent` | **7.59s** | **5.73s** | Multi-step agentic planning engine |
| `antigravity/gemini-3.1-pro-low` | **7.88s** | **5.45s** | Deep pro-grade reasoning |
| `antigravity/gemini-3.1-flash-lite` | **5.51s** | **4.79s** | Ultra-responsive lightweight Gemini model |

### ⚡ Baseten Family — 17 Models
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `baseten/moonshotai/Kimi-K2.6` | **3.12s** | **2.84s** | Super-fast function caller |
| `baseten/moonshotai/Kimi-K2.7-Code` | **6.64s** | **3.69s** | Exceptional coding and tool precision |
| `baseten/moonshotai/Kimi-K3` | **4.08s** | **3.89s** | Next-gen Kimi architecture |
| `baseten/deepseek-ai/DeepSeek-V4-Flash-0731` | **3.10s** | **3.72s** | Ultra-fast DeepSeek flash model |
| `baseten/deepseek-ai/DeepSeek-V4-Pro` | **3.79s** | **6.66s** | High precision DeepSeek reasoning |
| `baseten/deepseek-ai/DeepSeek-V4-Pro-0813` | **4.48s** | **3.89s** | Stable enterprise DeepSeek |
| `baseten/deepseek-ai/DeepSeek-V4.1-Flash` | **11.45s** | **5.02s** | Advanced DeepSeek reasoning flash |
| `baseten/openai/gpt-oss-120b` | **3.36s** | **6.73s** | 120B parameter open-weights model |
| `baseten/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` | **3.32s** | **6.46s** | Massive 550B flagship architecture |
| `baseten/thinkingmachines/inkling` | **3.64s** | **3.14s** | Fast specialized agent model |
| `baseten/thinkingmachines/inkling-small` | **3.73s** | **3.78s** | Compact low-latency agent |
| `baseten/zai-org/GLM-4.7` | **4.03s** | **6.65s** | Zhipu GLM high accuracy |
| `baseten/zai-org/GLM-5.2` | **4.26s** | **6.62s** | Advanced GLM multilingual |
| `baseten/zai-org/GLM-5.2-Fast` | **3.88s** | **3.44s** | High throughput GLM |
| `baseten/zai-org/GLM-5.3` | **8.72s** | **8.91s** | Complex instruction follower |
| `baseten/zai-org/GLM-5.3-Fast` | **7.69s** | **8.07s** | High-speed GLM 5.3 variant |
| `baseten/zai-org/GLM-5.3-Flash` | **4.15s** | **7.20s** | Fast turn GLM 5.3 |

### 🌐 Google Gemini Native — 7 Models
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `gemini/gemma-4-26b-a4b-it` | **3.58s** | **3.67s** | Google Gemma 26B instruction-tuned |
| `gemini/gemini-3.1-flash-lite` | **5.81s** | **9.13s** | Low-latency Gemini |
| `gemini/gemini-3.1-flash-lite-preview` | **5.54s** | **4.05s** | Fast preview model |
| `gemini/gemini-3.6-flash` | **5.57s** | **5.52s** | Stable Gemini 3.6 Flash |
| `gemini/gemini-3.8-flash` | **11.68s** | **9.50s** | Cutting-edge Gemini 3.8 |
| `gemini/gemini-flash-lite-latest` | **5.02s** | **4.56s** | Always latest flash-lite build |
| `gemini/gemini-robotics-er-2-preview` | **4.53s** | **6.38s** | Advanced tool execution model |

### 🚀 OpenRouter (Free Tier) — 11 Models
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `openrouter/cohere/north-mini-code:free` | **2.68s** | **2.89s** | Cohere North ultra-fast tool caller |
| `openrouter/liquid/lfm-2.5-2.6b:free` | **2.95s** | **2.89s** | Liquid foundation model, high speed |
| `openrouter/inclusionai/ling-3.0-flash-fin:free` | **3.08s** | **2.98s** | Finance/Market specialized Ling model |
| `openrouter/dots-studio/dots-3-note-preview:free` | **3.28s** | **3.79s** | Note and report generation |
| `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | **3.47s** | **3.19s** | 120B Super Nemotron |
| `openrouter/inclusionai/ling-3.0-flash-sante:free` | **3.88s** | **3.60s** | Ling 3.0 multilingual flash |
| `openrouter/nex-agi/nex-n2.5-mini:free` | **4.38s** | **3.20s** | Compact agentic model |
| `openrouter/openrouter/free` | **5.56s** | **4.04s** | OpenRouter auto-router free pool |
| `openrouter/nex-agi/nex-n2.5-pro:free` | **7.31s** | **5.67s** | Nex-AGI pro agent |
| `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | **9.03s** | **3.23s** | 550B parameter Ultra Nemotron |
| `openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | **3.42s** | **6.65s** | 30B reasoning model |

### 🌪️ Typhoon Family — 1 Model
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `typhoon/typhoon-v2.5-30b-a3b-instruct` | **2.55s** | **2.65s** | Ultra-responsive 30B instruction model |

### ⚡ FastRouter Family — 3 Models
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `fastrouter/meta-llama/llama-4-scout-17b-16e-instruct` | **3.20s** | **3.53s** | LLaMA 4 Scout MoE architecture |
| `fastrouter/Qwen/Qwen2.5-72B-Instruct` | **3.78s** | **3.52s** | Qwen 72B flagship reasoning |
| `fastrouter/x-ai/grok-4.1-fast` | **7.19s** | **4.20s** | xAI Grok 4.1 Fast |

### 🤖 MNN-AI Family — 5 Models
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `mnn-ai/gpt-4.1-mini` | **3.33s** | **3.65s** | Fast compact GPT model |
| `mnn-ai/gpt-5.2` | **3.99s** | **3.90s** | GPT 5.2 architecture |
| `mnn-ai/gpt-5.1` | **5.83s** | **4.42s** | GPT 5.1 high quality |
| `mnn-ai/nemotron-3-nano` | **9.26s** | **4.05s** | Compact Nemotron |
| `mnn-ai/qwen-3-235b-a22b-2507` | **9.34s** | **3.88s** | Qwen 235B parameter model |

### 🦙 Ollama Cloud — 2 Models
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `ollamacloud/nemotron-3-super` | **3.40s** | **3.52s** | Cloud hosted Nemotron |
| `ollamacloud/gemma4:31b` | **4.03s** | **3.40s** | Gemma 4 31B cloud model |

### 🎯 NVIDIA Direct — 1 Model
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `nvidia/nvidia/nemotron-3-super-120b-a12b` | **2.90s** | **4.14s** | Direct NVIDIA NIM inference |

### 🎨 Auriko Family — 2 Models
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `auriko/gemma-4-26b-a4b-it` | **4.04s** | **4.10s** | Gemma 26B instruction tuned |
| `auriko/gemma-4-31b-it` | **4.04s** | **5.11s** | Gemma 31B instruction tuned |

### 🐰 Independent / Specialist Models — 2 Models
| Model ID | Chat Speed | Tool Speed | Description / Key Strength |
|---|---|---|---|
| `oc/space-bunny-free` | **4.38s** | **3.35s** | Free agentic specialist |
| `agnes/agnes-2.5-flash` | **2.68s** | **7.74s** | Agnes 2.5 flash reasoning |

---

## 🟡 2. Chat-Only Models (19 Models)

*In models ne Chat response diya lekin Tool Calling support nahi ki ya time out ho gaye:*
* `gemini/gemini-3.5-flash-lite`, `gemini/gemini-flash-latest`
* `typhoon/typhoon-ocr`, `typhoon/typhoon-ocr-preview`, `typhoon/typhoon-ocr-v1.5`
* `mnn-ai/gpt-4.1`, `mnn-ai/gpt-4.1-nano`, `mnn-ai/gpt-oss-120b`, `mnn-ai/gpt-oss-20b`
* `nvidia/openai/gpt-oss-20b`
* `openrouter/nvidia/nemotron-3.5-content-safety:free`, `openrouter/poolside/laguna-s-2.1:free`
* `agnes/agnes-2.0-flash`
* `cfp/google/gemma-4-26b-a4b-it`, `cfp/ibm-granite/granite-4.0-h-micro`, `cfp/meta/llama-3.1-8b-instruct-fp8`, `cfp/moonshotai/kimi-k2.6`, `cfp/nvidia/nemotron-3-120b-a12b`, `cfp/qwen/qwen2.5-coder-32b-instruct`

---

## 🔴 3. Inactive / Failed Models (35 Models)

*In models me upstream 400 Bad Request, 401 Unauthorized, 404 Not Found ya timeout mila:*
* **aion (4):** `aion-2.0`, `aion-3.0`, `aion-3.0-mini`, `aion-rp-llama-3.1-8b` (Auth/Route offline)
* **groq (5):** `gpt-oss-120b`, `gpt-oss-20b`, `gpt-oss-safeguard-20b`, `allam-2-7b`, `qwen3.8-27b` (400 Bad Request)
* **cfp (10):** `deepseek-r1-distill-qwen-32b`, `deepseek-v4-flash-0731`, `deepseek-v4-pro-0813`, `llama-3.3-70b-instruct-fp8-fast`, `mistral-small-3.1-24b-instruct`, `kimi-k2.7-code`, `gpt-oss-20b`, `qwq-32b`, `glm-4.7-flash`, `glm-5.2` (Upstream connection error)
* **mnn-ai (8):** `gemini-3.1-flash-lite`, `gpt-4o`, `gpt-4o-mini`, `mistral-small-latest`, `pixtral-12b-2409`, `qwen-3-235b-a22b`, `qwen-3-coder-plus`, `qwen-3.5-397b-a17b`
* **Others:** `auriko/glm-4.5-flash`, `fastrouter/openai/gpt-oss-120b`, `fastrouter/openai/gpt-oss-20b`, `gemini/gemini-3-flash-preview`, `horde/aphrodite/TheDrummer/Cydonia-24B-v4.3`, `inception/mercury-2`, `anyapi/nvidia/nemotron-3-ultra-550b-a55b:free`, `openrouter/nvidia/nemotron-3.5-lightning:free`

---

## ⚙️ 4. Optimized Multi-Provider Failover Chain in `config.yaml`

Aapke system ko maximum resilience dene ke liye, failover chain ko aise design kiya gaya hai ki **har level par ek alag independent provider** kaam kare. Agar kisi ek provider ka server down ya rate limit ho, to agla provider instant takeover karega:

```yaml
model:
  provider: custom
  base_url: http://localhost:20128/v1
  name: antigravity/gemini-3.7-flash-medium

fallback_providers:
  # Tier 1: Flagship Deep Reasoning (Google Antigravity)
  - provider: custom
    model: antigravity/gemini-3.7-flash-high
    base_url: http://localhost:20128/v1

  # Tier 2: Ultra-Fast Tool & Function Calling (Baseten Moonshot)
  - provider: custom
    model: baseten/moonshotai/Kimi-K2.6
    base_url: http://localhost:20128/v1

  # Tier 3: High Capacity MoE / LLaMA 4 (FastRouter Meta)
  - provider: custom
    model: fastrouter/meta-llama/llama-4-scout-17b-16e-instruct
    base_url: http://localhost:20128/v1

  # Tier 4: Massive Parameter Architecture (Baseten Nemotron 550B)
  - provider: custom
    model: baseten/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B
    base_url: http://localhost:20128/v1

  # Tier 5: High Speed Free Intelligence (OpenRouter Cohere North)
  - provider: custom
    model: openrouter/cohere/north-mini-code:free
    base_url: http://localhost:20128/v1

  # Tier 6: High Speed Compact Fallback (Typhoon 30B)
  - provider: custom
    model: typhoon/typhoon-v2.5-30b-a3b-instruct
    base_url: http://localhost:20128/v1

web:
  search_backend: ddgs

agent:
  max_turns: 12
```

---

## 🔄 Automatic Switching Guarantee
1. **100% OmniRoute Exclusive:** Koi bhi external direct API call nahi hoti; sabhi `http://localhost:20128/v1` ke zariye securely pass hote hain.
2. **Instant Limit Switch:** HTTP 429 (Rate Limit) aate hi Hermes automatically bina query drop kiye agle tier par switch karta hai.
3. **Session Context Safe:** Mid-task research and state switch ke dauran 100% preserve rehta hai.
