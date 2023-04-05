import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import re
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
words = set(nltk.corpus.words.words())


# Does lots of basic cleaning
# Input: Sentence as string
# Output: Tokenized words as string
def preprocess(sentence: str):
    sentence = str(sentence)
    sentence = sentence.lower()
    sentence = sentence.replace('{html}', "")
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', sentence)
    rem_url = re.sub(r'http\S+', '', cleantext)  # Remove URLs
    rem_symbol = re.sub('[^A-Za-z ]+', '', rem_url)  # Only keep alphabets
    english_only = " ".join(w for w in nltk.wordpunct_tokenize(rem_symbol)
                            if w.lower() in words or not w.isalpha())  # Remove  non-english words
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(english_only)
    filtered_words = [w for w in tokens if len(
        w) > 2 if not w in stopwords.words('english')]
    stem_words = [stemmer.stem(w) for w in filtered_words]
    lemma_words = [lemmatizer.lemmatize(w) for w in stem_words]
    return " ".join(lemma_words)


# Pre-processing to extract the main category by removing the subcategories
def trimmer(x): return x.split(">", 1)[0]


# print(trimmer('Sweets, Chocolate & Gum > Chocolate > Bars > Multipack Bars'))
# print(preprocess('FunkyBuysÂ® larger lego star wars largely Large fun funny dance dancer toy toys large Christmas Holiday Express Festive Train Set (SI-TY1017) Toy Light / Sounds / batteries batteries Batteries battery batterys Operated & Smoke'))
