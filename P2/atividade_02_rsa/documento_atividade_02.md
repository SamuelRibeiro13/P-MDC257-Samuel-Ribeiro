# Relatório Técnico - Atividade 2: Criptografia RSA

## 1. Identificação do Aluno
- **Nome:** Samuel Ribeiro
- **Matrícula:** 2612130058
- **Disciplina:** Estruturas Matemáticas para Computação (Matemática Discreta)
- **Turno:** Matutino

---

## 2. Descrição do Problema
O objetivo desta atividade é construir um programa simplificado de criptografia RSA em Python, aplicando verificação de números primos, função totiente de Euler, inverso multiplicativo e exponenciação modular. O programa trabalha com um número inteiro $M$ (e não com textos completos) e é dividido em quatro partes:

- **Parte A:** verificar primalidade de $p$ e $q$ e calcular os parâmetros $n$, $\phi(n)$ e o expoente público $e$.
- **Parte B:** construir o expoente privado $d$ e as chaves pública e privada.
- **Parte C:** cifrar e decifrar um número inteiro $M$.
- **Parte D:** demonstrar os Teoremas de Euler e de Fermat na exponenciação modular.

O programa não usa funções prontas que resolvam o problema (`math.gcd`, `pow(a, b, n)`, `pow(a, -1, n)`, bibliotecas externas). Todos os procedimentos centrais foram implementados no código, e os passos são impressos na tela.

---

## 3. Procedimento Matemático Utilizado

### Parte A: Primalidade e parâmetros
1. **Primalidade:** um inteiro $m > 1$ é composto se tem divisor $d$ com $2 \le d \le \sqrt{m}$. Basta testar os divisores até $\sqrt{m}$.
2. **Módulo:** $n = p \cdot q$.
3. **Função totiente de Euler**, para o produto de dois primos distintos:
   $$\phi(n) = (p - 1)(q - 1)$$
4. **Expoente público $e$:** $1 < e < \phi(n)$ e $\text{mdc}(e, \phi(n)) = 1$, verificado pelo Algoritmo de Euclides.

### Parte B: Chaves
O expoente privado $d$ é o inverso multiplicativo de $e$ módulo $\phi(n)$:
$$e \cdot d \equiv 1 \pmod{\phi(n)}$$

Ele é obtido pelo **Algoritmo de Euclides Estendido**, que encontra $x$ e $y$ com $e \cdot x + \phi(n) \cdot y = \text{mdc}(e, \phi(n)) = 1$. Daí $e \cdot x \equiv 1 \pmod{\phi(n)}$, e $d = x \bmod \phi(n)$ (o $x$ pode sair negativo).
- Chave pública: $(e, n)$
- Chave privada: $(d, n)$

### Parte C: Cifragem e decifragem
$$C \equiv M^e \pmod n \qquad M' \equiv C^d \pmod n$$
com $0 \le M < n$. A decifragem funciona porque $e \cdot d = 1 + k\,\phi(n)$, logo $M^{ed} \equiv M \pmod n$ (justificativa na Parte D).

### Exponenciação modular rápida
Para não construir potências gigantes, o expoente é lido em binário, do bit menos significativo ao mais significativo. Se o bit é 1, multiplica-se o resultado pela base atual; em seguida eleva-se a base ao quadrado. Toda multiplicação é reduzida módulo $n$.

### Parte D: Teoremas de Euler e Fermat
- **Euler:** se $\text{mdc}(a, n) = 1$, então $a^{\phi(n)} \equiv 1 \pmod n$.
  Consequência: como $e \cdot d = 1 + k\,\phi(n)$,
  $$M^{ed} = M \cdot (M^{\phi(n)})^k \equiv M \cdot 1^k \equiv M \pmod n$$
- **Pequeno Teorema de Fermat:** se $p$ é primo e $p \nmid a$, então $a^{p-1} \equiv 1 \pmod p$.
- **Condições:** Fermat exige módulo primo, e $n = p \cdot q$ é composto, portanto não se aplica diretamente a $n$. Euler exige $\text{mdc}(a, n) = 1$. Quando nenhuma condição vale, a exponenciação modular por reduções sucessivas continua válida.

---

## 4. Breve Explicação da Implementação
- **`ler_inteiro`:** repete o pedido enquanto a entrada não for um inteiro.
- **`calcular_mdc`:** Algoritmo de Euclides, imprimindo cada divisão `dividendo = divisor × quociente + resto`.
- **`eh_primo`:** testa os divisores de 2 até $\sqrt{n}$ (o limite é achado com um laço `while`, sem bibliotecas). Se $\sqrt{n} \le 30$, imprime cada divisão. Para valores maiores, imprime apenas o resumo.
- **`euclides_estendido`:** mantém os coeficientes de cada resto e imprime a tabela `q | resto | x | y`.
- **`inverso_modular`:** usa o Euclides Estendido e devolve $x \bmod m$ (ou `None` se o MDC for diferente de 1).
- **`exponenciacao_modular`:** quadrados sucessivos, mostrando o binário do expoente, cada multiplicação e cada elevação ao quadrado.
- **`parte_a` a `parte_d`:** cada parte devolve seus resultados para a seguinte. O programa roda de A a D em sequência e pergunta no fim se deseja executar novamente.
- **Casos em que não há $e$:** se $(p-1)(q-1) \le 2$, não existe $e$ com $1 < e < \phi(n)$, e o programa pede novos primos.

**Como executar:**
```bash
python P2/atividade_02_rsa/rsa.py
```

---

## 5. Exemplos de Testes

### Teste 1: exemplo clássico
- **Entrada:** $p = 61$, $q = 53$, $e = 17$, $M = 65$, base de Fermat $a = 3$
- **Resultados obtidos:**
  - $n = 3233$, $\phi(n) = 3120$
  - $\text{mdc}(17, 3120) = 1$
  - $d = 2753$, e $17 \cdot 2753 = 46801 = 1 + 15 \cdot 3120$, com resto 1 módulo $3120$
  - Chave pública $(17, 3233)$, chave privada $(2753, 3233)$
  - $C = 65^{17} \bmod 3233 = 2790$
  - $M' = 2790^{2753} \bmod 3233 = 65 = M$
  - Euler: $\text{mdc}(65, 3233) = 1$ e $65^{3120} \equiv 1 \pmod{3233}$
  - Fermat: $3^{60} \equiv 1 \pmod{61}$ e $3^{52} \equiv 1 \pmod{53}$

### Teste 2: $p$ não primo
- **Entrada:** $p = 15$, $q = 53$
- **Resultado:** $15 \bmod 3 = 0$, então 15 não é primo. O programa pede novos valores.

### Teste 3: $p = q$
- **Entrada:** $p = 61$, $q = 61$
- **Resultado:** o programa informa que $p$ e $q$ precisam ser distintos e pede novos valores.

### Teste 4: $e$ não coprimo com $\phi(n)$
- **Entrada:** $p = 61$, $q = 53$, $e = 6$
- **Resultado:** $\text{mdc}(6, 3120) = 6$. O programa recusa o valor e pede outro $e$.

### Teste 5: mensagem não coprima com $n$
- **Entrada:** $p = 61$, $q = 53$, $e = 17$, $M = 122$ ($= 2 \cdot 61$), base de Fermat $a = 61$
- **Resultados obtidos:**
  - $\text{mdc}(122, 3233) = 61$, então o Teorema de Euler **não** se aplica.
  - $122^{3120} \bmod 3233 = 1220$, que não é 1.
  - A cifragem e a decifragem ainda recuperam $M' = 122 = M$, pois a exponenciação modular por reduções sucessivas continua válida.
  - Fermat com base $61$ e módulo $p = 61$: o programa informa que $61 \mid 61$ e que o teorema não se aplica. Com o módulo $q = 53$, confirma $61^{52} \equiv 1 \pmod{53}$.

### Teste 6: entradas inválidas
- Digitar texto como `abc` onde se espera um inteiro: o programa avisa e pede novamente.
- Digitar $M \ge n$ ou $M < 0$: o programa informa o intervalo $0 \le M < n$ e pede novamente.
