import ctranslate2

SRC_MODEL = "facebook/nllb-200-3.3B"
OUT_DIR   = "nllb-200-3.3B-ct2-int8_float16"

print("Converting " + SRC_MODEL + " -> " + OUT_DIR + " (int8_float16) ...")

converter = ctranslate2.converters.TransformersConverter(
    SRC_MODEL,
    low_cpu_mem_usage=True,
)

converter.convert(
    output_dir=OUT_DIR,
    quantization="int8_float16",
    force=True,
)

print("Done. Optimized model saved to: " + OUT_DIR + "/")
