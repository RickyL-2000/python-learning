# %%
import nltk
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords, wordnet
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

import time

# %%
# download packages
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

# %%
if __name__ == '__main__':

    # %%
    # read text
    with open("Sherlock_Holmes.txt", "r") as f:
        content = f.read()

    # %%
    # preprocess
    content = content.lower()
    puncts = '\\\'~`!@#$%^&*()-_=+[]{}|;:",./<>?'
    for char in puncts:
        content = content.replace(char, ' ')

    # %%
    # tokenize
    tokens = word_tokenize(content)
    print("#tokens:", len(tokens))

    # %%
    # stemming
    stemmer = PorterStemmer()   # use porter stemmer to stem the words
    for i in range(len(tokens)):
        tokens[i] = stemmer.stem(tokens[i])

    # %%
    # pos tagging
    pos_tags = nltk.pos_tag(tokens)
    pos_tags = dict(pos_tags)

    def get_pos(tag):
        # make the POS tags lemmatizer-friendly
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

    # %%
    # Lemmatization
    wordnet_lemmatizer = WordNetLemmatizer()
    for i in range(len(tokens)):
        if get_pos(pos_tags[tokens[i]]):    # if not, it's other words, like articles
            tokens[i] = wordnet_lemmatizer.lemmatize(tokens[i], pos=get_pos(pos_tags[tokens[i]]))

    # %%
    # eliminate stopwords
    def eliminate_stopwords(tokens, __stopwords):
        print("start filtering stopwords...")
        filtered = []
        t_begin = time.time()
        for i, w in enumerate(tokens):
            if w not in __stopwords:
                filtered.append(w)
            print(f"\r{i}/{len(tokens)}  time:{time.time() - t_begin: .3f}s", end='')
        return filtered
    
    filtered = eliminate_stopwords(tokens, stopwords.words('english'))
    print("\n#tokens after filtering:", len(filtered))

    # %%
    # eliminate customized stopwords
    stopwords_customized = set(stopwords.words('english'))
    stopwords_customized = stopwords_customized.union(set(['ok', 'sure', 'no', 'yes', 'yeah', 'so', 'laptop', 'suck', 'desk', 'gun']))
    filtered_customized = eliminate_stopwords(filtered, stopwords_customized)
    print("\n#tokens after filtering custmoized stopwords:", len(filtered_customized))

    # %%
    # freq stats
    print("10 most frequent word:")
    freq_dist = nltk.FreqDist(filtered_customized)  # count appearance
    freq_top10 = freq_dist.most_common(10)
    for (w, f) in freq_top10:
        print(f"{w}: {f}")

    # %%
    # output csv
    with open("word_freq.csv", "w") as file:
        file.write("word,freq\n")
        for (w, f) in freq_dist.items():
            if f > 3:
                file.write(f"{w},{f}\n")

