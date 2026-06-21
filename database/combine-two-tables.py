import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    p1 = pd.merge(person, address, on = 'personId', how = 'left')
    p1 = p1[['firstName', 'lastName', 'city', 'state']] 
    return p1