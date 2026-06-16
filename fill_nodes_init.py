# Safe __init__.py for ComfyUI_Fill-Nodes
# Only loads the nodes required by the WAN22 I2V workflow.
# Uses relative imports (works because this IS the package __init__.py)
# and wraps each import in try/except to avoid breaking on missing deps.

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

try:
    from .nodes.video.FL_RIFE import FL_RIFE
    NODE_CLASS_MAPPINGS["FL_RIFE"] = FL_RIFE
    NODE_DISPLAY_NAME_MAPPINGS["FL_RIFE"] = "FL RIFE Frame Interpolation"
    print("[Fill-Nodes] ✓ FL_RIFE")
except Exception as e:
    print(f"[Fill-Nodes] ✗ FL_RIFE: {e}")

try:
    from .nodes.utility.FL_NumberConverter import FL_IntToFloat, FL_FloatToInt
    NODE_CLASS_MAPPINGS["FL_IntToFloat"] = FL_IntToFloat
    NODE_DISPLAY_NAME_MAPPINGS["FL_IntToFloat"] = "FL Int to Float"
    print("[Fill-Nodes] ✓ FL_IntToFloat")
except Exception as e:
    print(f"[Fill-Nodes] ✗ FL_IntToFloat: {e}")

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
