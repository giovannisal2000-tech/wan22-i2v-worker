#!/usr/bin/env python3
"""Build-time patch: append LoaderGGUF alias to comfyui-gguf __init__.py.
Run this AFTER 'comfy node install comfyui-gguf' in the Dockerfile.
"""
import os, sys

INIT_PATH = "/comfyui/custom_nodes/comfyui-gguf/__init__.py"

PATCH = """

# -- LoaderGGUF alias (WAN 2.2 I2V) -----------------------------------------
try:
    import folder_paths as _fp

    class LoaderGGUF(NODE_CLASS_MAPPINGS["UnetLoaderGGUF"]):
        \"\"\"LoaderGGUF - alias for UnetLoaderGGUF (WAN 2.2 I2V workflow).\"\"\"
        @classmethod
        def INPUT_TYPES(cls):
            return {"required": {"gguf_name": (_fp.get_filename_list("unet_gguf"),)}}
        TITLE = "GGUF Loader"
        FUNCTION = "load_gguf"
        def load_gguf(self, gguf_name):
            return self.load_unet(gguf_name)

    NODE_CLASS_MAPPINGS["LoaderGGUF"] = LoaderGGUF
    NODE_DISPLAY_NAME_MAPPINGS["LoaderGGUF"] = "GGUF Loader"
    print("[ComfyUI-GGUF] LoaderGGUF alias registered")
except Exception as _e:
    print(f"[ComfyUI-GGUF] LoaderGGUF alias failed: {_e}")
"""

if not os.path.exists(INIT_PATH):
    print(f"ERROR: {INIT_PATH} not found", file=sys.stderr)
    sys.exit(1)

with open(INIT_PATH, "r") as f:
    existing = f.read()

if "LoaderGGUF" in existing:
    print("Already patched.")
    sys.exit(0)

with open(INIT_PATH, "a") as f:
    f.write(PATCH)

print(f"Patched {INIT_PATH}")
