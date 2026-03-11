import pandas as pd
import matplotlib.pyplot as plt
from limpeza_de_dados import preparar_e_verificar_dados  

df = preparar_e_verificar_dados("Titanic-Dataset.csv")  

pares = [("SibSp", "Parch"), ("Pclass", "Survived")]  

for x, y in pares:  
    df_par = df[[x, y]].dropna().copy()  

    correlacao = df_par[x].corr(df_par[y], method="pearson")  

    frequencia = (  
        df_par.groupby([x, y])  
        .size()  
        .reset_index(name="frequencia")  
    )  

    print("\n" + "=" * 50)  
    print(f"PAR: {x} x {y}")  
    print("=" * 50)  
    print(f"Correlação de Pearson: {correlacao:.3f}")  
    print(frequencia)  

    plt.figure(figsize=(9, 6))  
    plt.scatter(  
        frequencia[x],  
        frequencia[y],  
        s=frequencia["frequencia"] * 8,  
        alpha=0.6,  
        edgecolors="black"  
    )  

    for _, row in frequencia.iterrows():  
        plt.text(  
            row[x],  
            row[y],  
            str(int(row["frequencia"])),  
            fontsize=8,  
            ha="center",  
            va="center"  
        )  

    plt.title(f"Scatterplot com Frequência: {x} x {y}")  
    plt.xlabel(x)  
    plt.ylabel(y)  
    plt.grid(True, linestyle="--", alpha=0.7)  
    plt.show()  