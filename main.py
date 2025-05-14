from data_pipeline import load_and_prepare_data
from rules_miner import generate_and_format_rules_expression, save_rules
from reporting import print_rules_summary


def main():
    basket = load_and_prepare_data('data/alzheimers_disease_data.csv')

    rules_alzheimer, rules_no_alzheimer = generate_and_format_rules_expression(
        basket,
        min_support=0.11,
        min_confidence=0.5
    )

    save_rules(
        rules_alzheimer,
        rules_no_alzheimer,
        'output/alzheimers_association_rules_Diagnosis_1.csv',
        'output/alzheimers_association_rules_Diagnosis_0.csv'
    )

    print_rules_summary(rules_alzheimer, rules_no_alzheimer, n=15)


if __name__ == "__main__":
    main()
