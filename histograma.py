import pandas as pd
import matplotlib.pyplot as plt
from limpeza_de_dados import preparar_e_verificar_dados

df = preparar_e_verificar_dados("Titanic-Dataset.csv")

variaveis = ["Age", "Fare"]

df = df.dropna(subset=variaveis)

for coluna in variaveis:
    plt.figure(figsize=(8, 5))
    plt.hist(df[coluna], bins="auto", edgecolor="black")
    plt.title(f"Histograma de {coluna}")
    plt.xlabel(coluna)
    plt.ylabel("Frequência")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()