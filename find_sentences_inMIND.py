import pprint 
from pprint import pprint as pp
import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
import json
import pandas as pd
import numpy as np


# Choose the files to use: 
# Words: 
words_filepath = "../data/englishwords.csv"
# Texts to extract sentences from: 
texts_filepath = "../data/news_mini.tsv"

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


# ================ Extracting the MIND text =================================
mind_raw =pd.read_csv(texts_filepath,sep='\t')  # <10 MB
# mind_raw =pd.read_csv('data/news.tsv',sep='\t') # 90 MB
print(len(mind_raw))
print(mind_raw[1:10000])
mind_raw.columns = ["id", "type", "subtype", "title", "text", "link", "other", "whatever"]
print(mind_raw[1:10000])

mind_text = mind_raw[['text']].to_numpy()

# Make it into individual sentences
sentences = []
for sentence in mind_text:
    extracted = str(sentence[0])
    toksent = tokenizer.tokenize(extracted.strip())
    sentences.extend(toksent)



# # Find sentences from a split book
# def get_quotes_from_split(word, sentences, max = 5, max_length = 120):
#     word_with_spaces = ' '+ word + ' '
#     quotes = [str(sentence) for sentence in sentences if (word_with_spaces in sentence and len(sentence) <= max_length)] 
#     if len(quotes) >= max:
#         out = quotes[0:max]
#     else: out = quotes 
#     return out

def get_1quote_from_split(word, sentences, max_length = 120):
    word_with_spaces = ' '+ word + ' '
    quote = "No example found"
    for sentence in sentences: 
        if (word_with_spaces in sentence and len(sentence) <= max_length):
            quote = str(sentence)
            continue
    return quote


# This is the file with all the words
words = pd.read_csv(words_filepath,header=None)
words.columns = ["words"]


# When practicing, keep only a fraction of the words to make it run faster: 
fraction_to_keep = 1 
keeponly = round(len(words) * fraction_to_keep) 
print('keeping only', keeponly,'words out of', len(words), 'for practice')
words_list = words["words"].to_list()[0:keeponly]

print(words_list)


# get sentences from all books
def find_usages(wordlist, text, max, max_length): 
    usages_dict = dict()
    for word in wordlist:
        usages_dict[word] = {}
        try:
            # usages_dict[word] = get_quotes_from_split(word, text, max, max_length)
            usages_dict[word] = get_1quote_from_split(word, text, max_length)
        except IndexError:
            continue
    return usages_dict

# Avoid sentences that are too long with the max_length parameter
usages_dict = find_usages(words_list, sentences, max = 1, max_length =150)

# Print if need to debug:
# pp(usages_dict)

# Show an example:
# ex = usages_dict["vacation"]
# print(ex, type(str(ex)))


with open("../data/Sentence_fromMIND_small.json", "w") as outfile:
    json.dump(usages_dict, outfile)
outfile.close()







