
import pandas as pd


def discretize(df):
    df['Age'] = pd.cut(df['Age'], bins=[59, 70, 80, 90],
                       labels=['60-70', '71-80', '81-90'])
    df['BMI'] = pd.cut(df['BMI'], bins=[14, 18.5, 25, 30, 40], labels=[
                       'Underweight', 'Normal', 'Overweight', 'Obese'])
    df['AlcoholConsumption'] = pd.cut(
        df['AlcoholConsumption'], bins=[-1, 5, 10, 20], labels=['Low', 'Moderate', 'High'])
    df['PhysicalActivity'] = pd.cut(
        df['PhysicalActivity'], bins=[-1, 4, 7, 10], labels=['Low', 'Moderate', 'High'])
    df['DietQuality'] = pd.cut(
        df['DietQuality'], bins=[-1, 4, 7, 10], labels=['Poor', 'Average', 'Good'])
    df['SleepQuality'] = pd.cut(df['SleepQuality'], bins=[3, 6, 8, 10], labels=[
                                'Poor', 'Average', 'Good'])
    df['SystolicBP'] = pd.cut(df['SystolicBP'], bins=[89, 120, 130, 140, 180], labels=[
                              'Normal', 'Elevated', 'Hypertension 1', 'HyperTension 2'])
    df['DiastolicBP'] = pd.cut(df['DiastolicBP'], bins=[59, 80, 90, 120], labels=[
                               'Normal', 'Hypertension 1', 'Hypertension 2'])
    df['CholesterolTotal'] = pd.cut(df['CholesterolTotal'], bins=[
                                    149, 200, 240, 300], labels=['Desirable', 'Borderline', 'High'])
    df['CholesterolLDL'] = pd.cut(df['CholesterolLDL'], bins=[
                                  49, 100, 160, 200], labels=['Desirable', 'Borderline', 'High'])
    df['CholesterolHDL'] = pd.cut(df['CholesterolHDL'], bins=[
                                  19, 40, 60, 100], labels=['Low', 'Borderline', 'Normal'])
    df['CholesterolTriglycerides'] = pd.cut(df['CholesterolTriglycerides'], bins=[
                                            49, 150, 200, 400], labels=['Normal', 'Borderline', 'High'])
    df['MMSE'] = pd.cut(df['MMSE'], bins=[-1, 18, 24, 30],
                        labels=['Severe', 'Mild', 'Normal'])
    df['FunctionalAssessment'] = pd.cut(
        df['FunctionalAssessment'], bins=[-1, 3, 7, 10], labels=['Severe', 'Moderate', 'Normal'])
    df['ADL'] = pd.cut(df['ADL'], bins=[-1, 3, 7, 10],
                       labels=['Severe', 'Moderate', 'Normal'])
    return df


def encode_features(df):
    df_encoded = pd.DataFrame()
    for col in df.columns:
        if col not in ['PatientID', 'DoctorInCharge']:
            df_encoded[col] = df[col].astype(str)
            df_encoded[col] = col + "=" + df_encoded[col]
    return df_encoded
