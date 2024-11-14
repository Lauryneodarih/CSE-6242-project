import nltk
from nltk.corpus import wordnet
# nltk.download('wordnet')
import pandas as pd
import os
import Levenshtein
import json


def get_synonyms(synsets):
    synonyms = list()
    antonyms = list()
    deriv_forms = list()
    definitions = list()
    usages = list()
    for synset in synsets:
        # Get synonyms for each lemma inside each synset
        for lemma in synset.lemmas():
            if lemma.name() not in synonyms:
                synonyms.append(lemma.name())
            if lemma.antonyms():  # Antonyms are not always present
                if lemma.antonyms()[0].name() not in antonyms:
                    antonyms.append(lemma.antonyms()[0].name())
            if lemma.derivationally_related_forms():
                if lemma.derivationally_related_forms()[0].name() not in deriv_forms:
                    deriv_forms.append(lemma.derivationally_related_forms()[0].name())
        # Get definitions for each synset
        if synset.definition() and (synset.definition() not in definitions):
            definitions.append(synset.definition())
            # Get examples for the first synset only
    if synsets[0].examples():
        usages = synsets[0].examples()

    # Generate some output:
    print(f'The word {txt} has {len(synonyms)} synonym(s):', synonyms)
    print(f'The word {txt} has {len(antonyms)} antonyms(s):', antonyms)
    print(f'The word {txt} has {len(deriv_forms)} derivationally related form(s):', deriv_forms)
    print(f'There are {len(definitions)} definitions of {txt}:')
    for definition in definitions:
        print('    -', definition)
    print(f'Here are some examples of {txt} usage:')
    for usage in usages:
        print('    -', usage)

    # vocal.derivationally_related_forms()

txt = "happy"
synsets = wordnet.synsets(txt)

get_synonyms(synsets)


def get_synonyms_2(synsets):
    synonyms = list()
    antonyms = list()
    deriv_forms = list()
    definitions = list()
    usages = list()
    for synset in synsets:
        # Get synonyms for each lemma inside each synset
        for lemma in synset.lemmas():
            if lemma.name() not in synonyms:
                synonyms.append(lemma.name())
            if lemma.antonyms():  # Antonyms are not always present
                if lemma.antonyms()[0].name() not in antonyms:
                    antonyms.append(lemma.antonyms()[0].name())
            if lemma.derivationally_related_forms():
                if lemma.derivationally_related_forms()[0].name() not in deriv_forms:
                    deriv_forms.append(lemma.derivationally_related_forms()[0].name())
        # Get definitions for each synset
        if synset.definition() and (synset.definition() not in definitions):
            definitions.append(synset.definition())
            # Get examples for the first synset only
    if synsets[0].examples():
        usages = synsets[0].examples()

    # Return synonyms
    return synonyms


txt = "happy"
synsets = wordnet.synsets("happy")


get_synonyms_2(wordnet.synsets("happy"))[1:]




os.chdir(r"C:\Users\tjgry\PycharmProjects\GT_Visual_Analytics\Final_Project")
##https://www.kaggle.com/datasets/leite0407/list-of-nouns?resource=download

nouns = pd.read_csv("nounlist.csv",header=None)

#Clean Data
nouns.columns = ["nouns"]
nouns_list = nouns["nouns"].to_list()


#Get Synonyms Between Words

my_dictionary = dict()

for x in range(len(nouns_list)):
    my_dictionary[nouns_list[x]] = {}
    # print(Levenshtein.distance(nouns_list[x],nouns_list[y]))
    try:
        my_dictionary[nouns_list[x]] = get_synonyms_2(wordnet.synsets(nouns_list[x]))[1:]
    except IndexError:
        continue


with open("Synonym.json", "w") as outfile:
    json.dump(my_dictionary, outfile)


outfile.close()
