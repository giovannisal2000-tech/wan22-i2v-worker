# Minimal stub — exposes only FL_RIFE and FL_IntToFloat, skips all AI/cloud imports
try:
    from .nodes.video.FL_RIFE import FL_RIFE
except Exception as e:
    print("FL_RIFE import failed:", e)
    FL_RIFE = None

try:
    from .nodes.utility.FL_NumberConverter import FL_IntToFloat, FL_FloatToInt
except Exception as e:
    print("FL_IntToFloat import failed:", e)
    FL_IntToFloat = None
    FL_FloatToInt = None

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

if FL_RIFE is not None:
    NODE_CLASS_MAPPINGS["FL_RIFE"] = FL_RIFE
    NODE_DISPLAY_NAME_MAPPINGS["FL_RIFE"] = "FL RIFE Interpolation"

if FL_IntToFloat is not None:
    NODE_CLASS_MAPPINGS["FL_IntToFloat"] = FL_IntToFloat
    NODE_DISPLAY_NAME_MAPPINGS["FL_IntToFloat"] = "FL Int To Float"

if FL_FloatToInt is not None:
    NODE_CLASS_MAPPINGS["FL_FloatToInt"] = FL_FloatToInt
    NODE_DISPLAY_NAME_MAPPINGS["FL_FloatToInt"] = "FL Float To Int"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
print("comfyui_fill-nodes stub loaded. Nodes:", list(NODE_CLASS_MAPPINGS.keys()))
