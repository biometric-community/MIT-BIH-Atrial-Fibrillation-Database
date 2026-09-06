#!/usr/bin/env python3
"""Download PhysioNet AFDB into projects/datasets/afdb/data/."""
from pathlib import Path

import wfdb

dest = Path(__file__).resolve().parent / "data"
dest.mkdir(parents=True, exist_ok=True)
print(f"Downloading afdb -> {dest}")
wfdb.dl_database("afdb", str(dest))
files = [p for p in dest.rglob("*") if p.is_file()]
print(f"DONE: {len(files)} files, {sum(p.stat().st_size for p in files) / 1e6:.1f} MB")
for name in ("RECORDS", "04015.dat", "04015.hea"):
    p = dest / name
    status = "OK" if p.exists() else "MISSING"
    size = p.stat().st_size if p.exists() else 0
    print(f"  {name}: {status} ({size} bytes)")
