# Função para ler palavras de um arquivo
def ler_palavras_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return {linha.strip() for linha in arquivo.readlines()}
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return set()

# Função para salvar palavras em um arquivo
def salvar_palavras_arquivo(nome_arquivo, palavras):
    with open(nome_arquivo, "w") as arquivo:
        for palavra in sorted(palavras):  # Ordena as palavras antes de salvar
            arquivo.write(palavra + "\n")
    print(f"Palavras salvas em '{nome_arquivo}'.")

# Nomes dos arquivos de entrada e saída
arquivo_1 = "base.txt"
arquivo_2 = "resultado.txt"
arquivo_resultado = "base.txt"

# Ler palavras de ambos os arquivos
palavras_arquivo1 = ler_palavras_arquivo(arquivo_1)
palavras_arquivo2 = ler_palavras_arquivo(arquivo_2)

# Combinar os dois conjuntos de palavras (eliminando duplicatas)
palavras_combinadas = palavras_arquivo1 | palavras_arquivo2  # União dos conjuntos

# Salvar as palavras combinadas no arquivo de resultado
salvar_palavras_arquivo(arquivo_resultado, palavras_combinadas)
