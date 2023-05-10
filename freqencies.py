import pandas as pd
import numpy as np

df = pd.read_csv('unigram_freq.csv')
df.reset_index(inplace=True, drop=True)
arr = df.to_numpy()

f = open('final_list.txt', 'r')

f_words = np.array([f.read().split()][0])

words_with_frequencies = []

# Attach valid words to frequencies
for word in f_words:
    if word in arr:
        index = np.where(arr == word)
        index = index[0][0]
        words_with_frequencies.append([word, arr[index][1]])

# Sort words based on frequency
words_final = sorted(words_with_frequencies, key=lambda row: row[1], reverse=True)
print(words_final)
