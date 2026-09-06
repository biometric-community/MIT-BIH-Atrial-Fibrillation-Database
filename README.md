# MIT-BIH Atrial Fibrillation Database (AFDB)

[![License: ODC-By 1.0](https://img.shields.io/badge/License-ODC--By%201.0-green)](https://opendatacommons.org/licenses/by/1-0/)
[![Access: public](https://img.shields.io/badge/access-public-0e8a16.svg)](https://physionet.org/content/afdb/1.0.0/)

**MIT-BIH Atrial Fibrillation Database (AFDB)** — long-term ECG recordings of subjects with atrial fibrillation (paroxysmal or sustained); PhysioNet open access.

- **Dataset repository**: https://github.com/biometric-community/MIT-BIH-Atrial-Fibrillation-Database
- **Upstream source**: https://physionet.org/content/afdb/1.0.0/
- **DOI**: https://doi.org/10.13026/C2MW2D
- **Original format**: PhysioNet WFDB (`.dat` / `.hea` / `.atr` / `.qrs`) under `data/`
- **License (data)**: [Open Data Commons Attribution License v1.0](https://opendatacommons.org/licenses/by/1-0/) (PhysioNet)
- **License (helpers / docs)**: CC BY 4.0 (see [`LICENSE`](LICENSE))

| Field | Value |
|-------|-------|
| Catalog id (tbiom) | `afdb` |
| Category | `physio` |
| Access | `public` |
| PhysioNet / WFDB slug | `afdb` |
| Upstream homepage | https://physionet.org/content/afdb/1.0.0/ |
| Paper alias | AFDB (e.g. Abdeldayem & Bourlai, TBIOM 2019 spectral-correlation ECG ID) |

## TL;DR

- **Task**: atrial fibrillation rhythm analysis / ECG identity benchmarking
- **Modality**: two-channel ECG (WFDB `.dat` / `.hea`) plus rhythm and beat annotations
- **Platform**: MIT-BIH long-term ambulatory AF recordings
- **Real/Synthetic**: real
- **Subjects / records**: **25** records listed; **23** include continuous signals; `00735` and `03665` are rhythm-annotation-only (no `.dat`)
- **Sampling**: **250 Hz**
- **Duration**: ~10 h per signal record
- **Annotations**: rhythm labels (`.atr`) and QRS detections (`.qrs`)
- **Citation**: Moody & Mark / PhysioNet AFDB citation (see below)

## Download

- **This repository**: WFDB records under [`data/`](data/) (when populated).
- **Upstream**: https://physionet.org/content/afdb/1.0.0/
- **Helper script** (from tbiom monorepo root):

```bash
bash projects/datasets/scripts/download_afdb.sh
```

Preferred (after `pip install wfdb`):

```bash
python -c "import wfdb; wfdb.dl_database('afdb', r'projects/datasets/afdb/data')"
```

## Dataset structure

```text
afdb/
├── README.md
├── LICENSE
└── data/
    ├── RECORDS
    ├── ANNOTATORS
    ├── 04015.dat / .hea / .atr / .qrs
    └── …
```

## Quick start

```python
import wfdb

rec = wfdb.rdrecord("data/04015")
ann = wfdb.rdann("data/04015", "atr")
print(rec.sig_name, rec.fs, rec.p_signal.shape, len(ann.sample))
```

## License

- **Data** (PhysioNet AFDB): [ODC-By 1.0](https://opendatacommons.org/licenses/by/1-0/)
- **Helpers / docs** in this repository: [CC BY 4.0](LICENSE)

## Citation

Please cite the PhysioNet AFDB publication and the PhysioNet resource itself when using these data. See https://physionet.org/content/afdb/1.0.0/ for the recommended citations.

## Contact

- Upstream / PhysioNet: https://physionet.org/content/afdb/1.0.0/
- This mirror: https://github.com/biometric-community/MIT-BIH-Atrial-Fibrillation-Database
