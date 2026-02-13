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


def tensorflow_install_guide() -> str:
    py = sys.version_info
    version_str = f"{py.major}.{py.minor}"
    guide = [
        "TensorFlow가 설치되어 있지 않아 노트북을 실행할 수 없습니다.",
        f"현재 Python 버전: {version_str}",
        "",
        "설치 가이드:",
    ]

    if py.major == 3 and py.minor <= 11:
        guide.extend(
            [
                "- Python 3.10/3.11 환경에서는 아래 명령을 먼저 시도하세요:",
                "  pip install 'tensorflow==2.20.*'",
            ]
        )
    else:
        guide.extend(
            [
                "- TensorFlow 2.20 wheel 지원 범위를 확인하세요 (Python 버전에 따라 설치 가능 버전이 달라질 수 있습니다).",
                "- 아래 중 하나를 사용하세요:",
                "  1) Python 3.10/3.11 가상환경 생성 후: pip install 'tensorflow==2.20.*'",
                "  2) 현재 Python 유지 시: pip install tensorflow  (인덱스의 최신 안정화 버전)",
            ]
        )

    guide.extend(
        [
            "",
            "추가 확인:",
            "- pip 오류에 버전 목록이 보이는데 2.20이 없다면, 현재 패키지 인덱스에서 2.20이 제공되지 않는 상황입니다.",
            "- 이 경우: (a) 인덱스를 공식 PyPI로 변경하거나 (b) tensorflow 최신 안정화 버전으로 설치하세요.",
            "- 네트워크/프록시 제한 환경에서도 동일한 메시지가 발생할 수 있습니다.",
        ]
    )
    return "\n".join(guide)


def check_tensorflow() -> None:
    try:
        import tensorflow as tf  # noqa: F401
    except Exception as exc:  # pragma: no cover
        raise SystemExit(f"{tensorflow_install_guide()}\n원본 오류: {exc}")


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
