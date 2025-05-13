import pandas as pd
from preprocessing import discretize, encode_features
from mining import mine_rules, clean_rules


def main():
    df = pd.read_csv('alzheimers_disease_data.csv')
    df = discretize(df)
    df_encoded = encode_features(df)
    basket = pd.get_dummies(df_encoded)

    rules_alzheimer, rules_no_alzheimer = mine_rules(basket, 0.5, 0.7)
    rules_alzheimer = clean_rules(rules_alzheimer)
    rules_no_alzheimer = clean_rules(rules_no_alzheimer)

    rules_alzheimer.to_csv(
        'alzheimers_association_rules_Diagnosis_1.csv', index=False)
    rules_no_alzheimer.to_csv(
        'alzheimers_association_rules_Diagnosis_0.csv', index=False)

    print("=== Regras para Diagnosis = 1 (Alzheimer) ===")
    print(rules_alzheimer[['antecedents', 'consequents',
          'support', 'confidence', 'lift']].head(15))

    print("\n=== Regras para Diagnosis = 0 (Sem Alzheimer) ===")
    print(rules_no_alzheimer[['antecedents', 'consequents',
          'support', 'confidence', 'lift']].head(15))


if __name__ == "__main__":
    main()
