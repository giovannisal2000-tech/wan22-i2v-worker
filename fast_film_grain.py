# Standalone FastFilmGrain node for ComfyUI
# Provides: class_type "FastFilmGrain" (used in WAN22 I2V workflow, node #139)
# Only depends on torch -- no external libraries needed.

import torch


class FastFilmGrain:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "grain_intensity": ("FLOAT", {
                    "default": 0.1, "min": 0.0, "max": 1.0, "step": 0.001
                }),
                "saturation_mix": ("FLOAT", {
                    "default": 0.15, "min": 0.0, "max": 1.0, "step": 0.01
                }),
                "batch_size": ("INT", {
                    "default": 4, "min": 1, "max": 64, "step": 1
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_grain"
    CATEGORY = "image/filters"

    def apply_grain(self, images, grain_intensity, saturation_mix, batch_size):
        result = images.clone()

        # Optional slight desaturation
        if saturation_mix > 0.0:
            lum = (0.299 * result[..., 0:1]
                 + 0.587 * result[..., 1:2]
                 + 0.114 * result[..., 2:3])
            result = result * (1.0 - saturation_mix) + lum.expand_as(result) * saturation_mix

        # Add luminance-weighted grain
        grain = torch.randn_like(result) * grain_intensity
        result = (result + grain).clamp(0.0, 1.0)

        return (result,)


NODE_CLASS_MAPPINGS = {
    "FastFilmGrain": FastFilmGrain,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "FastFilmGrain": "Fast Film Grain",
}
