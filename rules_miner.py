from mining_tools import mine_rules, format_rules_expression, remove_duplicate_rules


def generate_and_format_rules_expression(basket, min_support, min_confidence):
    rules_alzheimer, rules_no_alzheimer = mine_rules(
        basket, min_support, min_confidence)

    rules_alzheimer = format_rules_expression(rules_alzheimer)
    rules_alzheimer = remove_duplicate_rules(rules_alzheimer)

    rules_no_alzheimer = format_rules_expression(rules_no_alzheimer)
    rules_no_alzheimer = remove_duplicate_rules(rules_no_alzheimer)

    return rules_alzheimer, rules_no_alzheimer


def save_rules(rules_alzheimer, rules_no_alzheimer, output_path_1, output_path_0):
    rules_alzheimer.to_csv(output_path_1, index=False)
    rules_no_alzheimer.to_csv(output_path_0, index=False)
