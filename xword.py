#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Meagan Ramey"
# YOUR HELPER FUNCTION GOES HERE


def word_search(word, word_dict):
    word_list = []
    for w in word_dict:
        if len(w) == len(word):
            word_list.append(w)
    for i, char in enumerate(word):
        if char != ' ':
            word_list = [w for w in word_list if w[i] == char]
    for w in word_list:
        print(w)


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        '''Please enter a word to solve.\nUse spaces to signify unknown letters:
        ''').lower()

    word_search(test_word, words)


if __name__ == '__main__':
    main()
