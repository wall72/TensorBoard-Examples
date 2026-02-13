#!/usr/bin/env python3
"""Execute all example notebooks and export HTML results.

Usage:
  python scripts/execute_notebooks.py
"""
from __future__ import annotations

import glob
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"


def check_tensorflow() -> None:
    try:
        import tensorflow as tf  # noqa: F401
    except Exception as exc:  # pragma: no cover
        raise SystemExit(
            "TensorFlow가 설치되어 있지 않아 노트북을 실행할 수 없습니다. "
            "`pip install tensorflow==2.15.*` 후 다시 실행하세요.\n"
            f"원본 오류: {exc}"
        )


def run() -> int:
    check_tensorflow()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    notebooks = sorted(glob.glob(str(ROOT / "0*-*.ipynb")))
    if not notebooks:
        print("No notebooks found.")
        return 1

    for nb in notebooks:
        name = Path(nb).name
        print(f"[RUN] {name}")
        cmd = [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.timeout=1800",
            nb,
        ]
        subprocess.run(cmd, check=True, cwd=ROOT)

        html_out = RESULTS_DIR / f"{Path(nb).stem}.html"
        cmd_html = [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "html",
            "--output",
            str(html_out),
            nb,
        ]
        subprocess.run(cmd_html, check=True, cwd=ROOT)
        print(f"[OK] {html_out.relative_to(ROOT)}")

    print("\nAll notebooks executed. Open HTML files in results/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
