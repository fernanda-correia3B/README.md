def analisar_texto(texto):
    total_caracteres = len(texto)
    total_palavras = len(texto.split())
    texto_invertido = texto[::-1]
    return total_caracteres, total_palavras, texto_invertido

def executar_programa():
    print("\n--- BEM-VINDO AO ANALISADOR DE TEXTO ---")
    entrada = input("Digite uma frase ou texto para analisar: ")
    
    if not entrada.strip():
        print("Erro: Você não digitou nenhum texto válido.")
        return

    caracteres, palavras, invertido = analisar_texto(entrada)
    
    print("\n=== RESULTADOS DA ANÁLISE ===")
    print(f"Total de caracteres (com espaços): {caracteres}")
    print(f"Total de palavras: {palavras}")
    print(f"Texto invertido: {invertido}")
    print("=============================")

if __name__ == "__main__":
    executar_programa()

