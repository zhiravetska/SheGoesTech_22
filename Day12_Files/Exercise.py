# Exercise
# read text from  sherlock_holmes_adventures.txt

import os  # system library
import string
from datetime import datetime as dt  # datetime has datetime submodule(klase)
from pathlib import Path

fstream = open("Day12_File_Operations/frost.txt", "r")
# reading mode is implied, instead of fstream we can use f or anything else
with open("Day12_File_Operations/frost.txt", encoding="utf-8") as fstream:
    text = fstream.read()

print(text)
# encoding="utf-8

# 1a


def file_line_len(fpath):
    fll = 1
    with open(fpath, encoding="utf-8") as fpath:
        for _ in fpath:
            fll += 1
        print(fll)
        return fll


file_line_len(fpath="Day12_File_Operations/frost.txt")

# 1b

# print(lines_without_newline)


def get_text_lines(fpath):
    lines_withn = [text.rstrip("\n") for line in fpath]
    print(lines_withn)
    # text_lines = list()
    # for line in fpath:
    #     if "\n" in line:
    #         text_lines = text_lines.append(line)
    #     print(text_lines)
    #     return text_lines


get_text_lines(fpath="Day12_File_Operations/frost.txt")
# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file

# check file_line_len("sherlock_holmes_adventures.txt") -> 12305

# 1b -> write the function get_text_lines(fpath), which returns a list with only those lines that contain text.

# So we want to avoid/filter out those lines that contain whitespace

# PS preferably use encoding = "utf-8" when reading

# 1c -> write the function save_lines(destpath, lines)

# This function will store all lines into destpath file

# 1d -> call save_lines with destpath being "pure_sherlock.txt" and lines being the text lines we cleaned from 1b

# 1e -> write the function clean_punkts(srcpath, destpath)

# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")

# 1f -> write the function get_word_usage(srcpath, destpath)

# The function opens the file and finds the most frequently used words

# recommendation to use Counter module!

# assume that the words are separated by either whitespace or newline (the good old split will come in handy)

# the saved list of words and frequency should be saved in destpath in the following form:

# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary
