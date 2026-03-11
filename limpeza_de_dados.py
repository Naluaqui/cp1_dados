import pandas as pd


def preparar_e_verificar_dados(caminho_csv):  
    df = pd.read_csv(caminho_csv)  

    #print("=== HEAD() ===")  
    #print(df.head())  

    #print("\n=== INFO() ===")  
    df.info()  

    #print("\n=== % DE NULOS POR COLUNA ===")  
    percentual_nulos = df.isnull().mean() * 100  
    #print(percentual_nulos.sort_values(ascending=False))  

    df = df.drop_duplicates()  
    df = df.drop(columns=["Cabin"], errors="ignore")  
    df = df.dropna(subset=["Age", "Embarked"])  

    #print("\n=== SHAPE APÓS LIMPEZA ===")  
    #print(df.shape)  

    #print("\n=== % DE NULOS APÓS LIMPEZA ===")  
    percentual_nulos_pos = df.isnull().mean() * 100  
    #print(percentual_nulos_pos.sort_values(ascending=False))  

    #print("\n=== HEAD() APÓS LIMPEZA ===")  
    #print(df.head())  

    return df  


if __name__ == "__main__":  
    df_limpo = preparar_e_verificar_dados("Titanic-Dataset.csv")  