from mlxtend.frequent_patterns import apriori, association_rules
from pandas import DataFrame


def mine_rules(basket, min_support=0.3, min_confidence=0.6, min_lift=1.5):
    frequent_itemsets = apriori(
        basket, min_support=min_support, use_colnames=True)
    rules = association_rules(
        frequent_itemsets, metric="confidence", min_threshold=min_confidence)

    rules = rules[rules['lift'] >= min_lift]

    rules_alzheimer = rules[rules['consequents'].astype(
        str).str.contains('Diagnosis=1')]
    rules_no_alzheimer = rules[rules['consequents'].astype(
        str).str.contains('Diagnosis=0')]

    rules_alzheimer = rules_alzheimer.sort_values(
        by='confidence', ascending=False)
    rules_no_alzheimer = rules_no_alzheimer.sort_values(
        by='confidence', ascending=False)

    return rules_alzheimer, rules_no_alzheimer


def format_rules_expression(rules):
    def clean_frozenset(frozenset_obj):
        items = sorted(list(frozenset_obj))
        clean_items = [item.split('_', 1)[-1] for item in items]
        return ', '.join(clean_items)

    rules = rules.copy()
    rules['antecedents'] = rules['antecedents'].apply(clean_frozenset)
    rules['consequents'] = rules['consequents'].apply(clean_frozenset)

    selected_cols = ['antecedents', 'consequents', 'antecedent support',
                     'consequent support', 'support', 'confidence', 'lift']
    return rules[selected_cols]


def remove_duplicate_rules(rules):
    seen = set()
    unique_rules = []

    for _, row in rules.iterrows():
        antecedent = frozenset(sorted(row['antecedents']))
        consequent = frozenset(sorted(row['consequents']))
        rule_key = (antecedent, consequent)

        if rule_key not in seen:
            seen.add(rule_key)
            unique_rules.append(row)

    return DataFrame(unique_rules)
