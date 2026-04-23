---
license: cc-by-nc-4.0
base_model: facebook/nllb-200-3.3B
library_name: ctranslate2
pipeline_tag: translation
tags:
  - nllb
  - ctranslate2
  - int8_float16
  - en
  - fa
languages:
  - en
  - fa
---

# NLLB-200 3.3B CTranslate2 int8_float16 Bundle

This folder contains an optimized CTranslate2 build of `facebook/nllb-200-3.3B` plus helper scripts.

## Model link

- Hugging Face model: https://huggingface.co/mohamadpk/nllb-200-3.3B-ct2-int8_float16
- GitHub version of this repo excludes `model.bin` to keep repository size manageable.

## File details

| File | Required | Purpose |
|---|---|---|
| `model.bin` | Yes | Quantized CTranslate2 weights (`int8_float16`). This is the main model payload used at inference time. |
| `config.json` | Yes | CTranslate2 runtime configuration (model architecture and decoding metadata expected by CT2). |
| `shared_vocabulary.json` | Yes | Vocabulary mapping used by CTranslate2 during token generation. |
| `sentencepiece.bpe.model` | Yes | SentencePiece tokenizer model. Encodes input text to subword pieces and decodes output pieces back to text. |
| `tokenizer.json` | Recommended | Full tokenizer definition used by Hugging Face tooling and some integrations. |
| `tokenizer_config.json` | Recommended | Tokenizer runtime options (special token behavior, defaults). |
| `special_tokens_map.json` | Recommended | Mapping for special tokens (language tags, BOS/EOS style tokens). |
| `translate.py` | Optional helper | Example EN<->FA inference script using CTranslate2 + SentencePiece. |
| `convert_model.py` | Optional helper | One-time conversion script from HF model to CT2 `int8_float16`. |
| `check_gpu.py` | Optional helper | Simple CUDA availability check in local PyTorch environment. |
| `requirements.txt` | Optional helper | Python dependencies for helper scripts (`ctranslate2`, `sentencepiece`, etc.). |

## Quick usage

Run commands from the project root:

```bash
venv\Scripts\pip.exe install -r nllb-200-3.3B-ct2-int8_float16\requirements.txt
venv\Scripts\python.exe nllb-200-3.3B-ct2-int8_float16\check_gpu.py
venv\Scripts\python.exe nllb-200-3.3B-ct2-int8_float16\translate.py
```

## Benchmark results (CUDA)

Benchmark mode: `HF float16 GPU` vs `CTranslate2 int8_float16 GPU`

| # | Direction | HF time | CT2 time | Speedup |
|---|---|---:|---:|---:|
| 1 | en->fa | 36.41s | 5.25s | 6.94x |
| 2 | en->fa | 15.74s | 5.99s | 2.63x |
| 3 | en->fa | 47.74s | 3.74s | 12.76x |
| 4 | fa->en | 32.98s | 2.98s | 11.07x |
| Total | mixed | 132.87s | 17.96s | 7.40x |

Benchmark environment:

- GPU: NVIDIA GeForce RTX 2060 SUPER (8GB VRAM)
- Runtime mode: CUDA
- Comparison: HF float16 GPU vs CT2 int8_float16 GPU

Quality snapshots:

1. en->fa  
HF: `در زبان برنامه نویسی گولانگ گولانگ، ما می توانیم از defer استفاده کنیم تا کد را در پایان تابع اجرا کنیم.`  
CT2: `در زبان برنامه نویسی Golang، ما می توانیم از defer برای اجرای کد در پایان یک تابع استفاده کنیم.`

2. en->fa  
HF: `هوش مصنوعی هوش مصنوعی در حال تغییر جهان است`  
CT2: `هوش مصنوعی در حال تغییر جهان است.`

3. en->fa  
HF: `مدل های یادگیری ماشینی مدل های یادگیری ماشین ماشین مدل های یادگیری یادگیری ماشین ماشین نیاز به مقدار زیادی از داده برای آموزش به طور موثر نیاز به داده های بزرگ برای آموزش موثر. .`  
CT2: `مدل های یادگیری ماشین به مقادیر زیادی از داده ها برای آموزش موثر نیاز دارند.`

4. fa->en  
HF: `Natural Language Processing (NLP) is one of the most important branches of AI.`  
CT2: `Natural language processing is one of the important branches of artificial intelligence.`

## Attribution

- Base model: `facebook/nllb-200-3.3B`
- Original model authors: Meta AI / NLLB team
- This package is a converted and quantized derivative (`CTranslate2 int8_float16`)

## Notes

- `translate.py` is self-contained and loads model/tokenizer files from this folder.
- `convert_model.py` is for local one-time conversion from `facebook/nllb-200-3.3B`.

## License

- Base/derived model artifacts follow: `CC-BY-NC-4.0`
- Non-commercial use only, unless you obtain separate permission from rights holders.
- Keep attribution to the base model when redistributing this package.
