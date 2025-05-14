def print_rules_summary(rules_alzheimer, rules_no_alzheimer, n=15):
    print("=== Regras para Diagnosis = 1 (Alzheimer) ===")
    print(rules_alzheimer.head(n))
    
    print("\n=== Regras para Diagnosis = 0 (Sem Alzheimer) ===")
    print(rules_no_alzheimer.head(n))
