
from mlxtend.frequent_patterns import apriori, association_rules

def mine_rules(basket, min_support=0.3, min_confidence=0.6):
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    
    rules_alzheimer = rules[rules['consequents'].astype(str).str.contains('Diagnosis=1')]
    rules_no_alzheimer = rules[rules['consequents'].astype(str).str.contains('Diagnosis=0')]
    
    rules_alzheimer = rules_alzheimer.sort_values(by='confidence', ascending=False)
    rules_no_alzheimer = rules_no_alzheimer.sort_values(by='confidence', ascending=False)
    
    return rules_alzheimer, rules_no_alzheimer
