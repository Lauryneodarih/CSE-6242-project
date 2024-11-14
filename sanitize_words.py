# https://en.lexipedia.org/ - greater than 500 Frequency & max length of 30
import pandas as pd
import os
import nltk

script_path = (os.path.dirname(os.path.realpath(__file__)))
highFreqWords = pd.read_csv(script_path+"/../data/en_words_500_1-30.csv")

# only keep english words from our list
words = highFreqWords['word'].dropna().astype(str).apply(lambda x: x.lower()).tolist()
english_words = nltk.corpus.words.words()
english_high_freq_words = set(words) & set(english_words)

df = pd.DataFrame(english_high_freq_words)
df.to_csv(script_path+"/../data/englishwords.csv",header=False, index=False)
# print(words)