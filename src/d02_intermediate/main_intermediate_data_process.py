from src.d01_data.load_data import load_data
from d01_data.load_data import load_data
from d02_intermediate.transform_data import *
from save_int_data import save_data


def main():
    
    # Load data from raw files
    df_books, df_users, df_ratings = load_data()
    breakpoint()
    
    # Transform datasets 
    results = books_data_treatment(df_books)
    df_books_inter = results['df_books_intermediate']
    isbn_allow_len_list = results['df_isbn_len_list']
    df_users_inter = users_data_treatment(df_users)
    df_ratings_inter = ratings_data_treatment(df_ratings, isbn_allow_len_list)
    
    # Save new datasets into intermediate data 
    
    int_dfs = {
        'df_books': df_books_inter, 
        'df_users': df_users_inter, 
        'df_ratings': df_ratings_inter}
    
    save_data(int_dfs)
    
if __name__ == '__main__':
    main()