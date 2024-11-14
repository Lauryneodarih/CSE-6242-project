DESCRIPTION
 - An english word visualizer tool to help ESL learners associate similar words to each other, and learn dissociation of confusing words.

FUNCTIONALITY
 - Given a user searches for a word, we help them visualize the word usage
 - suggest words that have a negative correlation for caution
 - suggest words that have positive correlation for building context
 - show example of the word in a sentence

INSTALLATION
 - To run the scripts used by this project to generate data:
   - For all of the following please be inside the `code` folder.
   - First install requirements `pip install -r requirements.txt`
   - Download wordnet data: `python scripts/download_nltk.py`
   - Clean the list of words to exclude names/places: `python scripts/sanitize_words.py`
   - Generate Synonyms: go into scripts folder then, `python wordnet_query_get_synonyms.py`
   - Generate Near Homonyms: `python scripts/Text_Similarity.py`

DATA
 - `en_words_500_1-30.csv` generated using `en.lexipedia.org`
   - Used for our application (default)
 - `news_mini.tsv` extracted from: `https://mind201910small.blob.core.windows.net/release/MINDlarge_train.zip`
   - Candidate for searching and generating sentences
 - `Synonym.json` Used by our application to generate the word graph (positive relation)
   - Created using `wordnet_query_get_synonyms.py`
 - `Levenshtein.json` used by our application to generate the word graph (negative relation)
   - Created using `Text_Similarity.py`

LIVE APPLICATION
 - https://english.opiteq.com/

DEMO
 - https://youtu.be/EHtdGSmyjaQ

EXECUTION
 - To run locally: `python -m http.server 8000` from `code` folder. then navigate to [localhost](http://localhost:8000)
