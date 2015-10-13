## Solution to part 2

- I've built a very simple code that prints 10 most popular 3-grams, you can run:

> python ngram_simple.py

- Some assumptions and pre-cleaning:

   - I assumed that this should be n-grams of words
   - I used stop-words from nltk
   - I used WikiExtractor script to clean wikipedia xml (https://github.com/attardi/wikiextractor), result saved as wiki_clean.txt (included)


- For larger amount of data I would use a MapReduce framework (using e.g. mrjob.job package) and heap queue (e.g. heapq package). 
   