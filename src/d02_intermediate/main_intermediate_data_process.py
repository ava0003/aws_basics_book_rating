from src.d01_data.load_data import load_data
from d02_intermediate.transform_data import *
from d02_intermediate.save_int_data import save_int_data


def main():
    
    # Load data from raw files
    [df_books, df_users, df_ratings] = load_data()

    
    # Transform datasets 
    df_books_inter = books_data_treatment(df_books)
    df_users_inter = users_data_treatment(df_users)
    df_ratings_inter = ratings_data_treatment(df_ratings)
    
    # Save new datasets into intermediate data 
    
    int_dfs = [df_books_inter, df_users_inter, df_ratings_inter]
    
    save_int_data(int_dfs)
    
if __name__ == '__main__':
    main()