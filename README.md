# Portfólio de Programação Matemática - Parte 1

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

## Interface Gráfica Interativa (Opcional / Extra)

Para executar a aplicação com interface visual moderna e interativa:
```bash
python app_gui.py
```
A documentação completa dos recursos, design e filtros da interface pode ser conferida em [DOCUMENTACAO_GUI.md](file:///DOCUMENTACAO_GUI.md).
