# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA - PARTE 2
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 2 - Criptografia RSA
# ==================================================
#
# Este programa constrói uma versão simplificada do RSA, trabalhando
# com números inteiros (e não com textos). Ele executa em sequência:
#   Parte A: primalidade e parâmetros (p, q, n, φ(n), e).
#   Parte B: construção das chaves pública e privada (d).
#   Parte C: cifragem e decifragem de um número inteiro M.
#   Parte D: Teoremas de Euler e de Fermat na exponenciação modular.
#
# Regra da atividade: nenhuma função pronta que resolva o problema
# (math.gcd, pow(a, b, n), pow(a, -1, n), sympy...) é utilizada.
# MDC, teste de primalidade, inverso modular e exponenciação modular
# são implementados aqui, mostrando os passos.

import sys

# Garante a correta exibição de caracteres especiais (φ, ≡, ×, ...)
# no terminal do Windows. Se não for possível, o programa segue normalmente.
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# --------------------------------------------------
# FUNÇÃO DE LEITURA (entrada do usuário com validação)
# --------------------------------------------------

def ler_inteiro(mensagem):
    """
    Lê um número inteiro qualquer (positivo, negativo ou zero).
    Enquanto o usuário digitar algo que não seja inteiro (letras,
    decimais, texto vazio), avisa o erro e pede novamente.
    """
    while True:
        entrada = input(mensagem).strip()  # strip() remove espaços nas pontas
        try:
            return int(entrada)  # int() lança ValueError se não for inteiro
        except ValueError:
            print("   Valor inválido. Digite um número inteiro.\n")


# --------------------------------------------------
# PROCEDIMENTOS MATEMÁTICOS
# --------------------------------------------------

def calcular_mdc(a, b, mostrar=True):
    """
    Algoritmo de Euclides para o MDC (Máximo Divisor Comum).

    Ideia matemática: mdc(a, b) = mdc(b, a mod b). Repetimos a divisão
    até o resto ser zero; o último divisor usado é o MDC.

    Se 'mostrar' for True, imprime cada divisão realizada.
    Retorna o MDC.
    """
    dividendo = max(a, b)  # o maior número vira o dividendo
    divisor = min(a, b)    # o menor número vira o divisor

    while divisor != 0:
        quociente = dividendo // divisor  # divisão inteira
        resto = dividendo % divisor       # resto da divisão
        if mostrar:
            print(f"      {dividendo} = {divisor} × {quociente} + {resto}")
        # Prepara a próxima rodada: divisor vira dividendo e o resto
        # vira o novo divisor.
        dividendo = divisor
        divisor = resto

    # Quando o divisor chega a zero, o dividendo guarda o MDC.
    return dividendo


def eh_primo(n):
    """
    Teste de primalidade por divisões sucessivas (tentativa de divisores).

    Ideia matemática: se n é composto, ele possui um divisor d com
    2 <= d <= √n. Logo, basta testar os divisores de 2 até √n.
    Se nenhum divide n, então n é primo.

    Imprime os divisores testados (quando são poucos) e retorna True/False.
    """
    # Números menores que 2 não são primos (0, 1 e negativos).
    if n < 2:
        print(f"      {n} é menor que 2, logo não é primo.")
        return False

    # Descobre o maior d tal que d × d <= n (equivale a d <= √n),
    # sem usar bibliotecas.
    limite = 1
    while (limite + 1) * (limite + 1) <= n:
        limite = limite + 1

    # Se houver poucos divisores a testar, mostra todos; senão, resume.
    mostrar_todos = limite <= 30
    print(f"      Testando divisores de 2 até {limite} (pois {limite}² <= {n}).")

    for d in range(2, limite + 1):
        resto = n % d  # se o resto for 0, d divide n
        if resto == 0:
            print(f"      {n} mod {d} = 0  => {d} divide {n}, logo {n} NÃO é primo.")
            return False
        if mostrar_todos:
            print(f"      {n} mod {d} = {resto}  (não divide)")

    if not mostrar_todos:
        print(f"      Nenhum divisor entre 2 e {limite} divide {n}.")
    print(f"      Nenhum divisor encontrado, logo {n} é primo.")
    return True


def euclides_estendido(a, b):
    """
    Algoritmo de Euclides Estendido.

    Além do MDC, encontra inteiros x e y tais que:
        a × x + b × y = mdc(a, b)       (Identidade de Bézout)

    Quando mdc(a, b) = 1, o x encontrado é o inverso de a módulo b,
    pois a × x = 1 - b × y, ou seja, a × x ≡ 1 (mod b).

    Mantemos, a cada passo, os "coeficientes" de cada resto:
        resto_i = a × x_i + b × y_i
    Imprime uma tabela com os passos e retorna (mdc, x, y).
    """
    # Valores iniciais: a = a×1 + b×0  e  b = a×0 + b×1.
    r_ant, r_atual = a, b
    x_ant, x_atual = 1, 0
    y_ant, y_atual = 0, 1

    print("      q  |  resto  |   x   |   y")
    print(f"      -  | {r_ant:>6}  | {x_ant:>4}  | {y_ant:>4}")
    print(f"      -  | {r_atual:>6}  | {x_atual:>4}  | {y_atual:>4}")

    while r_atual != 0:
        q = r_ant // r_atual  # quociente da divisão atual
        # Novo resto: r_ant - q × r_atual (equivale a r_ant mod r_atual).
        r_novo = r_ant - q * r_atual
        # Os coeficientes seguem a mesma fórmula do resto.
        x_novo = x_ant - q * x_atual
        y_novo = y_ant - q * y_atual
        # Desloca a janela: o "atual" vira "anterior".
        r_ant, r_atual = r_atual, r_novo
        x_ant, x_atual = x_atual, x_novo
        y_ant, y_atual = y_atual, y_novo
        print(f"    {q:>3}  | {r_atual:>6}  | {x_atual:>4}  | {y_atual:>4}")

    # Ao terminar, r_ant guarda o MDC e (x_ant, y_ant) seus coeficientes.
    return r_ant, x_ant, y_ant


def inverso_modular(valor, modulo):
    """
    Encontra o inverso multiplicativo de 'valor' módulo 'modulo':
    o número s tal que  valor × s ≡ 1 (mod modulo).

    Usa o Euclides Estendido. O inverso só existe se mdc(valor, modulo) = 1.
    O coeficiente x pode sair negativo; por isso usamos x mod modulo para
    trazê-lo ao intervalo de 0 até modulo - 1.
    Retorna o inverso (ou None, se não existir).
    """
    mdc, x, _ = euclides_estendido(valor, modulo)
    if mdc != 1:
        return None  # sem inverso: valor e modulo não são coprimos
    return x % modulo


def para_binario(n):
    """
    Converte n em texto binário (ex.: 13 -> "1101") usando divisões
    sucessivas por 2. Serve para mostrar como a exponenciação rápida
    "lê" o expoente.
    """
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits  # o resto da divisão por 2 é o próximo bit
        n = n // 2
    return bits


def exponenciacao_modular(base, expoente, modulo, mostrar=True):
    """
    Exponenciação modular rápida (quadrados sucessivos).
    Calcula  base ^ expoente  mod  modulo  SEM construir a potência inteira.

    Ideia: escrevemos o expoente em binário. Percorremos os bits do menos
    significativo para o mais significativo:
      - se o bit é 1, multiplicamos o resultado pela base atual;
      - em seguida elevamos a base ao quadrado.
    A cada multiplicação reduzimos módulo 'modulo', então os números
    nunca crescem demais.

    Se 'mostrar' for True, imprime cada etapa relevante.
    """
    if modulo == 1:
        return 0  # todo número é congruente a 0 módulo 1

    resultado = 1
    base_atual = base % modulo  # reduz a base logo no começo
    e = expoente

    if mostrar:
        print(f"      Calculando {base}^{expoente} mod {modulo}")
        print(f"      Expoente {expoente} em binário: {para_binario(expoente)}")
        print(f"      Começo: resultado = 1 e base = {base} mod {modulo} = {base_atual}")

    passo = 0
    while e > 0:
        passo = passo + 1
        bit = e % 2  # bit atual do expoente
        if bit == 1:
            novo = (resultado * base_atual) % modulo
            if mostrar:
                print(f"      passo {passo}: bit 1 -> resultado = "
                      f"{resultado} × {base_atual} mod {modulo} = {novo}")
            resultado = novo
        elif mostrar:
            print(f"      passo {passo}: bit 0 -> resultado continua {resultado}")

        e = e // 2  # descarta o bit que acabou de ser usado
        if e > 0:
            # Eleva a base ao quadrado (só se ainda houver bits a processar).
            nova_base = (base_atual * base_atual) % modulo
            if mostrar:
                print(f"              base = {base_atual}² mod {modulo} = {nova_base}")
            base_atual = nova_base

    if mostrar:
        print(f"      Resultado: {base}^{expoente} ≡ {resultado} (mod {modulo})")
    return resultado


# --------------------------------------------------
# PARTE A - PRIMALIDADE E PARÂMETROS RSA
# --------------------------------------------------

def parte_a():
    """
    Parte A: lê p e q (primos distintos), calcula n = p×q e φ(n),
    e lê o expoente público e com 1 < e < φ(n) e mdc(e, φ(n)) = 1.
    Retorna (p, q, n, phi, e).
    """
    print("\n" + "=" * 46)
    print("PARTE A - PRIMALIDADE E PARÂMETROS RSA")
    print("=" * 46)

    # Repete até obter p e q válidos (maiores que 1, distintos e primos)
    # que também permitam existir um expoente e (φ(n) > 2).
    while True:
        p = ler_inteiro("Digite o primo p: ")
        q = ler_inteiro("Digite o primo q: ")

        # Condição 1: ambos maiores que 1.
        if p <= 1 or q <= 1:
            print("   p e q precisam ser inteiros maiores que 1. Tente novamente.\n")
            continue
        # Condição 2: p e q distintos.
        if p == q:
            print("   p e q precisam ser distintos. Tente novamente.\n")
            continue

        # Condição 3: ambos primos (com o procedimento do aluno).
        print(f"\n   Verificando se p = {p} é primo:")
        p_primo = eh_primo(p)
        print(f"\n   Verificando se q = {q} é primo:")
        q_primo = eh_primo(q)
        if not (p_primo and q_primo):
            print("\n   Pelo menos um dos números não é primo. Digite novos valores.\n")
            continue

        # Com p e q primos distintos, calculamos φ(n) = (p-1)(q-1).
        # Se φ(n) <= 2, não existe e com 1 < e < φ(n).
        if (p - 1) * (q - 1) <= 2:
            print("\n   Com esses primos φ(n) <= 2 e não existe e com 1 < e < φ(n).")
            print("   Escolha primos maiores.\n")
            continue
        break  # tudo válido: sai do laço

    # Cálculo dos parâmetros principais.
    n = p * q
    phi = (p - 1) * (q - 1)
    print("\n" + "-" * 46)
    print("CÁLCULOS")
    print("-" * 46)
    print(f"1. n = p × q = {p} × {q} = {n}")
    print(f"2. φ(n) = (p - 1) × (q - 1) = {p - 1} × {q - 1} = {phi}")
    print("   (fórmula válida para o produto de dois primos distintos)")

    # Leitura do expoente público e: 1 < e < φ(n) e mdc(e, φ(n)) = 1.
    print(f"\n3. Escolha do expoente público e (1 < e < {phi}, mdc(e, {phi}) = 1):")
    while True:
        e = ler_inteiro("   Digite e: ")
        if not (1 < e < phi):
            print(f"   e precisa satisfazer 1 < e < {phi}. Tente novamente.\n")
            continue
        print(f"   Verificando mdc({e}, {phi}) pelo Algoritmo de Euclides:")
        mdc = calcular_mdc(e, phi)
        print(f"      => mdc({e}, {phi}) = {mdc}")
        if mdc != 1:
            print("   e e φ(n) não são coprimos. Digite outro valor.\n")
            continue
        break  # e válido

    print("\nResumo dos parâmetros:")
    print(f"   p = {p}, q = {q}")
    print(f"   n = {n}")
    print(f"   φ(n) = {phi}")
    print(f"   e = {e}")
    return p, q, n, phi, e


# --------------------------------------------------
# PARTE B - CONSTRUÇÃO DAS CHAVES
# --------------------------------------------------

def parte_b(n, phi, e):
    """
    Parte B: encontra o expoente privado d tal que e × d ≡ 1 (mod φ(n)),
    verifica o resultado e apresenta as chaves.
    Retorna d.
    """
    print("\n" + "=" * 46)
    print("PARTE B - CONSTRUÇÃO DAS CHAVES")
    print("=" * 46)

    # O expoente privado d é o inverso de e módulo φ(n).
    print(f"1. Procurando d tal que {e} × d ≡ 1 (mod {phi})")
    print("   Usando o Algoritmo de Euclides Estendido:")
    d = inverso_modular(e, phi)

    if d is None:
        # Segurança: com mdc(e, φ) = 1 verificado na Parte A, isso não ocorre.
        print("   Não existe inverso. Encerrando.")
        return None
    print(f"\n   => d = {d}")

    # Verificação: (e × d) mod φ(n) deve ser 1.
    produto = e * d
    resto = produto % phi
    print(f"\n2. Verificação: e × d = {e} × {d} = {produto}")
    print(f"   {produto} mod {phi} = {resto}")
    if resto == 1:
        print(f"   Como o resto é 1, e × d ≡ 1 (mod {phi}). Verificado.")
    else:
        print("   O resto não é 1. Algo deu errado.")

    print("\n3. Chaves geradas:")
    print(f"   Chave pública : (e, n) = ({e}, {n})")
    print(f"   Chave privada : (d, n) = ({d}, {n})")
    return d


# --------------------------------------------------
# PARTE C - CIFRAGEM E DECIFRAGEM
# --------------------------------------------------

def parte_c(n, e, d):
    """
    Parte C: cifra um inteiro M com a chave pública (C = M^e mod n)
    e decifra com a chave privada (M' = C^d mod n).
    Retorna M.
    """
    print("\n" + "=" * 46)
    print("PARTE C - CIFRAGEM E DECIFRAGEM")
    print("=" * 46)

    # Leitura da mensagem numérica M, com 0 <= M < n.
    while True:
        M = ler_inteiro(f"Digite a mensagem M (0 <= M < {n}): ")
        if 0 <= M < n:
            break
        print(f"   M precisa satisfazer 0 <= M < {n}. Tente novamente.\n")

    # Cifragem com a chave pública (e, n).
    print(f"\n1. Cifragem: C ≡ M^e (mod n) = {M}^{e} mod {n}")
    C = exponenciacao_modular(M, e, n)

    # Decifragem com a chave privada (d, n).
    print(f"\n2. Decifragem: M' ≡ C^d (mod n) = {C}^{d} mod {n}")
    M_decifrado = exponenciacao_modular(C, d, n)

    # Apresentação e verificação final.
    print("\n3. Resultados:")
    print(f"   Número original (M)      = {M}")
    print(f"   Número cifrado (C)       = {C}")
    print(f"   Resultado da decifragem  = {M_decifrado}")

    print("\n4. Conclusão:")
    if M_decifrado == M:
        print(f"   M' = {M_decifrado} é igual a M = {M}. A decifragem recuperou a mensagem original.")
    else:
        print(f"   M' = {M_decifrado} é diferente de M = {M}. A decifragem falhou.")
    return M


# --------------------------------------------------
# PARTE D - TEOREMAS DE EULER E DE FERMAT
# --------------------------------------------------

def parte_d(p, q, n, phi, e, d, M):
    """
    Parte D: demonstra os Teoremas de Euler e de Fermat.

    Teorema de Euler: se mdc(a, n) = 1, então a^φ(n) ≡ 1 (mod n).
    Pequeno Teorema de Fermat: se p é primo e p não divide a,
    então a^(p-1) ≡ 1 (mod p).
    """
    print("\n" + "=" * 46)
    print("PARTE D - TEOREMAS DE EULER E FERMAT")
    print("=" * 46)

    # ---- Teorema de Euler, usando a mensagem M e o módulo n ----
    print(f"1. Teorema de Euler com base M = {M} e módulo n = {n}")
    print(f"   Condição: mdc(M, n) = 1. Verificando mdc({M}, {n}):")
    mdc_Mn = calcular_mdc(M, n)
    print(f"      => mdc({M}, {n}) = {mdc_Mn}")

    if mdc_Mn == 1:
        print(f"   A condição vale. Pelo Teorema de Euler: {M}^{phi} ≡ 1 (mod {n}).")
        print("   Verificando com exponenciação modular:")
        r = exponenciacao_modular(M, phi, n)
        if r == 1:
            print(f"   Confirmado: {M}^{phi} ≡ 1 (mod {n}).")
        else:
            print("   O resultado não foi 1. Algo deu errado.")

        # Redução do expoente: como e × d = 1 + k × φ(n),
        # M^(e×d) = M × (M^φ)^k ≡ M × 1^k ≡ M (mod n).
        # É por isso que decifrar devolve a mensagem original.
        produto = e * d
        k = (produto - 1) // phi
        print(f"\n   Redução do expoente: e × d = {produto} = 1 + {k} × {phi}")
        print(f"   Então M^(e×d) = M^(1 + {k}×{phi}) = M × (M^{phi})^{k}")
        print(f"                 ≡ M × 1^{k} ≡ M (mod {n}).")
        print("   Esta é a razão pela qual a decifragem do RSA funciona.")
    else:
        print(f"   mdc(M, n) = {mdc_Mn} diferente de 1: o Teorema de Euler NÃO se aplica a esta base.")
        print("   Mostrando que a potência não volta a 1:")
        r = exponenciacao_modular(M, phi, n)
        print(f"   {M}^{phi} mod {n} = {r}, que não é 1.")
        print("   Nesse caso usamos a exponenciação modular por reduções")
        print("   sucessivas, que continua válida (foi o que fizemos na Parte C).")

    # ---- Pequeno Teorema de Fermat, com os primos p e q ----
    print("\n2. Pequeno Teorema de Fermat")
    print("   Condição: módulo primo e base não divisível por ele.")
    print("   Usaremos os primos p e q como módulo.")
    base = ler_inteiro("   Digite uma base a (um inteiro positivo): ")
    while base <= 0:
        print("   A base precisa ser positiva.\n")
        base = ler_inteiro("   Digite uma base a (um inteiro positivo): ")

    for primo, nome in ((p, "p"), (q, "q")):
        print(f"\n   Módulo {nome} = {primo} (primo), base a = {base}:")
        if base % primo == 0:
            # Se primo divide a base, a^(p-1) ≡ 0, nunca 1.
            print(f"   {primo} divide {base}: o Teorema de Fermat NÃO se aplica.")
            print(f"   (de fato, {base}^{primo - 1} ≡ 0 mod {primo}, e não 1).")
            continue
        print(f"   {primo} não divide {base} ({base} mod {primo} = {base % primo}). Condição atendida.")
        print(f"   Verificando {base}^{primo - 1} mod {primo}:")
        r = exponenciacao_modular(base, primo - 1, primo)
        if r == 1:
            print(f"   Confirmado: {base}^{primo - 1} ≡ 1 (mod {primo}).")
        else:
            print("   O resultado não foi 1. Algo deu errado.")

    # ---- Condições de aplicação (observação importante do enunciado) ----
    print("\n3. Condições de aplicação:")
    print(f"   - Fermat exige módulo PRIMO. O módulo RSA n = {n} é composto")
    print("     (n = p × q), portanto Fermat NÃO é aplicado diretamente a n.")
    print("   - Euler exige mdc(base, n) = 1. Se não for coprimo, não se aplica.")
    print("   - Quando nenhuma condição vale, a exponenciação modular por")
    print("     reduções sucessivas continua sendo válida.")


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
    print("Atividade 2 - Criptografia RSA")
    print("=" * 46)

    # Repete o programa inteiro até o usuário não querer mais executar.
    while True:
        # Cada parte usa os resultados da anterior.
        p, q, n, phi, e = parte_a()
        d = parte_b(n, phi, e)
        if d is not None:
            M = parte_c(n, e, d)
            parte_d(p, q, n, phi, e, d, M)

        print("\n" + "=" * 46)
        resposta = input("Deseja executar novamente? (s/n): ").strip().lower()
        if resposta != "s":
            break  # qualquer resposta diferente de 's' encerra

    print("\n" + "=" * 46)
    print("FIM DA EXECUÇÃO")
    print("=" * 46 + "\n")


# Só executa main() quando o arquivo é rodado diretamente
# (e não quando é importado por outro arquivo).
if __name__ == "__main__":
    main()
