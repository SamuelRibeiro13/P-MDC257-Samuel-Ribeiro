# Roteiro de Apresentação - Portfólio Parte 2

Perguntas que o professor pode fazer e respostas curtas, baseadas no código entregue.

---

## Atividade 1: [congruencia_tcr.py](atividade_01_congruencia_tcr/congruencia_tcr.py)

**O que significa `a ≡ b (mod n)`?**
Que `n` divide `a - b`, ou seja, `(a - b) % n == 0`. Está em `parte_a`.

**Por que o `%` do Python serve para números negativos?**
Com `n > 0`, o `%` do Python devolve resto entre 0 e `n - 1`, que é a convenção matemática. Exemplo: `-9 % 3 = 0`.

**Como o Algoritmo de Euclides funciona? (`calcular_mdc`)**
Usa `mdc(a, b) = mdc(b, a mod b)`. Repete a divisão até o resto ser 0. O último divisor é o MDC.

**Por que os módulos precisam ser coprimos dois a dois?**
Para que cada `N_i = N / n_i` tenha inverso módulo `n_i` e para a solução ser única módulo `N`. Se `mdc(n_i, n_j) > 1`, o sistema pode não ter solução ou o método não vale. Está em `sao_coprimos_dois_a_dois`.

**O que são `N` e `N_i`?**
`N` é o produto de todos os módulos. `N_i = N / n_i` é o produto de todos os outros módulos, o que o torna coprimo com `n_i`.

**Como achamos o inverso `s_i`? (`inverso_modular_por_busca`)**
Testando `s = 1, 2, ...` até `(N_i × s) % n_i == 1`. Ele existe porque `mdc(N_i, n_i) = 1`. Antes de testar, reduzimos `N_i` módulo `n_i` para os números ficarem menores.

**Por que a soma `a_i · N_i · s_i` resolve o sistema?**
Módulo `n_i`, todos os termos com `j` diferente de `i` somem, porque `N_j` é múltiplo de `n_i`. Sobra `a_i · N_i · s_i ≡ a_i · 1 = a_i`.

**Por que reduzimos módulo `N`?**
Para obter a menor solução não negativa `x0`. As demais são `x0 + t·N`.

**O que acontece com módulo 1?**
Todo inteiro é congruente a 0 módulo 1, então qualquer `s` serve. O código usa `s = 1`.

---

## Atividade 2: [rsa.py](atividade_02_rsa/rsa.py)

**Como o teste de primalidade funciona? (`eh_primo`)**
Se `n` é composto, tem divisor entre 2 e √n. Testamos esses divisores. Se nenhum divide, `n` é primo. O limite é achado com `while (limite+1)*(limite+1) <= n`, sem bibliotecas.

**O que é `φ(n)` e por que `(p-1)(q-1)`?**
É a quantidade de inteiros entre 1 e `n` coprimos com `n`. Para `n = p·q` com `p` e `q` primos distintos, vale `(p-1)(q-1)`.

**Por que `mdc(e, φ(n)) = 1`?**
É a condição para `e` ter inverso módulo `φ(n)`. Sem inverso não existe `d`.

**Como o `d` é calculado? (`euclides_estendido` e `inverso_modular`)**
O Euclides Estendido acha `x` e `y` com `e·x + φ·y = 1`. Então `e·x ≡ 1 (mod φ)`, e `d = x % φ` (o `x` pode ser negativo).

**Como funciona a exponenciação modular rápida? (`exponenciacao_modular`)**
Lê o expoente em binário. Se o bit é 1, multiplica o resultado pela base atual. Depois eleva a base ao quadrado. Tudo é reduzido módulo `n` a cada passo, então os números não explodem.

**Por que a decifragem recupera `M`?**
Como `e·d = 1 + k·φ(n)`, temos `M^(e·d) = M · (M^φ)^k`. Pelo Teorema de Euler, `M^φ ≡ 1`, logo o resultado é `M`. Está na `parte_d`.

**O que diz o Teorema de Euler? Quando se aplica?**
`a^φ(n) ≡ 1 (mod n)` se `mdc(a, n) = 1`. Se a base não for coprima com `n`, o teorema não vale.

**O que diz o Pequeno Teorema de Fermat? Quando se aplica?**
`a^(p-1) ≡ 1 (mod p)` se `p` é primo e `p` não divide `a`.

**Por que não aplicar Fermat ao módulo `n` do RSA?**
Porque `n = p·q` é composto. Fermat exige módulo primo.

**E se `M` não for coprimo com `n`, o RSA falha?**
Não. A exponenciação modular por reduções sucessivas continua válida e a decifragem ainda devolve `M` (teste com `M = 122`, `p = 61`, `q = 53`). O Euler é só uma forma de explicar por que funciona nos casos coprimos.

**O que é a chave pública e a privada?**
Pública `(e, n)`: usada para cifrar. Privada `(d, n)`: usada para decifrar. Quem só conhece `n` precisaria fatorar `n` para obter `φ(n)` e `d`.

---

## Valores para demonstrar ao vivo

| Atividade | Entrada | Resultado esperado |
|---|---|---|
| 1, Parte A | `23, 8, 5` | `23 ≡ 8 (mod 5)` |
| 1, Parte A | `10, 3, 4` | não congruentes |
| 1, Parte B | `2 mod 3`, `3 mod 5`, `2 mod 7` | `x0 = 23`, `N = 105` |
| 1, Parte B | módulos `2, 2, 3, 1` | recusa, `mdc(2, 2) = 2` |
| 2 | `p = 61`, `q = 53`, `e = 17`, `M = 65` | `d = 2753`, `C = 2790`, `M' = 65` |
| 2 | `e = 6` | recusa, `mdc(6, 3120) = 6` |
| 2 | `p = 15` | recusa, `15` não é primo |
| 2 | `M = 122` | Euler não se aplica, decifra `122` |
