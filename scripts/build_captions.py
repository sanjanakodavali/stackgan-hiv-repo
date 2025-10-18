#!/usr/bin/env python3
"""Generate caption CSV from pdb_meta.jsonl (placeholder for now)."""
import csv, json
from pathlib import Path

META = Path("data/pdb_meta.jsonl")
OUT = Path("data/pairs.csv")

def make_caption(m):
    base = f"Surface view of {m.get('protein','complex')}"
    lig = m.get("ligand")
    if lig: base += f" bound to {lig}"
    base += f" (PDB {m['pdb_id']}); {m.get('view','front')} orientation."
    return base

def main():
    rows = []
    if META.exists():
        for line in META.read_text().strip().splitlines():
            m = json.loads(line)
            rows.append({
                "id": f"{len(rows):06d}",
                "pdb_id": m["pdb_id"],
                "caption": make_caption(m),
                "image_path": f"data/images/{m['pdb_id']}_{m.get('view','front')}_{m.get('style','surface')}.png",
                "view": m.get("view","front")
            })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id","pdb_id","caption","image_path","view"])
        w.writeheader(); w.writerows(rows)
    print("Wrote", OUT)

if __name__ == "__main__":
    main()
