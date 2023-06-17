import string
import nltk
import re

nltk.download("stopwords")


# Cleans one text
def clean_one_text(text: str) -> str:
    """
    Cleans one text by removing punctuation, stopwords, and applying stemming.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.

    """

    # remove punctuation
    filter_str = string.punctuation.replace("'", "")

    new_string = text.translate(str.maketrans("", "", filter_str))
    tk = nltk.TweetTokenizer()

    s = set(nltk.corpus.stopwords.words("english"))
    # n't words
    rexp_1 = re.compile(r"n't")
    not_words = set(filter(rexp_1.findall, s))
    not_words.update(("against", "no", "nor", "not"))

    s.difference_update(not_words)

    stmr = nltk.stem.porter.PorterStemmer()
    tokens = [token for token in tk.tokenize(new_string) if token.lower() not in s]
    clean_tokens = [stmr.stem(token) for token in tokens]
    text = " ".join(clean_tokens)
    return text
