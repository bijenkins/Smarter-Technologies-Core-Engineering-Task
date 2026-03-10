# Package Sorter

Sorts packages into stacks (`STANDARD`, `SPECIAL`, `REJECTED`) based on their dimensions and mass.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
python -c "from sort import sort; print(sort(100, 100, 100, 25))"
```

## Tests

```bash
pytest
```
