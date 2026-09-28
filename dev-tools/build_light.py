"""Compatibility entry point for the committed text-only release builder."""
from pathlib import Path
import runpy
import sys

if __name__ == "__main__":
    directory = Path(__file__).resolve().parent / "buildScripts"
    sys.path.insert(0, str(directory))
    runpy.run_path(str(directory / "build_release.py"), run_name="__main__")
