# download the database only the first time.  You may need to pip install nltk, but likely not.
# nltk.download('wordnet'). 
import nltk
from nltk.corpus import wordnet


#  Quick practice
# print(wordnet.synsets('room'))
# synset = wordnet.synsets("Travel")
# print(synset)
# print('Word and Type : ' + synset[0].name())

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
txt = input("Type any single word: ")
# txt = "happy"
synsets = wordnet.synsets(txt)
# print(f"You entered the word {txt}, which has {len(synsets)} synsets")

# print('All synonyms in first synset using lemma_names', synsets[1].lemma_names())

# Get all synonyms and relevant words form wordnet
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
            if lemma.antonyms():    # Antonyms are not always present
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

get_synonyms(synsets)

# Let user try words over and over, until they write 999 
while txt != '999':
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    txt = input("Type another word or type 999 to exit: ")
    if txt == '999': 
        print('Bye now!')
        break
    # if several words, get out  
    if len(txt.split()) > 1:
        print('Sorry, I only do single words. Try again.')
        continue
    # if single word, get the synsets:
    else: 
        try: 
            synsets = wordnet.synsets(txt)
            if synsets == []: 
                print('Sorry, cannot find word in database. Try another.')
                continue 
            else: get_synonyms(synsets)
        # if word has no sysnet, get out  
        except ValueError: 
            print('This word has no entry in our database')
        