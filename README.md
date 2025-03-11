# Dominant Variation Checker for MCDM Models

This repository contains a Python script that checks for **variant domination** in **Multiple-Criteria Decision-Making (MCDM) models**.

## Description

The script compares different variants based on a given **criterial matrix** and a **criteria nature vector** (defining whether each criterion should be maximized or minimized). A variant is **dominated** if another variant is equal or better in all criteria and strictly better in at least one.

## Usage

1. Define your **criterial matrix** (list of variants with their criteria values).
2. Define the **criteria nature vector** (`'max'` for criteria to maximize, `'min'` for criteria to minimize).
3. Run the script to get the list of **dominated variants**.

### Example

```python
data = [
    [9990, 901385, 8, 0.7854, 193.5, 4385],
    [4999, 435275, 12, 0.8345, 192, 6000],
]

vec_criteria = ['min', 'max', 'max', 'max', 'min', 'max']

dominated_variants = find_dominated_variants(data)
print("Dominated Variants:", sorted(dominated_variants))
