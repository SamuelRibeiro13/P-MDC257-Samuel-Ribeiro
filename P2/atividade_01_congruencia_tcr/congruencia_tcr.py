# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA - PARTE 2
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 1 - Congruência Modular e Teorema Chinês do Resto
# ==================================================
#
# Este programa possui duas partes, escolhidas por um menu:
#   Parte A: verifica se a ≡ b (mod n).
#   Parte B: resolve um sistema de 3 ou 4 congruências lineares
#            usando o Teorema Chinês do Resto (TCR).
#
# Regra da atividade: nenhuma função pronta que resolva o problema
# (como math.gcd) é utilizada. O MDC e o inverso multiplicativo
# são implementados aqui, passo a passo.

import sys

# Garante a correta exibição de caracteres especiais (≡, ×, ...)
# no terminal do Windows. Se não for possível, o programa segue normalmente.
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# --------------------------------------------------
# FUNÇÕES DE LEITURA (entrada do usuário com validação)
# --------------------------------------------------

def ler_inteiro(mensagem):
    """
    Lê um número inteiro qualquer (positivo, negativo ou zero).
    Enquanto o usuário digitar algo que não seja inteiro (letras,
    número decimal, texto vazio), avisa o erro e pede novamente.
    """
    while True:
        entrada = input(mensagem).strip()  # strip() remove espaços nas pontas
        try:
            return int(entrada)  # int() lança ValueError se não for inteiro
        except ValueError:
            print("   Valor inválido. Digite um número inteiro.\n")


def ler_inteiro_positivo(mensagem):
    """
    Lê um número inteiro estritamente positivo (> 0).
    Usado para os módulos, pois um módulo precisa ser maior que zero.
    """
    while True:
        valor = ler_inteiro(mensagem)  # reaproveita a validação de inteiro
        if valor > 0:
            return valor
        print("   O valor precisa ser maior que zero.\n")


# --------------------------------------------------
# PROCEDIMENTOS MATEMÁTICOS
# --------------------------------------------------

def calcular_mdc(a, b):
    """
    Algoritmo de Euclides para o MDC (Máximo Divisor Comum).

    Ideia matemática: mdc(a, b) = mdc(b, a mod b). Repetimos a divisão
    até o resto ser zero; o último divisor usado é o MDC.

    Retorna: (mdc, passos), onde cada passo é uma tupla
    (dividendo, divisor, quociente, resto), para podermos imprimir
    o raciocínio depois.
    """
    passos = []
    dividendo = max(a, b)  # o maior número vira o dividendo
    divisor = min(a, b)    # o menor número vira o divisor

    while divisor != 0:
        quociente = dividendo // divisor  # divisão inteira
        resto = dividendo % divisor       # resto da divisão
        passos.append((dividendo, divisor, quociente, resto))
        # Prepara a próxima rodada: o divisor vira dividendo,
        # e o resto vira o novo divisor.
        dividendo = divisor
        divisor = resto

    # Quando o divisor chega a zero, o dividendo guarda o MDC.
    return dividendo, passos


def sao_coprimos_dois_a_dois(modulos):
    """
    Verifica se TODOS os pares de módulos são coprimos, ou seja,
    se mdc(n_i, n_j) = 1 para todo i diferente de j.

    Essa é a condição necessária do Teorema Chinês do Resto.
    Imprime o cálculo de cada par e retorna True/False.
    """
    todos_coprimos = True  # começa assumindo que está tudo certo

    # Dois laços aninhados percorrem cada par (i, j) uma única vez (i < j).
    for i in range(len(modulos)):
        for j in range(i + 1, len(modulos)):
            mdc, passos = calcular_mdc(modulos[i], modulos[j])

            # Monta o texto com as divisões do Algoritmo de Euclides.
            texto_passos = "; ".join(
                f"{d} = {s} × {q} + {r}" for (d, s, q, r) in passos
            )
            print(f"   mdc({modulos[i]}, {modulos[j]}): {texto_passos}")
            print(f"      => mdc({modulos[i]}, {modulos[j]}) = {mdc}")

            if mdc != 1:
                todos_coprimos = False  # achou um par que NÃO é coprimo

    return todos_coprimos


def inverso_modular_por_busca(valor, modulo):
    """
    Encontra o inverso multiplicativo de 'valor' módulo 'modulo',
    isto é, o número s tal que:  valor × s ≡ 1 (mod modulo).

    Procedimento (busca simples): testa s = 1, 2, 3, ..., modulo - 1
    e para no primeiro s em que (valor × s) mod modulo seja igual a 1.

    O inverso existe quando mdc(valor, modulo) = 1, condição que já foi
    garantida pelos módulos serem coprimos dois a dois.
    Retorna o inverso s (ou None, se não existir).
    """
    # Caso especial: módulo 1. Todo inteiro é congruente a 0 módulo 1,
    # então qualquer s serve. Usamos s = 1 por convenção.
    if modulo == 1:
        print("      Módulo 1: qualquer s serve (tudo é congruente módulo 1). Usando s = 1.")
        return 1

    # Trabalhamos com o resto de 'valor' para os números ficarem menores.
    # Isso não muda o resultado, pois valor ≡ (valor mod modulo) (mod modulo).
    resto_valor = valor % modulo
    print(f"      Procurando s com {valor} × s ≡ 1 (mod {modulo}),"
          f" lembrando que {valor} ≡ {resto_valor} (mod {modulo}).")

    # Para módulos muito grandes, imprimir toda tentativa seria enorme.
    mostrar_tentativas = modulo <= 30

    for s in range(1, modulo):
        resultado = (resto_valor * s) % modulo
        if mostrar_tentativas:
            print(f"        s = {s}: {resto_valor} × {s} mod {modulo} = {resultado}")
        if resultado == 1:
            if not mostrar_tentativas:
                print(f"        (módulo grande: tentativas intermediárias omitidas)")
                print(f"        s = {s}: {resto_valor} × {s} mod {modulo} = {resultado}")
            return s  # achamos o inverso, pode parar a busca

    return None  # nenhum s funcionou: não existe inverso


# --------------------------------------------------
# PARTE A - VERIFICAÇÃO DE CONGRUÊNCIA MODULAR
# --------------------------------------------------

def parte_a():
    """
    Parte A: dados a, b e n (n > 0), verifica se a ≡ b (mod n).

    Definição: a ≡ b (mod n) se, e somente se, n divide (a - b),
    isto é, se o resto de (a - b) por n é zero.
    """
    print("\n" + "=" * 46)
    print("PARTE A - VERIFICAÇÃO DE CONGRUÊNCIA MODULAR")
    print("=" * 46)

    # Passo 1: leitura dos dados. O módulo n precisa ser positivo.
    a = ler_inteiro("Digite o valor de a: ")
    b = ler_inteiro("Digite o valor de b: ")
    n = ler_inteiro_positivo("Digite o valor do módulo n (n > 0): ")

    print("\n" + "-" * 46)
    print("CÁLCULOS")
    print("-" * 46)

    # Passo 2: diferença entre a e b.
    diferenca = a - b
    print(f"1. Diferença: a - b = {a} - ({b}) = {diferenca}")

    # Passo 3: resto da divisão da diferença por n.
    # Em Python, quando n > 0 o resto (%) nunca é negativo, o que é
    # exatamente a convenção matemática que queremos (0 <= resto < n).
    quociente = diferenca // n
    resto = diferenca % n
    print(f"2. Divisão por n: {diferenca} = {n} × ({quociente}) + {resto}")
    print(f"   Resto de ({diferenca}) por {n} = {resto}")

    # Passo 4: o resto é zero?
    print(f"3. O resto é zero? {'Sim' if resto == 0 else 'Não'}")

    # Passo 5: conclusão justificada.
    print("4. Conclusão:")
    if resto == 0:
        print(f"   Como {n} divide ({diferenca}) (resto 0),")
        print(f"   concluímos que {a} ≡ {b} (mod {n}).")
    else:
        print(f"   Como {n} NÃO divide ({diferenca}) (resto {resto}),")
        print(f"   concluímos que {a} NÃO é congruente a {b} (mod {n}).")


# --------------------------------------------------
# PARTE B - TEOREMA CHINÊS DO RESTO
# --------------------------------------------------

def parte_b():
    """
    Parte B: resolve o sistema
        x ≡ a_1 (mod n_1)
        x ≡ a_2 (mod n_2)
        ...
    com 3 ou 4 congruências, módulos positivos e coprimos dois a dois.

    Resumo do método (Teorema Chinês do Resto):
      1. N   = n_1 × n_2 × ... × n_k
      2. N_i = N / n_i
      3. s_i = inverso de N_i módulo n_i  (N_i × s_i ≡ 1 mod n_i)
      4. x0  = (a_1·N_1·s_1 + ... + a_k·N_k·s_k) mod N
      5. Solução geral: x = x0 + t·N, com t inteiro.
    """
    print("\n" + "=" * 46)
    print("PARTE B - TEOREMA CHINÊS DO RESTO")
    print("=" * 46)

    # Passo 1: o usuário escolhe 3 ou 4 congruências.
    quantidade = 0
    while quantidade not in (3, 4):
        quantidade = ler_inteiro("Quantas congruências (3 ou 4)? ")
        if quantidade not in (3, 4):
            print("   Escolha apenas 3 ou 4.\n")

    # Listas que guardam os restos (a_i) e os módulos (n_i) de cada equação.
    restos = []
    modulos = []
    for i in range(quantidade):
        print(f"\nEquação {i + 1}:  x ≡ a{i + 1} (mod n{i + 1})")
        restos.append(ler_inteiro(f"   a{i + 1} = "))
        modulos.append(ler_inteiro_positivo(f"   n{i + 1} = "))

    # Mostra o sistema digitado, para o usuário conferir.
    print("\nSistema informado:")
    for i in range(quantidade):
        print(f"   x ≡ {restos[i]} (mod {modulos[i]})")

    # Passo 2: os módulos já são positivos (a leitura garante isso).
    # Falta verificar se são coprimos dois a dois.
    print("\n" + "-" * 46)
    print("VERIFICAÇÃO DOS MÓDULOS (coprimos dois a dois)")
    print("-" * 46)
    if not sao_coprimos_dois_a_dois(modulos):
        print("\nResultado: os módulos NÃO são coprimos dois a dois.")
        print("O sistema está fora das condições previstas para esta atividade.")
        return  # encerra a Parte B sem tentar resolver
    print("\nTodos os pares são coprimos. O TCR pode ser aplicado.")

    # Passo 3: N = produto de todos os módulos.
    print("\n" + "-" * 46)
    print("CÁLCULOS DO TEOREMA CHINÊS DO RESTO")
    print("-" * 46)
    N = 1
    for modulo in modulos:
        N = N * modulo  # multiplica acumulando o produto
    texto_produto = " × ".join(str(m) for m in modulos)
    print(f"1. N = {texto_produto} = {N}")

    # Passo 4: para cada equação, N_i = N / n_i.
    # Usamos // porque a divisão é exata (n_i divide N).
    print("\n2. Cálculo de N_i = N / n_i:")
    valores_N = []
    for i in range(quantidade):
        Ni = N // modulos[i]
        valores_N.append(Ni)
        print(f"   N{i + 1} = {N} / {modulos[i]} = {Ni}")

    # Passo 5: inverso multiplicativo s_i de cada N_i módulo n_i.
    print("\n3. Inverso multiplicativo s_i (N_i × s_i ≡ 1 mod n_i):")
    inversos = []
    for i in range(quantidade):
        print(f"   Equação {i + 1}: N{i + 1} = {valores_N[i]}, n{i + 1} = {modulos[i]}")
        s = inverso_modular_por_busca(valores_N[i], modulos[i])
        if s is None:
            # Segurança: com módulos coprimos isso não deve ocorrer.
            print("      Não foi encontrado inverso. Encerrando.")
            return
        inversos.append(s)
        print(f"      => s{i + 1} = {s}")

    # Passo 6: soma dos termos a_i × N_i × s_i e redução módulo N.
    print("\n4. Soma dos termos a_i × N_i × s_i:")
    soma = 0
    for i in range(quantidade):
        termo = restos[i] * valores_N[i] * inversos[i]
        soma = soma + termo
        print(f"   termo {i + 1} = {restos[i]} × {valores_N[i]} × {inversos[i]} = {termo}")
    print(f"   Soma = {soma}")

    # Reduz a soma módulo N para obter a menor solução não negativa x0.
    x0 = soma % N
    print(f"\n5. Solução particular: x0 = {soma} mod {N} = {x0}")

    # Passo 7: solução geral e exemplos de valores de t.
    print(f"\n6. Solução geral: x = {x0} + t × {N}, com t ∈ ℤ")
    for t in (-1, 0, 1):
        print(f"   t = {t:>2}: x = {x0 + t * N}")

    # Verificação: x0 precisa satisfazer TODAS as congruências.
    print("\n7. Verificação de x0 em cada congruência:")
    tudo_certo = True
    for i in range(quantidade):
        resto_x0 = x0 % modulos[i]        # resto de x0 por n_i
        resto_esperado = restos[i] % modulos[i]  # a_i reduzido módulo n_i
        ok = resto_x0 == resto_esperado
        if not ok:
            tudo_certo = False
        print(f"   {x0} mod {modulos[i]} = {resto_x0} | "
              f"{restos[i]} mod {modulos[i]} = {resto_esperado} "
              f"=> {'OK' if ok else 'ERRO'}")

    print("\nConclusão:")
    if tudo_certo:
        print(f"   x0 = {x0} satisfaz todas as congruências do sistema.")
        print(f"   Todas as soluções são x = {x0} + t × {N}, t ∈ ℤ.")
    else:
        print("   Algo deu errado: x0 não satisfaz todas as congruências.")


# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------

def main():
    # Dados de identificação do aluno
    nome = "Samuel Ribeiro"
    matricula = "2612130058"
    turno = "Matutino"

    # Impressão do cabeçalho da atividade
    print("\n" + "=" * 46)
    print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA - PARTE 2")
    print("=" * 46)
    print("Aluno:", nome)
    print("Matrícula:", matricula)
    print("Disciplina: Estruturas Matemáticas para Computação")
    print("Turno:", turno)
    print("Atividade 1 - Congruência Modular e TCR")
    print("=" * 46)

    # Menu: repete até o usuário escolher sair (opção 0).
    while True:
        print("\nMENU")
        print("  1 - Parte A: Verificar congruência modular")
        print("  2 - Parte B: Teorema Chinês do Resto")
        print("  0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            parte_a()
        elif opcao == "2":
            parte_b()
        elif opcao == "0":
            break  # sai do laço e encerra o programa
        else:
            print("   Opção inválida. Escolha 1, 2 ou 0.")

    print("\n" + "=" * 46)
    print("FIM DA EXECUÇÃO")
    print("=" * 46 + "\n")


# Só executa main() quando o arquivo é rodado diretamente
# (e não quando é importado por outro arquivo).
if __name__ == "__main__":
    main()
