import pandas as pd
import os
import Levenshtein
import json


#Read in data:
os.chdir(r"C:\Users\tjgry\PycharmProjects\GT_Visual_Analytics\Final_Project")
##https://www.kaggle.com/datasets/leite0407/list-of-nouns?resource=download

nouns = pd.read_csv("nounlist.csv",header=None)

#Clean Data
nouns.columns = ["nouns"]
nouns_list = nouns["nouns"].to_list()

#Write Functions

def cosine_sim_vectors(vec1,vec2):
    vec1 = vec1.reshape(1,-1)
    vec2 = vec2.reshape(1,-1)
    return cosine_similarity(vec1,vec2)[0][0]



#Get Cosine Similarity Between Words

my_dictionary = dict()

for x in range(len(nouns_list)):
    my_dictionary[nouns_list[x]] = {}
    for y in range(len(nouns_list)):
        if x == y:
            continue
        else:
            # print(Levenshtein.distance(nouns_list[x],nouns_list[y]))
            my_dictionary[nouns_list[x]][nouns_list[y]] = Levenshtein.distance(nouns_list[x],nouns_list[y])

    my_dictionary[nouns_list[x]] = sorted(my_dictionary[nouns_list[x]].items(), key=lambda x: x[1])
    my_dictionary[nouns_list[x]] = my_dictionary[nouns_list[x]][:3]


with open("Levenshtein.json", "w") as outfile:
    json.dump(my_dictionary, outfile)


outfile.close()
