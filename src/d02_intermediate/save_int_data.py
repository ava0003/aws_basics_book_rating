import argparse
import configparser


def save_csv(df, path):
    breakpoint()
    df.to_csv(path, index = False)

def save_data(int_dfs):

    # Get data from .csv files

    config = configparser.ConfigParser()
    config.read('config.ini')

    books_csv_url = config['URLIntermediate']['books']
    users_csv_url = config['URLIntermediate']['users']
    ratings_csv_url = config['URLIntermediate']['ratings']
    breakpoint()
    save_csv(int_dfs['df_books'], books_csv_url)
    save_csv(int_dfs['df_users'], users_csv_url)
    save_csv(int_dfs['df_ratings'], ratings_csv_url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('int_dfs', type=object)

    args = parser.parse_args()
    int_dfs = args.int_dfs
    result = save_csv(int_dfs) 