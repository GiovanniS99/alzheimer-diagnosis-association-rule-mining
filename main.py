from data_pipeline import load_and_prepare_data
from rules_miner import generate_and_format_rules_expression, save_rules
from reporting import print_rules_summary
from charts import create_pie_chart_variable_types, create_bar_chart_rule_counts


def main():

    # Definindo os parâmetros de suporte e confiança
    # list_of_args = [[0.65, 0.7], [0.5, 0.7], [
    #     0.55, 0.7], [0.55, 0.65], [0.6, 0.7]]

    list_of_args = [[0.12, 0.6], [0.12, 0.5]]
    
    for min_support, min_confidence in list_of_args:

        print(
            f" ======== Mineração com suporte = {min_support} e confiança = {min_confidence} ========\n")

        # Pré-processando os dados, transformando em um DataFrame e depois em um DataFrame binário transacional
        basket = load_and_prepare_data(
            'data/alzheimers_disease_data.csv')

        # Gerando as regras de associação a partir do DataFrame transacional e aplicando os filtros de suporte e confiança
        rules_alzheimer, rules_no_alzheimer = generate_and_format_rules_expression(
            basket,
            min_support,
            min_confidence
        )

        # Salvando as regras de associação em arquivos CSV
        save_rules(
            rules_alzheimer,
            rules_no_alzheimer,
            f'output/alzheimers_association_rules_Diagnosis_1_s-{min_support}_c-{min_confidence}.csv',
            f'output/alzheimers_association_rules_Diagnosis_0_s-{min_support}_c-{min_confidence}.csv'
        )

        # Imprimindo um resumo das regras de associação no terminal de execução
        print_rules_summary(rules_alzheimer, rules_no_alzheimer, n=15)

        # Gerando gráficos de barras com a quantidade de regras de associação mineradas
        create_bar_chart_rule_counts(
            min_support=min_support, min_confidence=min_confidence)

    # Gerando gráfico de pizza com a proporção de variáveis discretas e contínuas
    create_pie_chart_variable_types()


if __name__ == "__main__":
    main()
