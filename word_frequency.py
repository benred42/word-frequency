import sys
import re



def scrub_text(filepath):
    """Takes the text of a file, removes newlines and punctuation,
    and lowercases the text.

    Keyword Arguments:
    filepath -- the path to the file you wish to use
    """

    with open(filepath) as file:
        scrubbed_file = file.read()
        scrubbed_file = re.sub(r'[\s]+', ' ',scrubbed_file)
        #^replaces whitespace chars w/single space
        scrubbed_file = re.sub(r'[^A-Za-z ]', '',scrubbed_file)
        #^replaces all non-alpha and spaces with ""
        scrubbed_file = scrubbed_file.lower()

        return scrubbed_file

###############################################################################

def get_words(filepath):
    """Takes the text of a file and returns a list of every word found in the file.

    Keyword Arguments:
    filepath -- the path to the file you wish to use
    """

    clean_string = scrub_text(filepath)
    words = clean_string.split()

    return words

###############################################################################

def common_word_screen(filepath):
    """Takes the text of a file and returns all the words from that file except
    for words that are very commonly used.

    Keyword Arguments:
    filepath -- the path to the file you wish to use
    """

    words = []
    all_words = get_words(filepath)
    words_to_skip = ['a', 'able', 'about', 'across', 'after', 'all', 'almost',
     'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be',
     'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did',
     'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get',
      'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how',
      'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just',
      'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must',
      'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on',
      'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says',
      'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the',
      'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to',
      'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when',
      'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with',
      'would', 'yet', 'you', 'your']


    for word in all_words:
        if word not in words_to_skip:
            words.append(word)

    return words

###############################################################################

def top_20(a_dict):
    """Take a dictionary, sorts it in descending order by value, and returns
    a list of the top 20 key/value pairs

    Keyword Arguments:
    a_dict -- input dictionary
    """


    top_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    top_20_list = top_list[:20]
    return top_20_list

###############################################################################

def normalize_histogram(a_list, normalize_to=50):
    """Takes a descending-sorted list where each item is a pair
    of the form ["item", frequency] and determines a  divisor that can be used
    to normalize the remaining values to a given maximum.

    Keyword Arguments:
    a_list -- the list of value pairs to normalize
    normalize_to -- the maximum value to normalize to (default: 50)
    """

    divisor = a_list[0][1]/normalize_to
    return divisor

###############################################################################

def print_table(a_list):
    """Takes a descending-sorted list where each item is a pair
    of the form ["item", frequency] and prints out a table with "item" on
    the left and a normalized histogram bar representing the frequency on
    the right.

    Keyword Arguments:
    a_list -- the list of value pairs to make a table from
    """

    for index in a_list:
        print(index[0].ljust(20), "|".center(1),
        ("#"*(int(index[1]//normalize_histogram(a_list)))).rjust(1))

###############################################################################

def word_frequency(filepath):
    """Takes a filepath and creates a dictionary of every unique word
    found in the file and the number of times it appears (in the
    form {word: frequency})

    Keyword Arguments:
    filepath -- the path to the file you wish to use
    """

    words = common_word_screen(filepath)
    #takes the text from the file and retrieves all the words from it
    #sans those that are exceedingly common in English

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        #determines the frequency of each word and populates a dictionary with
        #key:value pairs of the form <"word":frequency>

    most_freq = top_20(freq)
    #creates a list from the given dict of the top 20 most frequent words where
    #each item in the list is a list of the form ["word", frequency]

    print_table(most_freq)

###############################################################################


if __name__ == '__main__':
    word_frequency(sys.argv[1])
