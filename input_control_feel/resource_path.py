from __future__ import annotations

from pathlib import Path
import sys


def _base_dir() -> Path:
    """Return the runtime base dir for source and PyInstaller builds."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent.parent


def resolve_asset_path(relative_path: str) -> str:
    """Resolve an asset path like 'input_control_feel/sprites/...'."""
    return str(_base_dir() / Path(relative_path))
