from fastapi import FastAPI, UploadFile, HTTPException
import subprocess
import json
import os
import tempfile

# =========================
# CONSTANTS
# =========================
SERVER = "grpc.nvcf.nvidia.com:443"
LANGUAGE = "en"

FUNCTION_ID = os.environ.get("NVIDIA_FUNCTION_ID")
API_KEY = os.environ.get("NVIDIA_API_KEY")

if not API_KEY:
    raise RuntimeError("NVIDIA_API_KEY environment variable is not set")

if not FUNCTION_ID:
    raise RuntimeError("NVIDIA_FUNCTION_ID environment variable is not set")

# =========================
# FASTAPI APP
# =========================
app = FastAPI(title="NVIDIA ASR Microservice")

@app.post("/asr")
async def transcribe(file: UploadFile):
    if not file.filename.lower().endswith((".wav", ".flac", ".opus")):
        raise HTTPException(status_code=400, detail="Unsupported audio format")

    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        audio_path = tmp.name

    cmd = [
        "python",
        "python-clients/scripts/asr/transcribe_file_offline.py",
        "--server", SERVER,
        "--use-ssl",
        "--metadata", "function-id", FUNCTION_ID,
        "--metadata", "authorization", f"Bearer {API_KEY}",
        "--language-code", LANGUAGE,
        "--input-file", audio_path
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    os.unlink(audio_path)

    if result.returncode != 0:
        raise HTTPException(
            status_code=500,
            detail=result.stderr
        )

    # Extract JSON safely
    stdout = result.stdout
    start = stdout.find("{")
    end = stdout.rfind("}") + 1

    if start == -1:
        raise HTTPException(status_code=500, detail="Invalid ASR output")

    return json.loads(stdout[start:end])
