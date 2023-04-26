import pandas as pd
import surprise
import nltk
import dill as pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# load saved models and files
with open('model_pkl', 'rb') as f:
    hybrid_recommender = pickle.load(f)

with open('sentence_processor.pkl', 'rb') as f:
    process_sentences = pickle.load(f)

with open('svd.pkl', 'rb') as f:
    model = pickle.load(f)

with open('wards.pkl', 'rb') as f:
    constituents_list = pickle.load(f)

with open('prices.pkl', 'rb') as f:
    price_map = pickle.load(f)

with open('content_base_r.pkl', 'rb') as f:
    contentB_recommend = pickle.load(f)

#with open('restaurants.pkl', 'rb') as f:
#    filtered_restaurant_df = pd.read_pickle(f, compression=None)


def show_recomms(words):
    print(constituents_list)
    print('\n')
    print(price_map)
    print('\n')
    query = words
    recomms = contentB_recommend(query)
    return recomms


print(show_recomms('tacos in Brooklyn'))