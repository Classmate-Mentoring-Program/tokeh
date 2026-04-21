# data/

This directory holds datasets used by the tokeh project and is **not**
tracked in version control (see `.gitignore`).

## Sub-directories

| Directory   | Purpose |
|-------------|---------|
| `raw/`      | Original, unmodified source data (CSV, JSON, plain text, etc.). |
| `processed/`| Cleaned and transformed data ready for modelling. |

## Usage

1. Download or place your raw data files inside `raw/`.
2. Run the appropriate preprocessing script (see `Makefile`) to populate `processed/`.

> **Note**: Never commit actual data files.  Add large files to `.gitignore`
> or use [DVC](https://dvc.org/) for data versioning.
