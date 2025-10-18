#!/usr/bin/env python3
"""Headless PDB rendering stub (PyMOL or py3Dmol).
Populate PDB_IDS and run to emit PNGs into data/images and a meta JSONL.
This is a scaffold for Deliverable 1 — full renderer comes in Milestone 2.
"""
from pathlib import Path
import json

PDB_IDS = ["4MBS", "3OE0", "1GC1"]  # CCR5:maraviroc, CXCR4:IT1t, gp120:CD4
OUT_DIR = Path("data/images")
META = Path("data/pdb_meta.jsonl")

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with META.open("w") as f:
        for pid in PDB_IDS:
            # Placeholder metadata (renders come in next milestone)
            rec = {"pdb_id": pid, "protein": "TBD", "ligand": "TBD", "view": "front", "style": "surface"}
            f.write(json.dumps(rec) + "\n")
    print("Wrote placeholder meta to", META)

if __name__ == "__main__":
    main()
