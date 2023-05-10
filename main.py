# ---------------------------------------------------
# File Name: SolvehiveNYT
# Created by: Spencer Shore
# Created on: 11/15/2022???
# Synopsis: A program that analyzes the words to the
#           given day's hive puzzle and outputs a list
#           of valid solutions in order of most
#           frequently used to least
# ---------------------------------------------------

import pandas as pd
import numpy as np


def load_words():
    with open('words_fixed.txt') as words_file:
        valid_words = set(words_file.read().split())
    return valid_words


def check_string(string, remaining_letters):
    if len(string) < 4:
        return False

    for char in string:
        if char not in remaining_letters:
            return False
    return True


words = load_words()
df = pd.read_csv('unigram_freq.csv')
df.reset_index(inplace=True, drop=True)
arr = df.to_numpy()

print('This is a solver for the NYT Hive letter puzzle')
input('Press enter to begin...')

# get key letter from user
key = input('Input the key letter for today\'s hive: ')

# pull only the words that contain the key letter
words_with_key = [w for w in words if key in w]

# get remaining letters from user and save to list
remaining = input('Input the remaining letters (press the \'enter\' key when you are done): ')

valid_words = []
for word in words_with_key:
    if check_string(word, remaining + key):
        valid_words.append(word)

# Attach valid words to frequencies
words_frequencies = []
for word in valid_words:
    if word in arr:
        index = np.where(arr == word)
        index = index[0][0]
        words_frequencies.append([word, arr[index][1]])

# Sort words based on frequency
words_final = sorted(words_frequencies, key=lambda row: row[1], reverse=True)

for row in words_final:
    print(row[0])
