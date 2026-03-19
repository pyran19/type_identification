from __future__ import annotations

import os
import shutil
import subprocess


SYSTEM_PYTHON_CANDIDATES = ("python3", "python")


def main() -> None:
    system_python = next((path for name in SYSTEM_PYTHON_CANDIDATES if (path := shutil.which(name))), None)
    if system_python is None:
        raise SystemExit("No system Python interpreter with pytest available was found.")

    env = os.environ.copy()
    existing_pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = "src" if not existing_pythonpath else f"src:{existing_pythonpath}"
    completed = subprocess.run([system_python, "-m", "pytest"], env=env)
    raise SystemExit(completed.returncode)
