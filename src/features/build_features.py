import pandas as pd
import numpy as np


### DATA FEATURES ###
def add_syn_latlon(df):
    # Latitude and longitude
    dimension=df.shape[0]
    lat = np.random.uniform(45.40, 45.52, dimension)
    lon = np.random.uniform(9.06, 9.3, dimension)
    df['lat'] = lat
    df['lon'] = lon
    return df

def add_library(df, num_libraries, col_name):
    # Favourite library
    dimension=df.shape[0]
    fav_library = np.random.random_integers(0, num_libraries-1, dimension).astype(str)
    df[col_name] = fav_library
    return df

def add_curr_loans(df):
    # Current loans
    df['num_curr_loans']=0
    return df

def add_number_copies(df, num_libraries):
    dimension = df.shape[0]
    num_copies_per_book = np.random.random_integers(1, 30, dimension)
    expanded_df = df.loc[df.index.repeat(num_copies_per_book)]
    expanded_df = add_library(expanded_df, num_libraries, 'owner_library')
    return expanded_df


def create_libraries(num_libraries):
    libraries = pd.DataFrame(np.arange(num_libraries).astype(str), columns=['lib_id'])

    # Latitude and longitude
    libraries = add_syn_latlon(libraries)

    return libraries

def create_users(num_users, num_libraries):
    users = pd.DataFrame(np.arange(num_users).astype(str), columns=['user_id'])

    # Favourite library
    users = add_library(users, num_libraries, 'fav_library')
    # Current loans
    users = add_curr_loans(users)

    return users

def create_books(num_books, num_libraries):
    books = pd.DataFrame(np.arange(num_books).astype(str), columns=['book_id'])

    # Expand by number of copies
    books = add_number_copies(books, num_libraries)
    # Serial id
    books['serial_id']=books['book_id']+'_'+books['owner_library']+'_'+np.arange(books.shape[0]).astype(str)
    # Borrower
    books['borrower']=''
    return books

def save_data(df, name_df, folder='synthetic'):
    df.to_csv('./data/{}/{}.csv'.format([folder, name_df]), index=False)






