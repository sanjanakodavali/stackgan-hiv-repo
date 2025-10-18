# StackGAN-HIV — Text→Figure Synthesis for HIV Entry & Drug-Target Structures

**Goal:** Adapt the original [StackGAN](https://github.com/hanzhanggit/StackGAN) (two-stage, conditioning augmentation) to generate publication-style molecular renderings
from short captions about HIV biology (CCR5/CXCR4, Env–CD4, RT/PR/IN complexes).

**Why this matters:** Clean, CC0 structural data from the Protein Data Bank (PDB) lets us train a caption-conditioned image generator without privacy hurdles. The system targets
research-lab-facing visuals (surface/cartoon/ligand views) that are crisp and easy to evaluate with both FID/KID and text–image retrieval metrics (Recall@K with a biomedical CLIP tower).

## Repository Layout
```
stackgan-hiv/
├─ data/            # (sample) image/caption pairs; scripts will populate this
├─ docs/            # blueprint PDF, diagrams, wireframes
├─ notebooks/       # setup.ipynb for initial EDA and environment checks
├─ results/         # exploratory plots or early outputs
├─ scripts/         # dataset building, PDB rendering stubs
├─ src/             # training/eval helpers that wrap the original StackGAN code
├─ ui/              # placeholder for Streamlit/Gradio demo
└─ README.md
```

## Installation
We recommend Python 3.10+ in a fresh environment.

**Option A — pip**
```bash
pip install -r requirements.txt
```

**Option B — conda**
```bash
conda env create -f environment.yml
conda activate stackgan-hiv
```

## Quick Start
1. Open `notebooks/setup.ipynb` and run all cells to verify the environment.
2. (Optional) Put a few sample PNGs in `data/images/` and a `data/pairs.csv` with columns:
   `id, pdb_id, caption, image_path, view`.
3. Train Stage I then Stage II (training scripts to be added in the next milestone).

## Dataset Information
- **Core:** RCSB **Protein Data Bank (PDB)** structures related to HIV/host entry and drug targets (e.g., CCR5:maraviroc, CXCR4:antagonists, Env–CD4, RT/PR/IN).
  We auto-render multiple views (surface/cartoon/ligand sticks) and generate short captions from metadata. **License:** CC0/public domain.
- **Optional add-on:** A small pack of **Human Protein Atlas** IF/IHC images for CCR5/CXCR4 (CC BY-SA 4.0; attribution required).

## How to Run the Setup Notebook
```bash
jupyter notebook notebooks/setup.ipynb
```
Run all cells. You should see a sample plot and environment checks succeed.

## Author
- Name: Aslesha Sanjana Kodavali
- Email: sanjanakodavali10@gmail.com

---
*This repo preserves the original StackGAN training flow while swapping in a biomedical text encoder and a PDB-based dataset pipeline.*
