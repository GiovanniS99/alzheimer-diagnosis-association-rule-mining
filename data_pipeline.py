import pandas as pd
from preprocessing import discretize, encode_features


def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)
    df = discretize(df)

    print(f"[INFO] Quantidade de registros da base de dados: {len(df)}")

    df_encoded = encode_features(df)
    basket = pd.get_dummies(df_encoded)
    basket = basket.astype(bool)
    return basket
