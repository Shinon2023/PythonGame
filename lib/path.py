from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[1]
def resolve_path(relative_path: str) -> str:
    """
    แปลง path ที่เป็นแบบ relative (@/) ให้เป็น absolute path
    """
    return str(PROJECT_ROOT / relative_path.lstrip("@/"))
