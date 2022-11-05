# text-mining

Please read the [instructions](instructions.md).

Write-Up:

The goal of this assignment is to analyze the writing style of one of the most famous Russian authors, Fyodor Dostoyevsky, through his book, The Idiot; 
Considering this objective, I hope to better understand the overall structure of the text (the frequency of different words used, the top 20 words used) and some other interesting statistical findings.

In this assignemnt, I use 3 different analytical techniques: word frequncy count, 
sentiment analysis, and text similarity analysis, TheFuzz (to compare it with the text of another famous Russian author - Leo Tolstoy, and his novel Anna Karenina). The first method was a result of what we 
learned in class; most of the time throughout my assignemnt, I use lists to analyse the data - 
lists are starightforward and mutable, hence, I believe, they work best. However, when it comes
to frequency count in relation to each item, dictionaries are superior due to their fundamental feature of key-value pairing, so I end up "jumping" by recording results from one data structure to another.
The last two methods I borrowed from the examples preseted in the instructions for this assignemnt
as they perfectly supported the data types I was working with.

The results, unfortunately, were less exciting then I expected them to be; the 20 most common 
words ended up being very generic, such as "like" and etc. along with some names of the main characters. 
Next time, I should definetly find a way to look for "unique" words, perhaps the ones that are the 
least used and have a certain number of letters in them. 
The sentiment analysis has determined the overall sentimnet of the text to be neutrial (neu: 0.769), which is not suprising, but still higher than I expected as I thought that the proportion of negative words would be higher. Nevertheless, I found this to be the most entertaining analysis thus far.
I was quite surprised to see the ratio of 41 for the fuzz analysis, meaning texts are more identical than I thourght initially. In reality, I think that the ratio is lower since this was the only type of analysis where I had to use Leo Tolstoy's text as raw data (meaning, with Gutenberg Project's headers and footers) even though I compare it with the text that has no headers and footers (book1 = remove_header()).

Reflection:
To be completely honets, even though my assigement lacks analytical techniques, I am very proud with myself in relation to how I mamanged to clean the data. For over a week I was tedeously searching through the internet to find a more efficient way to get rid of stopwords (even though NLTK was tremendous help, I had to take the matter into my own hands and update the punctuation list with punctuations, which otherwise would be left undetetcted by the program). As a result, I was able to get clean outputs and get dictionaries without annoying " ' " and stopwords like "He". 

Unfortunately, I did overestimate myself; by the time when most of the code was written, I've decided to compare it with Leo Tolstoy's book called Anna Karenina. I thought it would be easy to add a second text for further comparison analysis, howver, due to the structure of my code, I couldn't run it through the same algorithm as I used for The Idiot; hence, I ended up downloading the text in my main function and conducting similarity analysis there, without cleaning the data and perfroming any other analysis as with the book The Idiot. I clearly undertsand now that this was a result of me not clearly establishing my goals beofre writing the code - a lesson I've learned for certain when working in my future coding projects. 

