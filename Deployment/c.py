import sqlite3
import pandas as pd


#create connection
conn = sqlite3.connect('restaurant_recommender.db')
cursor = conn.cursor()

#read from db table
df = pd.read_sql("SELECT * FROM restaurants", conn)

def default_recommendations(df):
    random_samples = df.sample(n = 10, replace = True)
    return random_samples

