# 🧠 Alzheimer Diagnosis Association Rule Mining

Este projeto aplica técnicas de **mineração de regras de associação** para identificar padrões relevantes em dados clínicos associados ao diagnóstico da Doença de Alzheimer. Utiliza-se o algoritmo **Apriori**, com discretização de variáveis contínuas, codificação transacional e geração de regras com foco na variável de diagnóstico (`Diagnosis`).

---

## 📁 Base de dados

Os dados utilizados encontram-se na pasta [`/data`](./data) e são provenientes da seguinte base pública:

🔗 [Alzheimer's Disease Dataset – Kaggle](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset)

A base de dados contém informações clínicas, demográficas e cognitivas de pacientes, incluindo avaliações como MMSE, ADL, e histórico médico.

---

## 🎯 Objetivo

Identificar **regras frequentes** e **correlações relevantes** entre variáveis clínicas que estejam associadas ao diagnóstico positivo de Alzheimer, auxiliando no:

- Apoio à decisão clínica
- Detecção precoce de fatores de risco
- Apoio a campanhas educativas a familiares que detectarem indicadores ruins de maneira empírica

---

## ⚙️ Funcionamento do projeto

1. **Pré-processamento**
   - Discretização de variáveis contínuas
   - Codificação em dados transacionais
   - Binarização dos dados transacionais

2. **Mineração**
   - Algoritmo **Apriori** (`mlxtend`)
   - Regras separadas por consequente `Diagnosis=1` e `Diagnosis=0`

3. **Pós-processamento**
   - Filtragem por suporte, confiança e lift
   - Limpeza de regras redundantes
   - Visualização de métricas

---

## 📊 Parâmetros utilizados

- **Suporte mínimo:** configurável (ex.: `0.11`)
- **Confiança mínima:** configurável (ex.: `0.6`)
- **Lift mínimo:** opcional (recomendado `> 1.2`)
- **Filtro inteligente:** se o suporte for menor que `0.35`, as regras com `Diagnosis=0` são ignoradas na construção dos gráficos.

---

## 📂 Estrutura do projeto

📁 data/ # Dados originais (.csv) e glossário (.txt)
📁 output/ # Regras mineradas e gráficos gerados
📁 charts.py # Geração dos gráficos (barras, pizza)
📁 preprocessing.py # Discretização e codificação dos dados
📁 mining_tools.py # Mineração, limpeza e filtragem de regras
📁 rules_miner.py # Função central para gerar regras filtradas
📁 main.py # Execução principal do pipeline


---

## 📈 Exemplos de gráficos gerados

- Distribuição de variáveis contínuas vs discretas (pizza)
- Contagem de regras geradas por tipo de diagnóstico
- Visualização das variáveis por categoria clínica

Os gráficos são salvos automaticamente na pasta `/output`.

---

## 📌 Requisitos

- Python 3.8+
- pandas, matplotlib, mlxtend, squarify

```bash
pip install -r requirements.txt

