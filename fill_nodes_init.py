import os, importlib.util

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

def try_load_module(fpath, module_name):
    try:
        spec = importlib.util.spec_from_file_location(module_name, fpath)
        if spec is None:
            return
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, 'NODE_CLASS_MAPPINGS'):
            NODE_CLASS_MAPPINGS.update(mod.NODE_CLASS_MAPPINGS)
        if hasattr(mod, 'NODE_DISPLAY_NAME_MAPPINGS'):
            NODE_DISPLAY_NAME_MAPPINGS.update(mod.NODE_DISPLAY_NAME_MAPPINGS)
        print(f'[Fill-Nodes] ✓ {module_name}')
    except Exception as e:
        print(f'[Fill-Nodes] ✗ {module_name}: {type(e).__name__}: {e}')

base_dir = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(base_dir):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
    for fname in files:
        if fname.endswith('.py') and not fname.startswith('_'):
            fpath = os.path.join(root, fname)
            rel_path = os.path.relpath(fpath, base_dir)
            module_name = rel_path.replace(os.sep, '.')[:-3]
            try_load_module(fpath, module_name)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
