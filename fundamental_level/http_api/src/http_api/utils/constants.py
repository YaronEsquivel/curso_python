from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent

PATHS: dict[str, Path] = {"OUTPUT_PATH": BASE_PATH / "output"}
