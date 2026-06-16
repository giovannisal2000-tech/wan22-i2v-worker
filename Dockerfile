# WAN 2.2 I2V — RunPod Serverless Worker
FROM runpod/worker-comfyui:5.8.5-base

# ── Custom nodes from Comfy Registry ─────────────────────────────────────────
RUN comfy node install comfyui-videohelpersuite && \
    comfy node install rgthree-comfy && \
    comfy node install comfyui-nodes-base && \
    comfy node install comfyui-gguf && \
    comfy node install comfyui_essentials && \
    comfy node install comfyui-lama-remover || true

# Install CR Animation nodes (CR Simple Text Watermark)
RUN cd /comfyui/custom_nodes && \
    git clone --depth 1 https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes.git && \
    pip install -r ComfyUI_Comfyroll_CustomNodes/requirements.txt 2>/dev/null || true

# Install fill-nodes (FL_RIFE + FL_IntToFloat + FastFilmGrain) — from GitHub, then patch __init__.py
RUN cd /comfyui/custom_nodes && \
    git clone --depth 1 https://github.com/filliptm/ComfyUI_Fill-Nodes.git && \
    pip install -r ComfyUI_Fill-Nodes/requirements.txt 2>/dev/null || true

# Patch fill-nodes __init__.py: dynamic loader — exposes FL_RIFE, FL_IntToFloat, FastFilmGrain, etc.
COPY fill_nodes_init.py /comfyui/custom_nodes/ComfyUI_Fill-Nodes/__init__.py

# Download RIFE model needed by FL_RIFE
RUN mkdir -p /comfyui/models/rife && \
    wget -q -O /comfyui/models/rife/rife47.pth \
    https://github.com/hzwer/ECCV2022-RIFE/releases/download/v4.7/rife47.pth 2>/dev/null || \
    echo "RIFE model download failed — will load from network volume"

# ── Extra model paths: point to network volume structure ──────────────────────
COPY extra_model_paths.yaml /comfyui/extra_model_paths.yaml
