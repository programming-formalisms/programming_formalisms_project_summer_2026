import os
import pandas as pd

def load_data(file_path):

    """
    Read the data into a dataframe
    """
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"error")

    column_names = [
        'year', 'month', 'day', 
        'avg_temp', 'corrected_temp', 'location_id'
    ]


    df = pd.read_csv(file_path, sep=r'\s+', names=column_names)
    
    assert not df.empty, "error"
    assert len(df.columns) == 6, f"error"

    return df


path = r"data\uppsala_tm_1722-2022.dat"  
data = load_data(path)



print(data.head())
