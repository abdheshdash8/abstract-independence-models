# Abstract Independence Models

Research implementation of algorithms for abstract conditional independence models.

## Research Goals

This project investigates computational methods for

- Abstract independence models
- Graphoid axioms
- Singleton-transitivity closures
- Elementary triplets
- Graphical representations of independence structures

The project is part of a research internship under

**Prof. Kayvan Sadeghi**

Department of Statistical Science

University College London

## GitHub Repository Structure
```
abstract-independence-models/
│
├── LICENSE
├── README.md
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── CITATION.cff
├── CHANGELOG.md
│
├── docs/
│   ├── overview.md
│   ├── theory.md
│   ├── algorithms.md
│   └── references.bib
│
├── notebooks/
│   ├── 01_GGM_Exploration.ipynb
│   ├── 02_CI_Representation.ipynb
│   ├── 03_Elementary_Triplets.ipynb
│   ├── 04_Graphoid_Closure.ipynb
│   ├── 05_Singleton_Transitivity.ipynb
│   ├── 06_Examples_From_Papers.ipynb
│   └── 07_Graph_Reconstruction.ipynb
│
├── src/
│   └── aim/
│       ├── __init__.py
│       ├── ci.py
│       ├── independence_model.py
│       ├── elementary.py
│       ├── graphoid.py
│       ├── singleton.py
│       ├── graph.py
│       ├── io.py
│       └── utils.py
│
├── tests/
│   ├── test_ci.py
│   ├── test_elementary.py
│   ├── test_graphoid.py
│   ├── test_singleton.py
│   └── test_examples.py
│
├── examples/
│   ├── lauritzen/
│   ├── sadeghi/
│   └── studeny/
│
├── data/
│
└── reports/
    ├── Progress_Report_01.pdf
    └── figures/
```

## Current Status

✅ Literature review

✅ GGM package exploration

⬜ Independence model library

⬜ Closure algorithms

⬜ Graph reconstruction

## References

Lauritzen (1996)

Studený (2005)

Sadeghi (2024)
