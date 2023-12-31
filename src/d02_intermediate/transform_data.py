import pandas as pd
import numpy as np 

from d01_data.load_data import load_data
from d00_utils.contains_letters import contains_letters


def books_data_treatment(df):
    
    # Data cleaning 
    # ISBN should contain only numbers
    df = df[~df['ISBN'].apply(lambda x: not contains_letters(x))]
    
    # Clean year of publication column
    df['Year-Of-Publication'] = pd.to_numeric(df['Year-Of-Publication'], errors='coerce').fillna(0).astype(int)
    
    # Keep ISBN length in order to keep the same length in ratings data
    df['ISBN_length'] = df['ISBN'].str.len()
    df_books_len_list = df['ISBN_length'].unique().tolist()
    breakpoint()
    df.drop(['ISBN_length','Image-URL-S', 'Image-URL-M', 'Image-URL-L'], axis =1, inplace=True)
    
    return{
        'df_books_intermediate' : df,
        'df_isbn_len_list' : df_books_len_list
    }
    
def users_data_treatment(df):
    
    # Data transformation
    # Split location column in 3 columns : city, department, country

    df['location_city'] = df['Location'].str.split(',', expand=True)[0]
    df['location_department'] = df['Location'].str.split(',', expand=True)[1]
    df['location_country'] = df['Location'].str.split(',', expand=True)[2]

    # Data transformation
    # Cast age type into int

    df['Age'] = pd.to_numeric(df['Age'], errors='coerce').fillna(0).astype('Int64')

    df.drop(['Location'], axis=1, inplace=True)
    
    return df
    
def ratings_data_treatment(df, isbn_allow_len_list):
    
    # Data transformation
    # Delete values where ISBN contains letters. It should contains only numbers

    df = df[~df['ISBN'].apply(lambda x: not contains_letters(x))]


    # Delete values where ISBN lenght not correspond to the ones foundo on book dataset

    df = df[df['ISBN'].str.len().apply(lambda x: x in isbn_allow_len_list)]
    
    return df

    

