
# coding: utf-8

# In[12]:


#Use the corpus module to explore austen-persuasion.txt. How 
#many word tokens does this book have? How many word types?

import nltk
from nltk.corpus import gutenberg
persuasion = gutenberg.words('austen-persuasion.txt')
persuasionTypes = len(set(w.lower() for w in persuasion))
print("word tokens:" + " " + str(len(persuasion)))
print("word types (unique words):" + " " + str(persuasionTypes))

