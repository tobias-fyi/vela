"""
Graphs :: Day 3

Given two words (begin_word and end_word), and a dictionary's word list,
return the shortest transformation sequence from begin_word to end_word,
such that:

* Only one letter can be changed at a time.
* Each transformed word must exist in the word list.
  * Note that begin_word is not a transformed word.

Note:

* Return None if there is no such transformation sequence.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume begin_word and end_word are non-empty and are not the same.

Sample:
    begin_word = "hit"
    end_word = "cog"
    return: ['hit', 'hot', 'cot', 'cog']
    begin_word = "sail"
    end_word = "boat"
    ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
    beginWord = "hungry"
    endWord = "happy"
    None
"""

# %%
import os
import sys

sys.path.append(os.path.abspath("../graph"))
from graph import Graph
from util import Stack, Queue

# %%
with open("words.txt") as f:
    words = f.read().split()

# %%
def word_ladder(start, end, dictionary):
    graph = Graph()
    for iv, vert in dictionary:
        # Add word to graph
        if len(vert) == len(word):
            graph.add_vertex(vert)
        vert_set = set()
        for ii, ngbr in dictionary[iv:]:
            # Each word adds as its neighbor other words one transform away
            pass
    pass

# %%
# A solution

word_set = set()
for word in words:
    word_set.add(word.lower())



def get_neighbors(word):
    neighbors = []
    string_word = list
    for i in range(len(string_word)):
        for letter in alphabet:

def find_word_ladder(begin, end):
    visited = set()
    # Basically like a breadth first search
