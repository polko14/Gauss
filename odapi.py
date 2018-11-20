from requests import get
import json
import sys
import os
#program uruchamiamy komendą w konsoli: python odapi.py<tekst.txt>out.txt, gdzie tekst.txt jest dowolnym plikiem tekstowym
ROOT_URL="https://od-api.oxforddictionaries.com:443/api/v1/"
LANGUAGE="en"
ENTRIES_URL=ROOT_URL+"entries/"+LANGUAGE+"/"
credentials={"app_id":os.environ["APP_ID"], "app_key":os.environ["APP_KEY"]}
#APP_ID i APP_KEY należy ustawić w konsoli komendą set na wartości otrzymana po założenia konta w API oxford dictionaries
def get_definition(word):
    word_r=get(ENTRIES_URL+word.lower(),headers=credentials)
    if word_r.status_code<400:
        return word_r.json()
    else:
        return word_r.status_code

def get_synonyms(word):
    word_r=get(ENTRIES_URL+word.lower()+"/synonyms",headers=credentials)
    if word_r.status_code<400:
        return [s["text"] for s in word_r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"]]
    else:
        return []

def get_words_frequency(text):
    result=dict()
    splited=text.replace("."," ").replace(","," ").split()
    for word in splited:
        lowerword=word.lower()
        if lowerword in result:
            result[lowerword]+=1
        else:
            result[lowerword]=1
    return result

r=sys.stdin.read()
frequencies=get_words_frequency(r)
word_synonyms=[(word,get_synonyms(word)) for word,_ in sorted(frequencies.items(),key = lambda t: -t[1])]

for word,synonyms in word_synonyms:
    if len(synonyms)>0:
        print(word+"\n"+"   {}".format("\n   ".join(synonyms)))
