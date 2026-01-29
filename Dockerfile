FROM python:3.10-slim

# -----------------------------
# System dependencies
# -----------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Workdir
# -----------------------------
WORKDIR /app

# -----------------------------
# Python dependencies
# -----------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Clone NVIDIA Python client (shallow + remove .git)
# -----------------------------
RUN apt-get update && apt-get install -y git \
    && git clone --depth 1 --branch main https://github.com/nvidia-riva/python-clients.git python-clients \
    && rm -rf python-clients/.git \
    && apt-get purge -y git && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Copy app.py
# -----------------------------
COPY app.py .

# -----------------------------
# Expose FastAPI port
# -----------------------------
EXPOSE 8000

# -----------------------------
# Start server
# -----------------------------
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
