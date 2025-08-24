def karatsuba(x, y):
    """
    Implementação do algoritmo de Karatsuba para multiplicação de números inteiros grandes.
    
    Args:
        x (int): Primeiro número a ser multiplicado
        y (int): Segundo número a ser multiplicado
    
    Returns:
        int: O produto de x e y
    """
    # Caso base: se qualquer um dos números for pequeno o suficiente, use multiplicação tradicional
    if x < 10 or y < 10:
        return x * y
    
    # Calcula o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Divide os números em partes altas e baixas
    high1 = x // 10**m
    low1 = x % 10**m
    high2 = y // 10**m
    low2 = y % 10**m
    
    # Realiza as três recursões necessárias para o algoritmo de Karatsuba
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)
    
    # Combina os resultados usando a fórmula de Karatsuba
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

def main():
    """
    Função principal para testar o algoritmo de Karatsuba.
    """
    print("Algoritmo de Karatsuba para Multiplicação de Números Grandes")
    print("=" * 60)
    
    # Teste com números de exemplo
    num1 = 12345678901234567890
    num2 = 98765432109876543210
    
    print(f"Número 1: {num1}")
    print(f"Número 2: {num2}")
    print("-" * 60)
    
    # Calcula usando Karatsuba
    resultado = karatsuba(num1, num2)
    
    # Verifica com a multiplicação padrão do Python
    esperado = num1 * num2
    
    print(f"Resultado Karatsuba: {resultado}")
    print(f"Resultado Esperado:  {esperado}")
    print("-" * 60)
    print(f"Resultado correto: {resultado == esperado}")

if __name__ == "__main__":
    main()