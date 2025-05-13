
import pandas as pd
from preprocessing import discretize, encode_features
from mining import mine_rules

def main():
    df = pd.read_csv('alzheimers_disease_data.csv')
    print(f'df_bruto:\n ${df.head(10)}')
    df = discretize(df)
    print(f'df_discretizado:\n ${df.head(10)}')
    df_encoded = encode_features(df)
    print(f'df_transacional:\n ${df_encoded.head(10)}')
    basket = pd.get_dummies(df_encoded)
    
    rules_alzheimer, rules_no_alzheimer = mine_rules(basket, 0.2, 0.6)
    
    rules_alzheimer.to_csv('alzheimers_association_rules_Diagnosis_1.csv', index=False)
    rules_no_alzheimer.to_csv('alzheimers_association_rules_Diagnosis_0.csv', index=False)
    
    print("=== Regras para Diagnosis = 1 (Alzheimer) ===")
    print(rules_alzheimer[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(15))
    
    print("\n=== Regras para Diagnosis = 0 (Sem Alzheimer) ===")
    print(rules_no_alzheimer[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(15))

if __name__ == "__main__":
    main()
