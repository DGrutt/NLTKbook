
# coding: utf-8

# In[17]:


#Use the Brown corpus reader nltk.corpus.brown.words() or the 
#Web text corpus reader nltk.corpus.webtext.words() to access 
#some sample text in two different genres.

from nltk.corpus import webtext
#for fileid in webtext.fileids():
#    print(fileid)
    
print("first:" + " " + webtext.raw('grail.txt')[0:500] + "\n")
print("second:" + " " + webtext.raw('wine.txt')[0:500])



