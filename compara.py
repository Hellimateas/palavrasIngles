def ler_palavras_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            # Remove quebras de linha e espaços extras
            palavras = {linha.strip() for linha in arquivo.readlines()}
        return palavras
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return set()

def salvar_palavras_arquivo(nome_arquivo, palavras):
    with open(nome_arquivo, "w") as arquivo:
        for palavra in sorted(palavras):
            arquivo.write(palavra + "\n")
    print(f"Palavras salvas em '{nome_arquivo}'.")

# Nomes dos arquivos de entrada e saída
arquivo_base = "base.txt"
arquivo_novo = "arquivo.txt"
arquivo_resultado = "resultado.txt"

# Ler palavras dos dois arquivos
palavras_base = ler_palavras_arquivo(arquivo_base)
palavras_novo = ler_palavras_arquivo(arquivo_novo)

# Encontrar palavras que estão no novo.txt mas não no base.txt
palavras_diferentes = palavras_novo - palavras_base

# Salvar as palavras diferentes no arquivo de resultado
salvar_palavras_arquivo(arquivo_resultado, palavras_diferentes)