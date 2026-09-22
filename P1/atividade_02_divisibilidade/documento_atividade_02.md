# Relatório Técnico - Atividade 2: Divisibilidade, MDC e MMC

## 1. Identificação do Aluno
- **Nome:** Samuel Ribeiro
- **Matrícula:** 2612130058
- **Disciplina:** Estruturas Matemáticas para Computação (Matemática Discreta)
- **Turno:** Matutino

---

## 2. Descrição do Problema
O objetivo desta atividade é implementar um programa em Python que receba do usuário dois números inteiros positivos e calcule:
1. A divisão inteira (DIV);
2. O resto da divisão (MOD);
3. O passo a passo detalhado do Algoritmo de Euclides;
4. O Maior Divisor Comum (MDC) resultante;
5. O Mínimo Múltiplo Comum (MMC) calculado a partir da relação fundamental estudada em sala de aula.

O programa foi desenvolvido sem o uso de funções prontas de cálculo (como `math.gcd()`), implementando diretamente o algoritmo de divisões sucessivas.

---

## 3. Procedimento Matemático Utilizado

1. **Teorema da Divisão Euclidiana:**
   Dados dois inteiros $a$ e $b$ com $b > 0$, existem inteiros únicos $q$ (quociente) e $r$ (resto) tais que:
   $$a = b \times q + r \quad \text{onde } 0 \le r < b$$
   Em computação, $q = a \text{ // } b$ (DIV) e $r = a \pmod b$ (MOD).

2. **Algoritmo de Euclides para o MDC:**
   Baseia-se no princípio de que o máximo divisor comum entre dois números também divide o resto da sua divisão:
   $$\text{MDC}(a, b) = \text{MDC}(b, r)$$
   O procedimento consiste em repetidas divisões inteiras até que o resto seja zero. O último divisor (ou último resto não nulo) corresponde ao $\text{MDC}(a, b)$.

3. **Relação Fundamental entre MDC e MMC:**
   Para quaisquer dois inteiros positivos $a$ e $b$, o produto entre o MDC e o MMC é igual ao produto dos próprios números:
   $$\text{MDC}(a, b) \times \text{MMC}(a, b) = a \times b$$
   Dessa forma, o MMC pode ser calculado diretamente através de:
   $$\text{MMC}(a, b) = \frac{a \times b}{\text{MDC}(a, b)}$$

---

## 4. Breve Explicação da Implementação
- **Entrada com validação:** A função `ler_inteiro_positivo` solicita os números ao usuário e garante, através de um laço `while` e tratamento com `try/except`, que somente inteiros positivos ($> 0$) sejam aceitos. Entradas incorretas são rejeitadas sem interrupção do programa.
- **Divisão inteira e resto:** Calculados diretamente com os operadores nativos de Python `//` e `%`.
- **Algoritmo de Euclides:** A função `calcular_mdc_euclides_com_passos` realiza o laço `while divisor != 0:`, calculando $q$ e $r$ a cada iteração e registrando a linha correspondente no formato $a = b \times q + r$. Ao término do laço, o último dividendo é retornado como o MDC.
- **Cálculo do MMC:** Realizado aplicando a fórmula $(a \times b) \text{ // MDC}(a, b)$.

---

## 5. Exemplos de Testes

### Teste 1: Valores com divisor comum
- **Entrada:**
  - Primeiro número: $48$
  - Segundo número: $18$
- **Resultados Obtidos:**
  - $48 \text{ // } 18 = 2$
  - $48 \pmod{18} = 12$ ($48 = 18 \times 2 + 12$)
  - **Passo a passo de Euclides:**
    - $48 = 18 \times 2 + 12$
    - $18 = 12 \times 1 + 6$
    - $12 = 6 \times 2 + 0$
  - $\text{MDC}(48, 18) = 6$
  - $\text{MMC}(48, 18) = (48 \times 18) \text{ // } 6 = 144$

### Teste 2: Números primos entre si (MDC = 1)
- **Entrada:**
  - Primeiro número: $35$
  - Segundo número: $12$
- **Resultados Obtidos:**
  - **Passo a passo de Euclides:**
    - $35 = 12 \times 2 + 11$
    - $12 = 11 \times 1 + 1$
    - $11 = 1 \times 11 + 0$
  - $\text{MDC}(35, 12) = 1$
  - $\text{MMC}(35, 12) = (35 \times 12) \text{ // } 1 = 420$

### Teste 3: Múltiplos
- **Entrada:**
  - Primeiro número: $60$
  - Segundo número: $20$
- **Resultados Obtidos:**
  - $60 = 20 \times 3 + 0$
  - $\text{MDC}(60, 20) = 20$
  - $\text{MMC}(60, 20) = (60 \times 20) \text{ // } 20 = 60$
