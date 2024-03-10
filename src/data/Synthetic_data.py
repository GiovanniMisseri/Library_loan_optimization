import pandas as pd
import numpy as np
from src.features.build_features import (create_libraries,
                                         create_users,
                                         create_books,
                                         save_data)

def create_data(num_libraries, num_users, num_books, to_save=False):
    libraries = create_libraries(num_libraries)
    users = create_users(num_users, num_libraries)
    books = create_books(num_books, num_libraries)

    # Save
    if to_save:
        save_data(libraries, 'libraries')
        save_data(users, 'users')
        save_data(books, 'books')

    return libraries, users, books

libraries, users, books = create_data(10,100,15)






