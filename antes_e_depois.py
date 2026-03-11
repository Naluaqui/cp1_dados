import pandas as pd
import matplotlib.pyplot as plt
from limpeza_de_dados import preparar_e_verificar_dados  

df = preparar_e_verificar_dados("Titanic-Dataset.csv")  

coluna = "Fare"  

df_iqr = df[[coluna]].dropna().copy()  

q1 = df_iqr[coluna].quantile(0.25)  
q3 = df_iqr[coluna].quantile(0.75)  
iqr = q3 - q1  

limite_inferior = q1 - 1.5 * iqr  
limite_superior = q3 + 1.5 * iqr  

df_sem_outliers = df_iqr[  
    (df_iqr[coluna] >= limite_inferior) & (df_iqr[coluna] <= limite_superior)  
]  

print(f"Q1: {q1:.3f}")  
print(f"Q3: {q3:.3f}")  
print(f"IQR: {iqr:.3f}")  
print(f"Limite inferior: {limite_inferior:.3f}")  
print(f"Limite superior: {limite_superior:.3f}")  
print(f"Quantidade antes: {len(df_iqr)}")  
print(f"Quantidade depois: {len(df_sem_outliers)}")  
print(f"Outliers removidos: {len(df_iqr) - len(df_sem_outliers)}")  

plt.figure(figsize=(8, 5))  
plt.boxplot(df_iqr[coluna], vert=True)  
plt.title(f"Boxplot antes da remoção de outliers - {coluna}")  
plt.ylabel(coluna)  
plt.grid(True, linestyle="--", alpha=0.7)  
plt.show()  

plt.figure(figsize=(8, 5))  
plt.boxplot(df_sem_outliers[coluna], vert=True)  
plt.title(f"Boxplot depois da remoção de outliers - {coluna}")  
plt.ylabel(coluna)  
plt.grid(True, linestyle="--", alpha=0.7)  
plt.show()  