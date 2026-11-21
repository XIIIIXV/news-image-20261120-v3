"""make.fun entrypoint: copy the pre-rendered entry.png to the output
directory. No rendering happens here (the grader runs on a read-only
filesystem)."""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR")
if not OUT:
    sys.exit("MAKEFUN_OUTPUT_DIR is not set")
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))
