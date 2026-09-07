# MIT-BIH Atrial Fibrillation Database (AFDB)

[![License: ODC-By 1.0](https://img.shields.io/badge/License-ODC--By%201.0-green)](https://opendatacommons.org/licenses/by/1-0/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](https://creativecommons.org/licenses/by/4.0/)
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
- **Subjects / records** (verified in `data/RECORDS`): **25** listed; **23** with continuous `.dat`; `00735` and `03665` are rhythm-annotation-only (no `.dat`)
- **Sampling**: **250 Hz**
- **Duration**: ~10 h per signal record
- **Annotations**: rhythm labels (`.atr`) and QRS detections (`.qrs`); some records also ship `.qrsc`
- **Local tree** (verified): **102** files under `data/` (~**606 MiB**)
- **Citation**: Moody & Mark / PhysioNet AFDB citation (see below)

## Table of contents

- [Download](#download)
- [Dataset structure](#dataset-structure)
- [Quick start](#quick-start)
- [License](#license)
- [Citation](#citation)
- [Contact](#contact)

## Download

### This repository

```bash
git clone git@github.com:biometric-community/MIT-BIH-Atrial-Fibrillation-Database.git
```

WFDB records are under [`data/`](data/).

### tbiom helper

```bash
bash projects/datasets/scripts/download_afdb.sh
```

Or with WFDB (from this folder):

```bash
pip install wfdb
python download_afdb.py
# equivalent:
python -c "import wfdb; wfdb.dl_database('afdb', r'data')"
```

Upstream: https://physionet.org/content/afdb/1.0.0/

## Dataset structure

```text
afdb/
├── README.md
├── LICENSE
├── download_afdb.py          # optional WFDB downloader
└── data/
    ├── RECORDS               # 25 record ids
    ├── 00735.hea / .atr / .qrs          # annotation-only (no .dat)
    ├── 03665.hea / .atr / .qrs          # annotation-only (no .dat)
    ├── 04015.dat / .hea / .atr / .qrs
    └── …                     # through 08455
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
