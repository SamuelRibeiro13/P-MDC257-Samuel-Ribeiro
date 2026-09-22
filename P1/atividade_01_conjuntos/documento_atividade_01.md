# Relatório Técnico - Atividade 1: Teoria dos Conjuntos

## 1. Identificação do Aluno
- **Nome:** Samuel Ribeiro
- **Matrícula:** 2612130058
- **Disciplina:** Estruturas Matemáticas para Computação (Matemática Discreta)
- **Turno:** Matutino

---

## 2. Descrição do Problema
O objetivo desta atividade é implementar um programa em Python capaz de ler dois conjuntos numéricos finitos ($A$ e $B$) informados pelo usuário e calcular as principais operações fundamentais da Teoria dos Conjuntos: união, interseção, diferenças, cardinalidades, conjunto das partes com sua respectiva cardinalidade, um exemplo prático de partição, produto cartesiano e verificação de inclusão.

---

## 3. Procedimento Matemático Utilizado

1. **União ($A \cup B$):** 
   Conjunto de todos os elementos que pertencem a $A$, a $B$, ou a ambos:
   $$A \cup B = \{x \mid x \in A \lor x \in B\}$$

2. **Interseção ($A \cap B$):**
   Conjunto dos elementos comuns a ambos os conjuntos:
   $$A \cap B = \{x \mid x \in A \land x \in B\}$$

3. **Diferenças ($A - B$ e $B - A$):**
   - $A - B = \{x \mid x \in A \land x \notin B\}$ (elementos exclusivos de $A$).
   - $B - A = \{x \mid x \in B \land x \notin A\}$ (elementos exclusivos de $B$).

4. **Cardinalidade ($|X|$):**
   Número de elementos distintos contidos no conjunto $X$.

5. **Conjunto das Partes ($\mathcal{P}(X)$):**
   Conjunto formado por todos os subconjuntos de $X$, incluindo o conjunto vazio $\emptyset$ e o próprio conjunto $X$.
   Sua cardinalidade é dada por $|\mathcal{P}(X)| = 2^{|X|}$.

6. **Partição de um Conjunto:**
   Uma partição de $A$ é uma família de subconjuntos não vazios $\{A_1, A_2, \dots, A_k\}$ de $A$ disjuntos dois a dois ($A_i \cap A_j = \emptyset$ para $i \neq j$) cuja união é o próprio conjunto $A$ ($\bigcup A_i = A$). No trabalho, foi utilizada a partição natural de $A$ com base na paridade dos elementos (números pares e números ímpares).

7. **Produto Cartesiano ($A \times B$):**
   Conjunto de todos os pares ordenados $(a, b)$ tais que $a \in A$ e $b \in B$:
   $$A \times B = \{(a, b) \mid a \in A \land b \in B\}$$
   com cardinalidade $|A \times B| = |A| \times |B|$.

8. **Relação de Inclusão ($A \subseteq B$):**
   $A$ é subconjunto de $B$ se e somente se todo elemento de $A$ pertencer a $B$:
   $$\forall x (x \in A \implies x \in B)$$

---

## 4. Breve Explicação da Implementação
- **Entrada de dados e validação:** A função `ler_conjunto` recebe a sequência de dados digitada pelo usuário, converte para números inteiros e elimina repetições mantendo a definição estrita de conjunto. Um tratamento com `try/except` impede que entradas inválidas interrompam o programa.
- **Operações básicas:** As operações de união, interseção e diferença foram implementadas utilizando laços `for` e condicionais `if`, respeitando as regras de não utilizar métodos prontos que mascarem a lógica do algoritmo.
- **Conjunto das partes:** Construído de forma recursiva/iterativa iniciando com `[[]]`. Para cada elemento, ele é concatenado a cada um dos subconjuntos já formados.
- **Partição:** O algoritmo classifica os elementos de $A$ em listas de pares e ímpares. Caso existam ambos, forma a partição $\{A_{\text{pares}}, A_{\text{ímpares}}\}$. Se todos tiverem a mesma paridade, divide $A$ em dois blocos disjuntos.

---

## 5. Exemplos de Testes

### Teste 1: Conjuntos com elementos em comum
- **Entrada:**
  - $A = \{1, 2, 3, 4\}$
  - $B = \{3, 4, 5, 6\}$
- **Resultados Obtidos:**
  - $A \cup B = \{1, 2, 3, 4, 5, 6\}$
  - $A \cap B = \{3, 4\}$
  - $A - B = \{1, 2\}$
  - $B - A = \{5, 6\}$
  - $|A| = 4, |B| = 4, |A \cup B| = 6, |A \cap B| = 2$
  - $|\mathcal{P}(A)| = 16 = 2^4$
  - Partição de $A$: $A_1 = \{2, 4\}$ (pares), $A_2 = \{1, 3\}$ (ímpares)
  - $|A \times B| = 16$ pares ordenados
  - $A \subseteq B$: Não; $B \subseteq A$: Não.

### Teste 2: Conjuntos disjuntos
- **Entrada:**
  - $A = \{1, 2\}$
  - $B = \{3, 4\}$
- **Resultados Obtidos:**
  - $A \cup B = \{1, 2, 3, 4\}$
  - $A \cap B = \emptyset$
  - $A - B = \{1, 2\}$
  - $B - A = \{3, 4\}$
  - $|A \cap B| = 0$
  - $|\mathcal{P}(A)| = 4 = 2^2$
