import string, re

# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

def filter_words(words, skip_words):
    for skip_word in skip_words:
        for word in words:
            if word == skip_word:
                words.remove(word)
    return words

def remove_punct(text):
    text = re.sub(r'[^\w\s]','',text) #remove punctuation via regex
    return text

def normalise_input(user_input):
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    #split string into individual words
    split_string = no_punct.split()
    #filter out words
    filtered_string = filter_words(split_string, skip_words)
    #return filtered_string
    return filtered_string
