# Documentação Técnica - Interface Gráfica (`app_gui.py`)

## 1. Visão Geral e Objetivo
O aplicativo `app_gui.py` foi desenvolvido como um complemento interativo de alta usabilidade para aumentar a **a Showde bolice do Samuel** na disciplina de Estruturas Matemáticas para Computação ja que no dia 22/09 ele ficou sem demandas no trabalho.

Ele permite executar visualmente todos os procedimentos matemáticos das Atividades 1 e 2, mantendo uma experiência de uso fluida, moderna e limpa, consumindo de maneira modular as funções implementadas nos scripts da pasta `P1/`.

---

## 2. Decisões de UX/UI Design

- **Paleta de Cores Deep Slate & Neon Accents:**
  - Fundo ultra-escuro (`#0b0f19`) com superfícies de cards em camadas (`#141c2e` e `#1a243a`).
  - Destaques funcionais em Índigo (`#4f46e5`), Ciano (`#38bdf8`), Esmeralda (`#10b981`) e Âmbar (`#f59e0b`).
- **Cards Métricos de Resumo Rápido:**
  - Na aba de Conjuntos: Exibição em cards dos valores instantâneos de $|A|$, $|B|$, $|A \cup B|$, $|A \cap B|$ e status de $A \subseteq B$.
  - Na aba de Divisibilidade: Exibição destacada dos valores de $\text{DIV}$, $\text{MOD}$, $\text{MDC}$ e $\text{MMC}$.
- **Banner de Alerta Integrado (In-App Toast):**
  - Em vez de um popup padrão do Windows, um banner estilizado vermelho/rosa surge no topo da aplicação caso a entrada seja inválida, exibindo `"Hoje não Cristiane tenta outra coisa."` com auto-dispensa ou fechamento manual (recomendo o teste).
- **Botões de Teste Rápido:**
  - Botões para carregar rapidamente dados de teste (ex: `48 e 18`, números primos `35 e 12`).
- **Acessibilidade e Agilidade:**
  - Layout dividido em duas abas principais com alternância instantânea estilo segmented control.
  - Botão dedicado de **"Copiar Resultados"** que transfere toda a saída formatada para a área de transferência do sistema operacional.
  - Barra de status na base da janela com retorno em tempo real de cada ação executada.

---

## 3. Sistema de Filtragem de Inputs (Anti-Crash & Anti-Pegadinha)

A interface possui uma camada dupla de proteção para impedir que entradas incorretas ou tentativas de quebra travem a aplicação:

### Camada 1: Filtragem em Tempo Real (`validatecommand`)
- **Aba de Conjuntos:** A digitação é monitorada instantaneamente, permitindo apenas números inteiros, espaços, vírgulas e sinal de menos. Qualquer outro caractere alfanumérico ou caractere especial é bloqueado no ato da digitação.
- **Aba de Divisibilidade:** Permite estritamente dígitos decimais de `0` a `9`. Qualquer caractere alfabético, ponto flutuante ou símbolo estranho é rejeitado imediatamente pelo campo.

### Camada 2: Validação Semântica no Acionamento
Mesmo que o usuário cole ou tente submeter campos vazios, zeros ou números negativos:
- O sistema intercepta o erro através de `try/except`.
- Um alerta nativo (`messagebox.showwarning`) é acionado com a mensagem:
  ```text
  Hoje não Cristiane tenta outra coisa.
  ```
- O foco é retornado ao campo com sinalização visual na barra de status, sem fechar a aplicação nem exibir mensagens técnicas do Python.

---

## 4. Recursos e Operações Disponíveis

### Aba 1: Teoria dos Conjuntos
Consome os métodos de `P1/atividade_01_conjuntos/conjuntos.py`:
- **União ($A \cup B$)** e **Interseção ($A \cap B$)**
- **Diferenças** ($A - B$ e $B - A$)
- **Cardinalidades** ($|A|$, $|B|$, $|A \cup B|$, $|A \cap B|$)
- **Conjunto das Partes** ($\mathcal{P}(A)$ e $\mathcal{P}(B)$) e suas cardinalidades ($2^{|A|}$ e $2^{|B|}$)
- **Exemplo de Partição** de $A$ (classificação disjunta)
- **Produto Cartesiano** ($A \times B$)
- **Relações de Inclusão** ($A \subseteq B$ e $B \subseteq A$)

### Aba 2: Divisibilidade, MDC e MMC
Consome os métodos de `P1/atividade_02_divisibilidade/divisibilidade.py`:
- **Divisão Inteira (DIV)** e **Resto da Divisão (MOD)**
- **Expressão Euclidiana:** $a = b \times q + r$
- **Passo a Passo do Algoritmo de Euclides** formatado com alinhamento tabular
- **MDC (Maior Divisor Comum):** Obtido pelas divisões sucessivas
- **MMC (Mínimo Múltiplo Comum):** Calculado a partir da relação teórica $\text{MMC}(a, b) = \frac{a \times b}{\text{MDC}(a, b)}$

---

## 5. Como Executar

Abra o terminal no diretório raiz do projeto e execute:

```powershell
python app_gui.py
```
