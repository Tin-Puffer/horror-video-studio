#!/usr/bin/env python3
"""Vietnamese speech-to-text for tools/check_voice.py, run with the Python that has torch + transformers
(the Dubber venv, "vieneu_python" in config.local.json).

  <python> tools/asr_worker.py <model> <in.json: [wav paths]> <out.json: {path: {text, words: [[word, start, end]]}}>

The model (default vinai/PhoWhisper-base, ~300 MB) is downloaded to the Hugging Face cache on first use.
"""
import json
import subprocess
import sys


def main():
    model, src, dst = sys.argv[1:4]
    import numpy as np
    from transformers import pipeline
    asr = pipeline("automatic-speech-recognition", model=model, device="cpu")
    paths = json.load(open(src))
    out = {}
    for i, p in enumerate(paths):
        # 0.3 s of leading silence: without it Whisper often drops the first word of a take
        sr = 16000  # Whisper's rate; ffmpeg resamples (the pipeline would need torchaudio)
        pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
                             capture_output=True, check=True).stdout
        audio = np.concatenate([np.zeros(int(0.3 * sr), np.float32), np.frombuffer(pcm, np.float32)])
        r = asr({"raw": audio, "sampling_rate": sr}, return_timestamps="word",
                generate_kwargs={"language": "vi", "task": "transcribe"})
        for c in r.get("chunks", []):
            c["timestamp"] = tuple(None if t is None else max(0.0, t - 0.3) for t in c["timestamp"])
        out[p] = {"text": r["text"].strip(),
                  "words": [[c["text"].strip(), c["timestamp"][0], c["timestamp"][1]] for c in r.get("chunks", [])]}
        print(f"  asr {i + 1}/{len(paths)}", file=sys.stderr, flush=True)
    json.dump(out, open(dst, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
