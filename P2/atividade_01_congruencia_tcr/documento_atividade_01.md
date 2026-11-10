# Relatório Técnico - Atividade 1: Congruência Modular e Teorema Chinês do Resto

## 1. Identificação do Aluno
- **Nome:** Samuel Ribeiro
- **Matrícula:** 2612130058
- **Disciplina:** Estruturas Matemáticas para Computação (Matemática Discreta)
- **Turno:** Matutino

---

## 2. Descrição do Problema
O objetivo desta atividade é implementar em Python dois procedimentos:

- **Parte A:** dados três inteiros $a$, $b$ e $n$ (com $n > 0$), verificar se $a \equiv b \pmod n$, mostrando o cálculo realizado e justificando o resultado.
- **Parte B:** resolver um sistema de três ou quatro congruências lineares $x \equiv a_i \pmod{n_i}$, com módulos positivos e coprimos dois a dois, usando o Teorema Chinês do Resto (TCR).

O programa não utiliza funções prontas que resolvam o problema (como `math.gcd`). O MDC e o inverso multiplicativo foram implementados no próprio código.

---

## 3. Procedimento Matemático Utilizado

### Parte A: Congruência modular
Por definição, $a \equiv b \pmod n$ se, e somente se, $n$ divide $a - b$, isto é, se o resto da divisão de $a - b$ por $n$ é zero:

$$a \equiv b \pmod n \iff n \mid (a - b) \iff (a - b) \bmod n = 0$$

Passos do programa: ler $a$, $b$, $n$ (validando $n > 0$); calcular $a - b$; calcular o resto da divisão por $n$; verificar se é zero; apresentar a conclusão.

### Parte B: Teorema Chinês do Resto
Para o sistema $x \equiv a_i \pmod{n_i}$, $i = 1, \dots, k$ ($k = 3$ ou $4$), com $\text{mdc}(n_i, n_j) = 1$ para $i \neq j$:

1. **Verificação:** os módulos são positivos e coprimos dois a dois (MDC calculado pelo Algoritmo de Euclides para cada par). Caso contrário, o programa informa que o sistema está fora das condições da atividade.
2. **Produto dos módulos:** $N = n_1 \cdot n_2 \cdots n_k$.
3. **Valores $N_i$:** $N_i = N / n_i$.
4. **Inverso multiplicativo:** encontrar $s_i$ tal que $N_i \cdot s_i \equiv 1 \pmod{n_i}$. Ele existe porque $\text{mdc}(N_i, n_i) = 1$.
5. **Solução particular:**
   $$x_0 = \left(\sum_{i=1}^{k} a_i \cdot N_i \cdot s_i\right) \bmod N$$
6. **Solução geral:** $x = x_0 + t \cdot N$, com $t \in \mathbb{Z}$.
7. **Verificação:** conferir que $x_0 \bmod n_i = a_i \bmod n_i$ para todo $i$.

---

## 4. Breve Explicação da Implementação
- **Leitura de dados:** `ler_inteiro` e `ler_inteiro_positivo` repetem o pedido enquanto a entrada for inválida (texto, decimal, ou módulo menor ou igual a zero).
- **MDC:** `calcular_mdc` implementa o Algoritmo de Euclides e devolve também cada divisão `dividendo = divisor × quociente + resto`, que é exibida na tela.
- **Coprimos dois a dois:** `sao_coprimos_dois_a_dois` percorre todos os pares com dois laços `for` aninhados e imprime o MDC de cada par.
- **Inverso multiplicativo:** `inverso_modular_por_busca` testa $s = 1, 2, \dots, n_i - 1$ e para no primeiro valor com $(N_i \cdot s) \bmod n_i = 1$. O resto de $N_i$ por $n_i$ é usado para trabalhar com números menores. Para módulos maiores que 30, as tentativas intermediárias não são impressas. Para módulo 1 qualquer $s$ serve, e o programa usa $s = 1$.
- **Resto negativo:** quando $n > 0$, o operador `%` do Python devolve resto entre $0$ e $n - 1$, que é a convenção matemática usada na Parte A.
- **Menu:** o programa repete um menu até o usuário escolher sair, permitindo testar vários casos numa mesma execução.

**Como executar:**
```bash
python P2/atividade_01_congruencia_tcr/congruencia_tcr.py
```

---

## 5. Exemplos de Testes

### Teste 1 (Parte A): congruência verdadeira
- **Entrada:** $a = 23$, $b = 8$, $n = 5$
- **Resultado:**
  - $a - b = 15$
  - $15 = 5 \times 3 + 0$, resto $0$
  - Conclusão: $23 \equiv 8 \pmod 5$

### Teste 2 (Parte A): congruência falsa
- **Entrada:** $a = 10$, $b = 3$, $n = 4$
- **Resultado:**
  - $a - b = 7$
  - $7 = 4 \times 1 + 3$, resto $3$
  - Conclusão: $10$ não é congruente a $3$ módulo $4$.

### Teste 3 (Parte A): diferença negativa
- **Entrada:** $a = -7$, $b = 2$, $n = 3$
- **Resultado:** $a - b = -9 = 3 \times (-3) + 0$, logo $-7 \equiv 2 \pmod 3$.

### Teste 4 (Parte A): entradas inválidas
- Digitar `abc` para $a$: o programa avisa e pede novamente.
- Digitar `0` como módulo: o programa informa que o valor precisa ser maior que zero e pede novamente.

### Teste 5 (Parte B): sistema clássico com 3 congruências
- **Entrada:**
  - $x \equiv 2 \pmod 3$
  - $x \equiv 3 \pmod 5$
  - $x \equiv 2 \pmod 7$
- **Resultado:**
  - Todos os pares de módulos têm MDC igual a 1.
  - $N = 3 \cdot 5 \cdot 7 = 105$
  - $N_1 = 35$, $N_2 = 21$, $N_3 = 15$
  - $s_1 = 2$, $s_2 = 1$, $s_3 = 1$
  - Soma $= 2 \cdot 35 \cdot 2 + 3 \cdot 21 \cdot 1 + 2 \cdot 15 \cdot 1 = 233$
  - $x_0 = 233 \bmod 105 = 23$
  - Solução geral: $x = 23 + 105t$, $t \in \mathbb{Z}$
  - Verificação: $23 \bmod 3 = 2$, $23 \bmod 5 = 3$, $23 \bmod 7 = 2$

### Teste 6 (Parte B): sistema com 4 congruências e módulos maiores
- **Entrada:** $x \equiv 1 \pmod{31}$, $x \equiv 5 \pmod{32}$, $x \equiv 7 \pmod{37}$, $x \equiv 11 \pmod{41}$
- **Resultado:**
  - $N = 1\,504\,864$
  - $x_0 = 799\,429$
  - As quatro verificações $x_0 \bmod n_i = a_i$ foram confirmadas.

### Teste 7 (Parte B): módulos não coprimos
- **Entrada:** módulos $2$, $2$, $3$ e $1$ (com restos quaisquer).
- **Resultado:** o programa calcula $\text{mdc}(2, 2) = 2$ e informa que os módulos não são coprimos dois a dois, ficando o sistema fora das condições previstas.

### Teste 8 (Parte B): quantidade inválida
- Digitar `5` como quantidade de congruências: o programa informa que só aceita 3 ou 4 e pede novamente.
