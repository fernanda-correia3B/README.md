def analisar_texto(texto):
    """
    Função que conta caracteres, palavras e inverte o texto.
    """
    # Remove espaços extras nas pontas e conta caracteres totais
    total_caracteres = len(texto)
    
    # Divide o texto por espaços para contar as palavras
    palavras = texto.split()
    total_palavras = len(palavras)
    
    # Inverte a string
    texto_invertido = texto[::-1]
    
    return total_caracteres, total_palavras, texto_invertido

def executar_programa():
    print("--- BEM-VINDO AO ANALISADOR DE TEXTO ---")
    entrada = input("Digite uma frase ou texto para analisar: ")
    
    # Validação simples para garantir que o usuário digitou algo
    if not entrada.strip():
        print("Erro: Você não digitou nenhum texto válido.")
        return

    # Executa a lógica
    caracteres, palavras, invertido = analisar_texto(entrada)
    
    # Exibe os resultados de forma limpa
    print("\n=== RESULTADOS DA ANÁLISE ===")
    print(f"Total de caracteres (com espaços): {caracteres}")
    print(f"Total de palavras: {palavras}")
    print(f"Texto invertido: {invertido}")
    print("=============================")

# Garante que o script rode apenas se executado diretamente
if __name__ == "__main__":
    executar_programa()
