# Validator examples

Short illustrations for Step 2 and Step 3. Translate to the framework's language after resolving it from the repository. The identifier bound comes from the governing requirement; `max_length` here is the configured value, which may be stricter but not larger.

## Identifier

```python
import re
SAFE_ID = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9_-]*$")

def require_id(value: object, *, max_length: int, hard_max: int) -> str:
    if not isinstance(max_length, int) or isinstance(max_length, bool) or not 1 <= max_length <= hard_max:
        raise RuntimeError("configured identifier limit must be within the governing bound")
    if not isinstance(value, str) or len(value) > max_length or not SAFE_ID.fullmatch(value):
        raise ValueError("invalid identifier")
    return value
```

## Environment value

```python
def require_env(name: str, environ: dict[str, str]) -> str:
    value = environ.get(name)
    if value is None or not value.strip():
        raise RuntimeError(f"{name} is required")
    return value
```

## Workspace path

```python
import re
from pathlib import Path
RESERVED = re.compile(r"(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?", re.IGNORECASE)

def workspace_path(workspace: Path, requested: str) -> Path:
    relative = Path(requested.replace("\\", "/"))
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("path must be workspace-relative")
    for part in relative.parts:
        if ":" in part or part.endswith((".", " ")) or RESERVED.fullmatch(part):
            raise ValueError("path component is not portable")
    root = workspace.resolve(strict=True)
    candidate = (root / relative).resolve(strict=False)
    if not candidate.is_relative_to(root):
        raise ValueError("path escapes workspace")
    return candidate
```

Containment checks do not remove symlink races; sensitive writes also need a trusted directory handle, exclusive creation and a post-open ownership and permission check.
