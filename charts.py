from pandas.errors import EmptyDataError
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os

plt.rcParams['figure.figsize'] = (8, 6)

continuous_vars = [
    'Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality',
    'SystolicBP', 'DiastolicBP', 'CholesterolTotal', 'CholesterolLDL',
    'CholesterolHDL', 'CholesterolTriglycerides', 'MMSE', 'FunctionalAssessment', 'ADL'
]

discrete_vars = [
    'Gender', 'Ethnicity', 'EducationLevel', 'Smoking', 'FamilyHistoryAlzheimers',
    'CardiovascularDisease', 'Diabetes', 'Depression', 'HeadInjury', 'Hypertension',
    'MemoryComplaints', 'BehavioralProblems', 'Confusion', 'Disorientation',
    'PersonalityChanges', 'DifficultyCompletingTasks', 'Forgetfulness', 'Diagnosis'
]


def create_pie_chart_variable_types(output_folder='output'):

    sizes = [len(continuous_vars), len(discrete_vars)]
    labels = ['Contínuas', 'Discretas']
    colors = ['#66b3ff', '#99ff99']
    explode = (0.05, 0.05)

    fig, ax = plt.subplots()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')

    ax.tick_params(bottom=False, left=False)

    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)

    wedges, texts, autotexts = ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops=dict(width=0.5),
        textprops=dict(color="black", fontsize=12)
    )

    ax.axis('equal')
    plt.title('Proporção de Variáveis Contínuas vs Discretas')

    os.makedirs(output_folder, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'quant_variaveis_dataset.png'))
    plt.close()


def create_bar_chart_rule_counts(output_folder='output', min_support=0.1, min_confidence=0.6):
    path_diag1 = os.path.join(
        output_folder, f'alzheimers_association_rules_Diagnosis_1_s-{min_support}_c-{min_confidence}.csv')
    path_diag0 = os.path.join(
        output_folder, f'alzheimers_association_rules_Diagnosis_0_s-{min_support}_c-{min_confidence}.csv')

    count_diag1 = 0
    count_diag0 = 0

    try:
        if os.path.exists(path_diag1):
            df_diag1 = pd.read_csv(path_diag1)
            count_diag1 = len(df_diag1)
    except EmptyDataError:
        count_diag1 = 0

    try:
        if os.path.exists(path_diag0):
            df_diag0 = pd.read_csv(path_diag0)
            count_diag0 = len(df_diag0)
    except EmptyDataError:
        count_diag0 = 0

    counts = {}
    if count_diag1 > 0 or count_diag1 == 0:
        counts['Com Alzheimer'] = count_diag1
    if count_diag0 > 0 or count_diag0 == 0:
        counts['Sem Alzheimer'] = count_diag0
    if count_diag1 + count_diag0 > 0 or count_diag1 + count_diag0 == 0:
        counts['Totalidade'] = count_diag1 + count_diag0

    if not counts:
        return

    bar_colors = ['#FF6961', '#77DD77', '#779ECB'][:len(counts)]
    bar_width = 0.25

    fig, ax = plt.subplots()
    bars = ax.bar(counts.keys(), counts.values(),
                  color=bar_colors, width=bar_width, edgecolor='none')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')

    ax.tick_params(bottom=False, left=False)

    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)

    max_count = max(counts.values())
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim(0, max_count * 1.2)

    plt.title(
        f'Quantidade de Regras Mineradas\n(Suporte ≥ {min_support}, Confiança ≥ {min_confidence})', fontsize=14)
    plt.ylabel('Nº de Regras', fontsize=12)
    plt.xlabel('Tipo de Diagnóstico', fontsize=12)

    for i, v in enumerate(counts.values()):
        ax.text(i, v + (max_count * 0.02), str(v),
                ha='center', va='bottom', fontsize=10)

    plt.tight_layout()

    os.makedirs(output_folder, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(
        output_folder, f'contagem_regras_s-{min_support}_c-{min_confidence}.png'), dpi=300)
    plt.close()
