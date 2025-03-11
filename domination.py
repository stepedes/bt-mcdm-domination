#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File name: domination.py
Created: 2025-02-17
Version: 1.0.0
Description: Checks for variant domination from criterial matrix. Compares each variant to each other by each criterion. Requires criteria nature vector.
License: CC 0 1.0, https://creativecommons.org/publicdomain/zero/1.0/deed.en
Dependencies: none
"""

def is_variant_dominated(row1, row2, vec_criteria):
    """
    Checks if row1 is dominated by row2 based on given vec_criteria.
    Definiton: row1 is dominated if row2 is equal or better in all criteria and strictly better in at least one.
    Does NOT check if row2 is dominated by row1
    """
    # debug output
    #print("comparing row1: ", row1, " with row2: ", row2, " using criterial vector: ", vec_criteria)
    
    better_or_equal = True
    strictly_better = False
    
    for i, nature in enumerate(vec_criteria):
        if nature == 'max':
            if row1[i] > row2[i]:
                better_or_equal = False
            if row1[i] < row2[i]:
                strictly_better = True
        else:  # 'min'
            if row1[i] < row2[i]:
                better_or_equal = False
            if row1[i] > row2[i]:
                strictly_better = True
    return better_or_equal and strictly_better

def find_dominated_variants(data):
    """
    Compares all variant pairs
    """
    dominated = set() #Empty set
    num_variants = len(data)
    
    for variant1 in range(num_variants):
        for variant2 in range(num_variants):
            if variant1 != variant2 and is_variant_dominated(data[variant1], data[variant2], vec_criteria):
                dominated.add(variant1 + 1)  # Adding 1 to match variant numbering
    return dominated

if __name__ == "__main__":

    # Define input data
    data = [
        [9990, 901385, 8, 0.7854, 193.5, 4385],
        [4999, 435275, 12, 0.8345, 192, 6000],
        [8599, 504808, 8, 0.5511, 173, 5000],
        [8499, 707480, 12, 0.5011, 190, 5000],
        [7499, 707480, 8, 0.5011, 190, 5000],
        [8224, 481956, 8, 0.5511, 191, 5110],
        [4490, 306996, 4, 0.5011, 194, 5000],
        [8990, 473737, 8, 0.8345, 197, 5000],
        [8490, 597658, 6, 0.6678, 209, 5000],
        [9900, 734625, 8, 0.6678, 213, 5000],
        [7989, 600986, 8, 0.5511, 187, 5100],
    ]

    # Define criteria nature vector
    vec_criteria = ['min', 'max', 'max', 'max', 'min', 'max']

    # Run program
    dominated_variants = find_dominated_variants(data)
    #Print dominated variants
    print("Dominated Variants:", sorted(dominated_variants))
