import pandas as pd
import surprise
from surprise import Reader, Dataset, SVD, accuracy
from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# load saved models and files

with open('content_based.pkl', 'rb') as f:
    contentB_recommend = pickle.load(f)

with open('model_pkl', 'rb') as f:
    hybrid_recommender = pickle.load(f)

with open('sentence_processor.pkl', 'rb') as f:
    process_sentences = pickle.load(f)

#with open('svd.pkl', 'rb') as f:
#    hybrid_recommender = pickle.load(f)

with open('wards.pkl', 'rb') as f:
    constituents_list = pickle.load(f)

with open('prices.pkl', 'rb') as f:
    price_map = pickle.load(f)

with open('restaurants.pkl', 'rb') as f:
    filtered_restaurant_df = pd.read_pickle(f, compression=None)


def show_recomms(description):
    print(constituents_list)
    print('\n')
    print(price_map)
    print('\n')
    #with open('content_based.pkl', 'rb') as file:
    #    contentB_recommend = pickle.load(file)
    recomms = hybrid_recommender(0, description)
    return recomms


print(show_recomms('for tacos'))
