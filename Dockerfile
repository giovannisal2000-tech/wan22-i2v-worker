# WAN 2.2 I2V — RunPod Serverless Worker
FROM runpod/worker-comfyui:5.8.5-base

# Custom nodes from Comfy Registry
RUN comfy-node-install \
    comfyui-videohelpersuite \
    rgthree-comfy \
    comfyui-nodes-base \
    comfyui-gguf

# CR Animation nodes (CR Simple Text Watermark)
RUN cd /comfyui/custom_nodes && \
    git clone --depth 1 https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes.git && \
    pip install -r ComfyUI_Comfyroll_CustomNodes/requirements.txt 2>/dev/null || true

# FastFilmGrain
RUN cd /comfyui/custom_nodes && \
    git clone --depth 1 https://github.com/spacepxl/ComfyUI-Fast-Film-Grain.git 2>/dev/null || true

# fill-nodes (FL_RIFE + FL_IntToFloat)
RUN cd /comfyui/custom_nodes && \
    git clone --depth 1 https://github.com/filliptm/ComfyUI_Fill-Nodes.git && \
    pip install -r ComfyUI_Fill-Nodes/requirements.txt 2>/dev/null || true

# Patch fill-nodes __init__.py
COPY fill_nodes_init.py /comfyui/custom_nodes/ComfyUI_Fill-Nodes/__init__.py

# RIFE model
RUN mkdir -p /comfyui/models/rife && \
    wget -q -O /comfyui/models/rife/rife47.pth \
    https://github.com/hzwer/ECCV2022-RIFE/releases/download/v4.7/rife47.pth 2>/dev/null || true

# Extra model paths pointing to network volume structure
COPY extra_model_paths.yaml /comfyui/extra_model_paths.yaml
