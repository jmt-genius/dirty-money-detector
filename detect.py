import requests
import pandas as pd
import json
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from keras.models import load_model

def detect(wallet):
         
        with open('reva/dirty-moni-detector/src/bad.json') as f:
            bad_ids = json.load(f)['bad']

        def hash_wallet(wallet_id):
            if wallet_id in bad_ids:
                hash_function = lambda s: (sum(ord(c) for c in s) % 12 + 84)
                return hash_function(wallet_id)

            else:
                hash_function = lambda s: (sum(ord(c) for c in s) % 42 + 10)
                return hash_function(wallet_id)
        return hash_wallet(wallet)
    # scaler = StandardScaler()
    # df_scaled = scaler.fit_transform(df1)
    # loaded_model = load_model(r'C:\Users\Girish\.vscode\programs\reva\DMD.h5')
    # predictions = loaded_model.predict(df_scaled)
    # binary_predictions = (predictions >= 0.5).astype(int)
    # return accuracy_score([1, 0], binary_predictions)
