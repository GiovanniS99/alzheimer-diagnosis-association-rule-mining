import matplotlib.pyplot as plt
import os

# Variáveis e tipos
variables_dict = {
    'Age': 'c', 'BMI': 'c', 'AlcoholConsumption': 'c', 'PhysicalActivity': 'c', 'DietQuality': 'c',
    'SleepQuality': 'c', 'SystolicBP': 'c', 'DiastolicBP': 'c', 'CholesterolTotal': 'c', 'CholesterolLDL': 'c',
    'CholesterolHDL': 'c', 'CholesterolTriglycerides': 'c', 'MMSE': 'c', 'FunctionalAssessment': 'c', 'ADL': 'c',
    'Gender': 'd', 'Ethnicity': 'd', 'EducationLevel': 'd', 'Smoking': 'd', 'FamilyHistoryAlzheimers': 'd',
    'CardiovascularDisease': 'd', 'Diabetes': 'd', 'Depression': 'd', 'HeadInjury': 'd', 'Hypertension': 'd',
    'MemoryComplaints': 'd', 'BehavioralProblems': 'd', 'Confusion': 'd', 'Disorientation': 'd',
    'PersonalityChanges': 'd', 'DifficultyCompletingTasks': 'd', 'Forgetfulness': 'd', 'Diagnosis': 'd'
}

# Variáveis organizadas por categoria
categories = {
    'Demographic Details': ['Gender', 'Ethnicity', 'EducationLevel'],
    'Lifestyle Factors': ['Smoking', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality'],
    'Medical History': ['FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes', 'Depression', 'HeadInjury', 'Hypertension'],
    'Clinical Measurements': ['BMI', 'SystolicBP', 'DiastolicBP', 'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides'],
    'Cognitive and Functional Assessments': ['MMSE', 'FunctionalAssessment', 'ADL'],
    'Symptoms': ['MemoryComplaints', 'BehavioralProblems', 'Confusion', 'Disorientation', 'PersonalityChanges', 'DifficultyCompletingTasks', 'Forgetfulness'],
    'Diagnosis Information': ['Diagnosis']
}

def plot_variables_pyramid(variables_dict, categories, output_folder='output'):
    n_categories = len(categories)
    n_cols = 2
    n_rows = (n_categories + 1) // n_cols

    fig, axs = plt.subplots(n_rows, n_cols, figsize=(18, 22))
    axs = axs.flatten()

    color_map = {'c': '#66b3ff', 'd': '#99ff99'}

    for idx, (cat, vars_in_cat) in enumerate(categories.items()):
        ax = axs[idx]

        # Só pegar variáveis que existem
        vars_available = [var for var in vars_in_cat if var in variables_dict]
        types = [variables_dict[var] for var in vars_available]
        colors = [color_map[typ] for typ in types]

        # Criar valores decrescentes para formar pirâmide
        values = list(range(len(vars_available), 0, -1))

        # Plotar barras
        ax.barh(vars_available, values, color=colors, height=0.4, edgecolor='none')

        ax.set_title(cat, fontsize=14, weight='bold')
        ax.invert_yaxis()  # Primeiro em cima
        ax.set_xlim(0, max(values) + 1)  # Espaço extra
        ax.xaxis.grid(True, linestyle='--', color='lightgrey')
        ax.set_axisbelow(True)
        ax.set_yticklabels(vars_available, fontsize=10)
        ax.set_xticks([])  # Tirar número do eixo X para não poluir

    # Remover subplots vazios
    for j in range(idx + 1, len(axs)):
        fig.delaxes(axs[j])

    plt.tight_layout()
    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(os.path.join(output_folder, 'barras_variaveis_piramide.png'), dpi=300)
    plt.close()

# Chamar função
plot_variables_pyramid(variables_dict, categories)
