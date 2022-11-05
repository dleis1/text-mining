import urllib.request
from thefuzz import fuzz
import string
import nltk

# downloading the book from projectgutenberg.org

def get_book():
    """
    This function loads the books from 
    projectgutenberg.org specified below using their URL
    """
    
    url = 'https://www.gutenberg.org/files/2638/2638-0.txt'  
    # The Idiot by Fyodor Dostoyevsky
    with urllib.request.urlopen(url) as f:
        response = urllib.request.urlopen(url)
        data = response.read()  # a `bytes` object
        book = data.decode('utf-8')
        #print(book) # for testing

    return book

#------------------------------------------------------------------------

# Now, we modify the data for further analysis

# 1. Removing the header 

def remove_header():
    """
    This function uses an imported gutenberg_cleaner package to simplify the process of 
    erasing uncessary data before analyzing it.
    """
    from gutenberg_cleaner import simple_cleaner
    # source: https://github.com/kiasar/gutenberg_cleaner
    """
    This function removes the header and end text inserted by projectgutenberg.org 
    """

    book_raw = get_book()
    book_cleaned = simple_cleaner(book_raw)

    return book_cleaned

# 2. Removing stop words

def delete_stopwords():
    """
    This function removes punctuation as well as stopwords from the downloaded text;
    """
    # resource for this code was https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
    nltk.download('stopwords')
    nltk.download('punkt')
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from string import punctuation

    stop_words = set(stopwords.words('english'))
    punctuation = list(punctuation)
    punctuation.append('-')
    punctuation.append('“')
    punctuation.append('”')
    punctuation.append('’')
    punctuation.append('‘')
    
    #print(stop_words) 
    #print(punctuation) 
    # double-checking the list of stopwords that we shouldn't see in output

    book = remove_header()

    word_tokens = word_tokenize(book)

    filtered_sentence = []

    for w in word_tokens:
        if w.lower() not in stop_words and w not in punctuation:
            filtered_sentence.append(w)

    return filtered_sentence

#------------------------------------------------------------------------

# Now, we may analyze and interpret data

# 1. Basic generic information

def total_words():
    """
    Returns the total number of non-generic words used in the book; 
    """
    hist = delete_stopwords()
    total = 0
    for freq in hist.values():
        total += freq
    return (f"The total number of words in the text is {total}")

def frequencies():
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    """
    This function prints a dictionary with all the words in the book; 
    Then, the function sorts words in the descending order of frequency 
    and returns the 20 most used words;
    Lastly, the fucntion prints the sentiment analysis;
    """
    freq = {}
    sorted_list = [] # sorted by frequency
    top_20 = []
    fitered_sentences = delete_stopwords()

    for item in fitered_sentences:
        freq[item] = freq.get(item, 0)+1

    print(freq)

    for word, frequency in freq.items():
        sorted_list.append((frequency, word))
            
    sorted_list.sort(reverse=True)

    sorted_list_20 = sorted_list[0:20]

    for freq, word in sorted_list_20:
        top_20.append(word)

    book = remove_header()
    score = SentimentIntensityAnalyzer().polarity_scores(book)
           
    return (f"The 20 most frequenntly used words in the text are: {top_20}. The sentiment score for the text is:{score}")

#print(frequencies())
        
def main():
    book1 = get_book()
    url = 'https://www.gutenberg.org/cache/epub/1399/pg1399.txt'
    # Anna Karenina by Leo Tolstoy
    with urllib.request.urlopen(url) as f:
        response = urllib.request.urlopen(url)
        data = response.read()  # a `bytes` object
        book2 = data.decode('utf-8')

    print(f"The fuzz ratio between the two texts is {fuzz.ratio(book1, book2)}")

    print(frequencies())


if __name__ == '__main__':
    main()
