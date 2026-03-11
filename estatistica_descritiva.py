import pandas as pd
from limpeza_de_dados import preparar_e_verificar_dados  

df = preparar_e_verificar_dados("Titanic-Dataset.csv")  

variaveis = ["Age", "Fare"]

df = df.dropna(subset=variaveis)

for coluna in variaveis:
    serie = df[coluna]

    media = serie.mean()
    mediana = serie.median()
    moda = serie.mode()
    variancia_amostral = serie.var(ddof=1)
    desvio_padrao_amostral = serie.std(ddof=1)

    print("\n" + "=" * 50)
    print(f"VARIÁVEL: {coluna}")
    print("=" * 50)
    print(f"Média: {media:.3f}")
    print(f"Mediana: {mediana:.3f}")

    if len(moda) == 1:
        print(f"Moda: {moda.iloc[0]:.3f}")
    else:
        print(f"Moda(s): {[round(x, 3) for x in moda.tolist()]}")

    print(f"Variância amostral: {variancia_amostral:.3f}")
    print(f"Desvio-padrão amostral: {desvio_padrao_amostral:.3f}")