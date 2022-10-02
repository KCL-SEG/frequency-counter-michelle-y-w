"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {['a', 'a', 'b', 'b', 'b', 'c']}
    # Your code goes here
    dict = {}
    for key in items:
        if key not in dict.keys():
            dict.update({key: 1})
        else :
            dict[key] = dict[key] + 1
    return dict
