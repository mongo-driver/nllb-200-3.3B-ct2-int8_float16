from pathlib import Path

import ctranslate2
import sentencepiece as spm

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = str(BASE_DIR)
SPM_MODEL = str(BASE_DIR / "sentencepiece.bpe.model")

LANG_CODES = {
    "en": "eng_Latn",
    "fa": "pes_Arab",
}

translator = ctranslate2.Translator(MODEL_DIR, device="cpu", inter_threads=4)
sp = spm.SentencePieceProcessor()
sp.Load(SPM_MODEL)


def translate(text: str, src_lang: str, tgt_lang: str) -> str:
    src_code = LANG_CODES[src_lang]
    tgt_code = LANG_CODES[tgt_lang]

    tokens = sp.Encode(text, out_type=str)
    tokens = [src_code] + tokens

    results = translator.translate_batch(
        [tokens],
        target_prefix=[[tgt_code]],
        beam_size=4,
        max_decoding_length=256,
        no_repeat_ngram_size=4,
    )

    output_tokens = results[0].hypotheses[0][1:]  # strip target lang token
    return sp.Decode(output_tokens)


if __name__ == "__main__":
    samples = [
        ("In the Golang programming language, we can use defer to execute code at the end of a function.", "en", "fa"),
        ("در زبان برنامه نویسی گولنگ می توانیم از دیفر برای اجرای یک کد در انتهای یک تابع استفاده کرد", "fa", "en"),
        ("Artificial intelligence is transforming the world.", "en", "fa"),
    ]

    for text, src, tgt in samples:
        result = translate(text, src, tgt)
        print(f"[{src}->{tgt}] {text}")
        print(f"        -> {result}\n")
