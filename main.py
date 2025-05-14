from data_pipeline import load_and_prepare_data
from rules_miner import generate_and_format_rules_expression, save_rules
from reporting import print_rules_summary
from charts import create_pie_chart_variable_types, create_bar_chart_rule_counts


def main():

    list_of_args = [[0.5, 0.7], [0.55, 0.7], [
        0.55, 0.65], [0.5, 0.65], [0.11, 0.5], [0.11, 0.6], [0.12, 0.5]]

    for min_support, min_confidence in list_of_args:

        print(
            f" ======== Mineração com suporte = {min_support} e confiança = {min_confidence} ========\n")

        basket = load_and_prepare_data('data/alzheimers_disease_data.csv')

        rules_alzheimer, rules_no_alzheimer = generate_and_format_rules_expression(
            basket,
            min_support,
            min_confidence
        )

        save_rules(
            rules_alzheimer,
            rules_no_alzheimer,
            'output/alzheimers_association_rules_Diagnosis_1.csv',
            'output/alzheimers_association_rules_Diagnosis_0.csv'
        )

        print_rules_summary(rules_alzheimer, rules_no_alzheimer, n=15)

        create_bar_chart_rule_counts(
            min_support=min_support, min_confidence=min_confidence)

    create_pie_chart_variable_types()


if __name__ == "__main__":
    main()
