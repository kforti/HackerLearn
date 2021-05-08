import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")
# nlp = en_core_web_sm.load()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
stop_words = set(stopwords.words('english'))

from bs4 import BeautifulSoup
import requests
import re

def html_to_string(html):
    soup = BeautifulSoup(html)
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def load_source(path):
    text = ""
    with open(path) as f:
        for line in f:
            text += line
    return text


def preprocess(sent):
    tokens = nltk.word_tokenize(sent)
    filtered_words = [w for w in tokens if not w in stop_words]
    #sent = nltk.pos_tag(sent)
    return " ".join(filtered_words)


PATH = "/home/kevin/bin/hacker-learn/research/data/web_pages/so_0.html"

text = load_source(PATH)
text = html_to_string(text)
text = preprocess(text)

tokens = nlp(text)
count = {}
for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)
    if token.is_stop or token.is_punct or len(token.text) == 1:
        continue
    t = token.text.lower()
    if t not in count:
        count[t] = 1
        continue
    count[t] += 1

counts = [(k, v) for k, v in count.items()]

counts.sort(key=lambda x: x[1], reverse=True)
print(counts)