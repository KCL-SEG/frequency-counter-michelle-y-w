"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for element in items:
        key = str(element)
        if key in frequencies:
            frequencies[key] += 1
        else:
            frequencies[key] = 1
    return frequencies
