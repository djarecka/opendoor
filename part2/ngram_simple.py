from collections import defaultdict
import re
import pdb
import nltk

WORD_RE = re.compile(r"\w+", re.UNICODE)
Stop_words = nltk.corpus.stopwords.words('english')
N = 3

# openning wikipedia xml (cleaned using Wiki Extractor)
with open("wiki_clean.txt", "r") as f:
    line_url = f.readline()
    content = f.read().decode("utf8")

# creating a list of words    
words = [word.lower() for word in WORD_RE.findall(content)
         if word.lower() not in Stop_words]
    
# buolding ngrams
ngram_counts = defaultdict(int)
for i in range(len(words)):
    if i + N <= len(words):
        ngram = ' '.join(words[i:i + N])
        ngram_counts[ngram] += 1
                                                                    
most_pop = [(k, ngram_counts[k]) for k in
            sorted(ngram_counts, key=ngram_counts.get, reverse=True)][:10]

print most_pop
