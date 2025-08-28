# Implementação do Algoritmo de Karatsuba em Python

O **Algoritmo de Karatsuba** é uma técnica eficiente para multiplicação de números inteiros grandes, desenvolvida por Anatolii Karatsuba em 1960. Este projeto implementa esse algoritmo em Python, demonstrando sua superioridade em comparação com o método tradicional de multiplicação.

## Complexidade Assintótica

A **complexidade assintótica** é uma maneira de expressar o comportamento de um algoritmo quando o tamanho da entrada tende ao infinito. Ela descreve o tempo ou espaço de execução de um algoritmo em termos do tamanho da entrada, ignorando fatores como o hardware ou o tempo de execução real. A complexidade assintótica ajuda a comparar a eficiência de diferentes algoritmos de forma mais objetiva, independentemente das condições do sistema.

## Diferença entre Complexidade Assintótica e Complexidade Ciclomática

A **complexidade assintótica** refere-se ao comportamento de um algoritmo à medida que a entrada aumenta, enquanto a **complexidade ciclomática** mede a complexidade do código de um programa com base no número de caminhos lineares independentes no código. A complexidade ciclomática é útil para determinar a quantidade de testes necessários para garantir a cobertura adequada do código.

## Algoritmo de Karatsuba

### Descrição do Algoritmo

O algoritmo de Karatsuba segue uma abordagem "dividir para conquistar" para multiplicação de números grandes:

1. **Caso base**: Se os números são pequenos, usa multiplicação tradicional
2. **Divisão**: Separa cada número em duas partes de tamanho aproximadamente igual
3. **Recursão**: Realiza três multiplicações recursivas com números menores
4. **Combinação**: Usa uma fórmula específica para combinar os resultados

### Implementação Linha a Linha

```python
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
    m = n // 2  # Ponto médio para divisão
    
    # Divide x em partes alta e baixa
    high1 = x // 10**m  # Parte alta de x
    low1 = x % 10**m    # Parte baixa de x
    
    # Divide y em partes alta e baixa
    high2 = y // 10**m  # Parte alta de y
    low2 = y % 10**m    # Parte baixa de y
    
    # Três multiplicações recursivas necessárias para o algoritmo
    z0 = karatsuba(low1, low2)                    # Multiplica partes baixas
    z1 = karatsuba((low1 + high1), (low2 + high2)) # Multiplica somas das partes
    z2 = karatsuba(high1, high2)                  # Multiplica partes altas
    
    # Combina os resultados usando a fórmula de Karatsuba
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0
```

## Como Executar o Projeto

### Pré-requisitos
- Python 3.6 ou superior instalado

### Execução Direta
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/trabalho_individual_1_FPAA.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd trabalho_individual_1_FPAA
   ```

3. Execute o programa:
   ```bash
   python main.py
   ```

### Usando Ambiente Virtual (Recomendado)

1. Crie um ambiente virtual:
   ```bash
   python3 -m venv .venv
   ```

2. Ative o ambiente virtual:
   - No macOS e Linux:
     ```bash
     source .venv/bin/activate
     ```
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```

3. Execute o programa:
   ```bash
   python main.py
   ```

4. Para desativar o ambiente virtual:
   ```bash
   deactivate
   ```

## Relatório Técnico

### Análise da Complexidade Ciclomática

#### Fluxo de Controle da Função
A função `karatsuba` possui o seguinte fluxo de controle:
1. Início do código
2. Verificação do caso base (if)
3. se verdadeiro, Retorna x*y 
4. se falso, N = max(len(str(x)), len(str(y)))
5. M = n/2
6. Divide x em high e low
7. Divide x em high e low
8. Três chamadas recursivas
9. Combinação dos resultados

#### Cálculo da Complexidade Ciclomática
Usando a fórmula M = E - N + 2P:
- Número de arestas (E): 9
- Número de nós (N): 9
- Número de componentes conexos (P): 1

M = 9 - 9 + 2*1 = 2

A complexidade ciclomática é 2, indicando que o código tem uma complexidade simples com 2 caminhos independentes possíveis: multiplicação tradicional para números pequenos ou aplicação do algoritmo de karatsuba para números grandes.

#### Grafo de Fluxo
!{Karatsuba.png}

### Análise da Complexidade Assintótica
O algoritmo de Karatsuba tem complexidade temporal de O(n^log₂3) ≈ O(n^1.585), que é uma melhoria significativa em relação ao algoritmo tradicional de multiplicação que é O(n²).

- **Melhor caso**: O(1) - quando os números são pequenos o suficiente para usar multiplicação direta
- **Caso médio**: O(n^log₂3) - a complexidade esperada do algoritmo
- **Pior caso**: O(n^log₂3) - mesmo no pior caso, mantém a mesma complexidade


## Exemplo de Saída

```
Algoritmo de Karatsuba para Multiplicação de Números Grandes
============================================================
Número 1: 12345678901234567890
Número 2: 98765432109876543210
============================================================
Resultado Karatsuba: 1219326311370217952237463801111263526900
Resultado Esperado:  1219326311370217952237463801111263526900
============================================================
Resultado correto: True
```

## Referências
- Karatsuba, A. (1962). "Multiplication of Many-Digital Numbers by Automatic Computers". Proceedings of the USSR Academy of Sciences.
- Wikipedia: Algoritmo de Karatsuba

## Licença
Este projeto está licenciado sob a Licença MIT.