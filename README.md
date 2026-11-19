# Human Virome Methods Hub

A living, evidence-linked resource for selecting, comparing, and reporting computational and laboratory methods in human viral metagenomics.

> Status: community prototype developed alongside the HVP Bioinformatics Working Group review. This is not yet an official HVP standard.

## Scope

This resource complements broad software catalogues by focusing on method–specimen fit, evidentiary claims, failure modes, benchmarks, and reporting requirements in **human** viromics.

## Website

After GitHub Pages is enabled, the project site will be available at:

[https://manishsinha002.github.io/human-virome-methods-hub/](https://manishsinha002.github.io/human-virome-methods-hub/)

## Local preview

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

## Data

- `data/methods.csv`: curated methods and tools
- `data/specimen_matrix.csv`: method–specimen compatibility
- `data/benchmarks.csv`: benchmark datasets
- `data/references.csv`: supporting literature

## Contributing

Please read `CONTRIBUTING.md`. Evidence-backed corrections and additions are welcome through GitHub Issues and pull requests.
