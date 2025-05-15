import pandas as pd
from preprocessing import discretize, encode_features

def load_and_prepare_data(file_path, filter_diagnosis_1=False):
    df = pd.read_csv(file_path)
    df = discretize(df)
    
    if filter_diagnosis_1:
        df = df[df['Diagnosis'] == 1].reset_index(drop=True)
        print(f"[INFO] Dados filtrados: {len(df)} registros com Diagnosis = 1.")
    else:
        print(f"[INFO] Dados completos: {len(df)} registros no total.")
    
    df_encoded = encode_features(df)
    basket = pd.get_dummies(df_encoded)
    basket = basket.astype(bool)
    return basket
