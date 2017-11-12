
# coding: utf-8

# In[4]:


#Read in the texts of the State of the Union addresses, using the state_union corpus reader. 
#Count occurrences of men, women, and people in each document. What has happened to the 
#usage of these words over time?

import nltk

cfd = nltk.ConditionalFreqDist(
    (address, word)
    for address in nltk.corpus.state_union.fileids()
    for word in nltk.corpus.state_union.words(fileids=address))

addresses = ["1945-Truman.txt", "1946-Truman.txt", "1947-Truman.txt", "1948-Truman.txt", "1949-Truman.txt",
"1950-Truman.txt",
"1951-Truman.txt",
"1953-Eisenhower.txt",
"1954-Eisenhower.txt",
"1955-Eisenhower.txt",
"1956-Eisenhower.txt",
"1957-Eisenhower.txt",
"1958-Eisenhower.txt",
"1959-Eisenhower.txt",
"1960-Eisenhower.txt",
"1961-Kennedy.txt",
"1962-Kennedy.txt",
"1963-Johnson.txt",
"1963-Kennedy.txt",
"1964-Johnson.txt",
"1965-Johnson-1.txt",
"1965-Johnson-2.txt",
"1966-Johnson.txt",
"1967-Johnson.txt",
"1968-Johnson.txt",
"1969-Johnson.txt",
"1970-Nixon.txt",
"1971-Nixon.txt",
"1972-Nixon.txt",
"1973-Nixon.txt",
"1974-Nixon.txt",
"1975-Ford.txt",
"1976-Ford.txt",
"1977-Ford.txt",
"1978-Carter.txt",
"1979-Carter.txt",
"1980-Carter.txt",
"1981-Reagan.txt",
"1982-Reagan.txt",
"1983-Reagan.txt",
"1984-Reagan.txt",
"1985-Reagan.txt",
"1986-Reagan.txt",
"1987-Reagan.txt",
"1988-Reagan.txt",
"1989-Bush.txt",
"1990-Bush.txt",
"1991-Bush-1.txt",
"1991-Bush-2.txt",
"1992-Bush.txt",
"1993-Clinton.txt",
"1994-Clinton.txt",
"1995-Clinton.txt",
"1996-Clinton.txt",
"1997-Clinton.txt",
"1998-Clinton.txt",
"1999-Clinton.txt",
"2000-Clinton.txt",
"2001-GWBush-1.txt",
"2001-GWBush-2.txt",
"2002-GWBush.txt",
"2003-GWBush.txt",
"2004-GWBush.txt",
"2005-GWBush.txt",
"2006-GWBush.txt"]
words = ["men", "women", "people"]
cfd.tabulate(conditions=addresses, samples=words)



#for x in nltk.corpus.state_union.fileids():
#    print(x)
##    num_words = len(nltk.corpus.state_union.words(x))
#    num_men = len(w.lower() for w in nltk.corpus.state_union.words(x))
#    print(num_words)

