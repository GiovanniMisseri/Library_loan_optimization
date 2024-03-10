import pandas as pd

from src.data.Synthetic_data import create_data

simulate_synth_data = True
use_synth_data = True

if simulate_synth_data:
    create_data(10, 1000, 150, to_save=True)

if use_synth_data:
    libraries = pd.read_csv('../data/synthetic/libraries.csv')
    users = pd.read_csv('../data/synthetic/users.csv')
    books = pd.read_csv('../data/synthetic/books.csv')

