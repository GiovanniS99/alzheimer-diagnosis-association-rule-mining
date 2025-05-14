import matplotlib.pyplot as plt
import squarify
import os

variables_dict = {
    'Age': 'c',
    'BMI': 'c',
    'AlcoholConsumption': 'c',
    'PhysicalActivity': 'c',
    'DietQuality': 'c',
    'SleepQuality': 'c',
    'SystolicBP': 'c',
    'DiastolicBP': 'c',
    'CholesterolTotal': 'c',
    'CholesterolLDL': 'c',
    'CholesterolHDL': 'c',
    'CholesterolTriglycerides': 'c',
    'MMSE': 'c',
    'FunctionalAssessment': 'c',
    'ADL': 'c',
    'Gender': 'd',
    'Ethnicity': 'd',
    'EducationLevel': 'd',
    'Smoking': 'd',
    'FamilyHistoryAlzheimers': 'd',
    'CardiovascularDisease': 'd',
    'Diabetes': 'd',
    'Depression': 'd',
    'HeadInjury': 'd',
    'Hypertension': 'd',
    'MemoryComplaints': 'd',
    'BehavioralProblems': 'd',
    'Confusion': 'd',
    'Disorientation': 'd',
    'PersonalityChanges': 'd',
    'DifficultyCompletingTasks': 'd',
    'Forgetfulness': 'd',
    'Diagnosis': 'd'
}

def plot_variables_treemap(variables_dict, output_folder='output'):
    labels = [f"{var}\n({typ})" for var, typ in variables_dict.items()]
    sizes = [1] * len(variables_dict)  # Cada variável terá peso igual

    color_map = {
        'c': '#66b3ff',  # Azul para Contínuas
        'd': '#99ff99'   # Verde para Discretas
    }
    colors = [color_map[typ] for typ in variables_dict.values()]

    fig, ax = plt.subplots(figsize=(14, 8))
    squarify.plot(
        sizes=sizes,
        label=labels,
        color=colors,
        alpha=0.8,
        text_kwargs={'fontsize': 10},
        ax=ax,               # 🔥 garantir plot correto dentro do 'ax'
        pad=True              # 🔥 espaçamento melhor
    )

    plt.title('Distribuição de Variáveis: Contínuas vs Discretas', fontsize=16)
    plt.axis('off')

    os.makedirs(output_folder, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'treemap_variaveis.png'), dpi=300)
    plt.close()

plot_variables_treemap(variables_dict)