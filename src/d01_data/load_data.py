import pandas as pd
import numpy as np 
import configparser


def read_csv(path):
    return pd.read_csv(path)

def load_data():

    # Get data from .csv files

    config = configparser.ConfigParser()
    config.read('../config.ini')

    books_csv_url = config['URL Raw']['books']
    users_csv_url = config['URL Raw']['users']
    ratings_csv_url = config['URL Raw']['ratings']

    df_books = read_csv(books_csv_url)
    df_users = read_csv(users_csv_url)
    df_ratings = read_csv(ratings_csv_url)

    return {
        'df_books': df_books,
        'df_users' : df_users,
        'df_ratings' : df_ratings
    }
    

if __name__ == '__main__':
    load_data()