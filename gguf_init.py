# Patched __init__.py for ComfyUI-GGUF
# Adds LoaderGGUF alias (uses gguf_name parameter) for WAN22 I2V workflow compatibility
# city96/ComfyUI-GGUF registers UnetLoaderGGUF; the WAN22 workflow needs LoaderGGUF(gguf_name)

try:
    import comfy.utils
except ImportError:
    pass
else:
    import folder_paths
    from .nodes import NODE_CLASS_MAPPINGS, UnetLoaderGGUF

    NODE_DISPLAY_NAME_MAPPINGS = {k: v.TITLE for k, v in NODE_CLASS_MAPPINGS.items()}

    class LoaderGGUF(UnetLoaderGGUF):
        """LoaderGGUF — alias for UnetLoaderGGUF with gguf_name parameter."""

        @classmethod
        def INPUT_TYPES(cls):
            unet_names = folder_paths.get_filename_list("unet_gguf")
            return {"required": {"gguf_name": (unet_names,)}}

        TITLE = "GGUF Loader"
        FUNCTION = "load_gguf"

        def load_gguf(self, gguf_name):
            return self.load_unet(gguf_name)

    NODE_CLASS_MAPPINGS["LoaderGGUF"] = LoaderGGUF
    NODE_DISPLAY_NAME_MAPPINGS["LoaderGGUF"] = "GGUF Loader"
    print("[ComfyUI-GGUF] \u2713 LoaderGGUF alias registered")

    __all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
