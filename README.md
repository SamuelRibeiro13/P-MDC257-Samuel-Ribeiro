# Portfólio de Programação Matemática - Partes 1 e 2

## Identificação
- **Aluno:** Samuel Ribeiro
- **Matrícula:** 2612130058
- **Disciplina:** Estruturas Matemáticas para Computação
- **Turno:** Matutino

---

## Atividade 1 – Teoria dos Conjuntos

### Arquivo
`P1/atividade_01_conjuntos/conjuntos.py`

### Como executar
Abra o terminal no diretório raiz do projeto e execute:
```bash
python P1/atividade_01_conjuntos/conjuntos.py
```

O programa apresenta o cabeçalho de identificação e, em seguida, solicita os elementos dos conjuntos A e B (separados por espaço).

### Exemplo de entrada
```text
Digite os elementos do conjunto A (separados por espaço): 1 2 3 4
Digite os elementos do conjunto B (separados por espaço): 3 4 5 6
```

### O programa apresenta:
- União ($A \cup B$);
- Interseção ($A \cap B$);
- Diferenças ($A - B$ e $B - A$);
- Cardinalidades ($|A|$, $|B|$, $|A \cup B|$, $|A \cap B|$);
- Conjunto das partes ($\mathcal{P}(A)$ e $\mathcal{P}(B)$);
- Cardinalidade do conjunto das partes ($2^{|A|}$ e $2^{|B|}$);
- Exemplo de partição de um dos conjuntos;
- Produto cartesiano ($A \times B$);
- Relações de inclusão ($A \subseteq B$ e $B \subseteq A$).

---

## Atividade 2 – Divisibilidade, MDC e MMC

### Arquivo
`P1/atividade_02_divisibilidade/divisibilidade.py`

### Como executar
Abra o terminal no diretório raiz do projeto e execute:
```bash
python P1/atividade_02_divisibilidade/divisibilidade.py
```

O programa apresenta o cabeçalho de identificação e, em seguida, solicita dois números inteiros positivos.

### Exemplo de entrada
```text
Digite o primeiro número: 48
Digite o segundo número: 18
```

### O programa apresenta:
- Divisão inteira (DIV);
- Resto da divisão (MOD);
- Passo a passo completo do Algoritmo de Euclides;
- Maior Divisor Comum (MDC);
- Mínimo Múltiplo Comum (MMC), calculado pela relação fundamental estudada em aula.

---

# Parte 2

## Atividade 1 – Congruência Modular e Teorema Chinês do Resto

### Arquivo
`P2/atividade_01_congruencia_tcr/congruencia_tcr.py`

### Como executar
```bash
python P2/atividade_01_congruencia_tcr/congruencia_tcr.py
```

O programa apresenta um menu com duas opções:
- **Parte A:** pede $a$, $b$ e $n$ ($n > 0$) e verifica se $a \equiv b \pmod n$, mostrando $a - b$ e o resto da divisão por $n$;
- **Parte B:** pede 3 ou 4 congruências $x \equiv a_i \pmod{n_i}$, verifica se os módulos são coprimos dois a dois e resolve o sistema pelo Teorema Chinês do Resto, mostrando $N$, $N_i$, os inversos $s_i$, a solução $x_0$, a solução geral $x_0 + tN$ e a verificação em cada congruência.

Documento explicativo: `P2/atividade_01_congruencia_tcr/documento_atividade_01.md`

---

## Atividade 2 – Criptografia RSA

### Arquivo
`P2/atividade_02_rsa/rsa.py`

### Como executar
```bash
python P2/atividade_02_rsa/rsa.py
```

### Exemplo de entrada
```text
p = 61, q = 53, e = 17, M = 65
```

### O programa apresenta:
- Parte A: verificação de primalidade de $p$ e $q$, $n = p \cdot q$, $\phi(n) = (p-1)(q-1)$ e verificação de $\text{mdc}(e, \phi(n)) = 1$;
- Parte B: expoente privado $d$ (Euclides Estendido) e chaves pública e privada;
- Parte C: cifragem $C \equiv M^e \pmod n$ e decifragem $M' \equiv C^d \pmod n$, com as etapas da exponenciação modular;
- Parte D: Teorema de Euler, Pequeno Teorema de Fermat e as condições de aplicação de cada um.

Documento explicativo: `P2/atividade_02_rsa/documento_atividade_02.md`

Roteiro com perguntas e respostas para a apresentação: `P2/roteiro_apresentacao.md`

---

## Interface Gráfica Interativa (Opcional / Extra)

Para executar a aplicação com interface visual moderna e interativa:
```bash
python app_gui.py
```
A documentação completa dos recursos, design e filtros da interface pode ser conferida em [DOCUMENTACAO_GUI.md](file:///DOCUMENTACAO_GUI.md).
