import pandas as pd
import numpy as np
from datetime import datetime
import warnings

warnings.filterwarnings('ignore', category=FutureWarning)
pd.set_option('future.no_silent_downcasting', True)

def transform_data(data_produk):
    data = pd.DataFrame(data_produk)

    data = data[data['title'].str.lower() != 'unknown product']

    data['price'] = data['price'].replace(r'[^\d.]', '', regex=True).replace('', np.nan)
    data.dropna(subset=['price'], inplace=True)
    data['price'] = data['price'].astype(float) * 16000

    data['rating'] = data['rating'].replace(r'[^0-9.]', '', regex=True).replace('', np.nan)
    data.dropna(subset=['rating'], inplace=True)
    data['rating'] = data['rating'].astype(float)

    data['colors'] = data['colors'].replace(r'\D', '', regex=True).replace('', np.nan)
    data.dropna(subset=['colors'], inplace=True)
    data['colors'] = data['colors'].astype(int)

    data['size'] = data['size'].str.replace(r'Size:\s*', '', regex=True)
    data['gender'] = data['gender'].str.replace(r'Gender:\s*', '', regex=True)

    data.drop_duplicates(inplace=True)
    data.dropna(inplace=True)

    data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return data