# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 1 - Teoria dos Conjuntos
# ==================================================

import sys

# Garante a correta exibição de caracteres especiais no terminal do Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def ler_conjunto(nome_conjunto):
    """
    Lê os elementos de um conjunto digitados pelo usuário.
    Garante que sejam inteiros e não quebrem o programa.
    """
    while True:
        entrada = input(f"Digite os elementos do conjunto {nome_conjunto} (separados por espaço): ").strip()
        if not entrada:
            print("Hoje não Cristiane tenta outra coisa.\n")
            continue
        
        try:
            tokens = entrada.replace(",", " ").split()
            if not tokens:
                print("Hoje não Cristiane tenta outra coisa.\n")
                continue
            
            # Converte para inteiros e elimina elementos repetidos mantendo a ordem
            elementos = []
            for t in tokens:
                num = int(t)
                if num not in elementos:
                    elementos.append(num)
            
            return elementos
        except ValueError:
            print("Hoje não Cristiane tenta outra coisa.\n")


def conjunto_partes(conjunto):
    """
    Gera o conjunto das partes (todos os subconjuntos possíveis).
    Começa com o conjunto vazio e vai expandindo a cada elemento.
    """
    partes = [[]]
    for elem in conjunto:
        novos = []
        for sub in partes:
            novos.append(sub + [elem])
        partes.extend(novos)
    return partes


def formatar_conjunto(lista):
    """Auxiliar para exibir listas com formatação matemática de conjunto: {1, 2, 3}"""
    if not lista:
        return "∅"
    return "{" + ", ".join(str(x) for x in lista) + "}"


def formatar_partes(lista_partes):
    """Formata a lista de subconjuntos como conjunto das partes."""
    subconjuntos_str = [formatar_conjunto(sub) for sub in lista_partes]
    return "{" + ", ".join(subconjuntos_str) + "}"


def processar_conjuntos(A, B):
    """
    Executa todas as operações entre os conjuntos A e B
    e retorna um dicionário estruturado com os resultados.
    """
    uniao = list(A)
    for x in B:
        if x not in uniao:
            uniao.append(x)

    intersecao = [x for x in A if x in B]
    dif_A_B = [x for x in A if x not in B]
    dif_B_A = [x for x in B if x not in A]

    partes_A = conjunto_partes(A)
    partes_B = conjunto_partes(B)

    # Exemplo de partição de A
    particao = []
    if A:
        pares = [x for x in A if x % 2 == 0]
        impares = [x for x in A if x % 2 != 0]
        if pares and impares:
            particao = [pares, impares]
        elif len(A) >= 2:
            meio = len(A) // 2
            particao = [A[:meio], A[meio:]]
        else:
            particao = [A]

    # Produto cartesiano
    prod_cartesiano = [(a, b) for a in A for b in B]

    # Inclusão
    a_em_b = all(x in B for x in A)
    b_em_a = all(x in A for x in B)

    return {
        "A": A,
        "B": B,
        "uniao": uniao,
        "intersecao": intersecao,
        "dif_A_B": dif_A_B,
        "dif_B_A": dif_B_A,
        "card_A": len(A),
        "card_B": len(B),
        "card_uniao": len(uniao),
        "card_intersecao": len(intersecao),
        "partes_A": partes_A,
        "partes_B": partes_B,
        "card_partes_A": len(partes_A),
        "card_partes_B": len(partes_B),
        "particao_A": particao,
        "prod_cartesiano": prod_cartesiano,
        "A_sub_B": a_em_b,
        "B_sub_A": b_em_a,
    }


def main():
    # Dados de identificação do aluno
    nome = "Samuel Ribeiro"
    matricula = "2612130058"
    turno = "Matutino"

    # Impressão do cabeçalho da atividade
    print("\n" + "=" * 46)
    print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
    print("=" * 46)
    print("Aluno:", nome)
    print("Matrícula:", matricula)
    print("Disciplina: Estruturas Matemáticas para Computação")
    print("Turno:", turno)
    print("Atividade 1 - Teoria dos Conjuntos")
    print("=" * 46 + "\n")

    # Entrada dos conjuntos A e B
    A = ler_conjunto("A")
    B = ler_conjunto("B")

    print("\n" + "=" * 46)
    print("CONJUNTOS INFORMADOS")
    print("=" * 46)
    print("A =", formatar_conjunto(A))
    print("B =", formatar_conjunto(B))

    print("\n" + "-" * 46)
    print("OPERAÇÕES COM CONJUNTOS")
    print("-" * 46)

    # 1. União (A U B)
    uniao = list(A)
    for x in B:
        if x not in uniao:
            uniao.append(x)
    print("1. União (A ∪ B):", formatar_conjunto(uniao))

    # 2. Interseção (A ∩ B)
    intersecao = []
    for x in A:
        if x in B:
            intersecao.append(x)
    print("2. Interseção (A ∩ B):", formatar_conjunto(intersecao))

    # 3. Diferenças (A - B e B - A)
    dif_A_B = []
    for x in A:
        if x not in B:
            dif_A_B.append(x)
    print("3. Diferença (A - B):", formatar_conjunto(dif_A_B))

    dif_B_A = []
    for x in B:
        if x not in A:
            dif_B_A.append(x)
    print("   Diferença (B - A):", formatar_conjunto(dif_B_A))

    # 4. Cardinalidades
    print("\n4. Cardinalidades:")
    print(f"   |A| = {len(A)}")
    print(f"   |B| = {len(B)}")
    print(f"   |A ∪ B| = {len(uniao)}")
    print(f"   |A ∩ B| = {len(intersecao)}")

    # 5. Conjunto das Partes de A e B
    partes_A = conjunto_partes(A)
    partes_B = conjunto_partes(B)

    print("\n5. Conjunto das Partes:")
    print("   P(A) =", formatar_partes(partes_A))
    print("   P(B) =", formatar_partes(partes_B))

    # 6. Cardinalidade do Conjunto das Partes
    print("\n6. Cardinalidade das Partes:")
    print(f"   |P(A)| = {len(partes_A)} (ou seja, 2^{len(A)})")
    print(f"   |P(B)| = {len(partes_B)} (ou seja, 2^{len(B)})")

    # 7. Exemplo de partição de um dos conjuntos (Conjunto A)
    print("\n7. Exemplo de Partição de A:")
    if not A:
        print("   O conjunto A é vazio, portanto não possui partição.")
    else:
        # Partição por paridade (pares e ímpares)
        pares = [x for x in A if x % 2 == 0]
        impares = [x for x in A if x % 2 != 0]

        if pares and impares:
            print("   Partição em pares e ímpares:")
            print(f"   A1 = {formatar_conjunto(pares)}, A2 = {formatar_conjunto(impares)}")
            print(f"   P = {{{formatar_conjunto(pares)}, {formatar_conjunto(impares)}}}")
        elif len(A) >= 2:
            # Caso todos sejam pares ou todos sejam ímpares, divide em dois blocos disjuntos
            meio = len(A) // 2
            bloco1 = A[:meio]
            bloco2 = A[meio:]
            print("   Partição em dois subconjuntos disjuntos:")
            print(f"   A1 = {formatar_conjunto(bloco1)}, A2 = {formatar_conjunto(bloco2)}")
            print(f"   P = {{{formatar_conjunto(bloco1)}, {formatar_conjunto(bloco2)}}}")
        else:
            print("   Como A tem apenas 1 elemento, a única partição possível é ele mesmo:")
            print(f"   P = {{{formatar_conjunto(A)}}}")

    # 8. Produto Cartesiano (A x B)
    prod_cartesiano = []
    for a in A:
        for b in B:
            prod_cartesiano.append((a, b))
    
    prod_str = ", ".join(f"({a}, {b})" for a, b in prod_cartesiano)
    print(f"\n8. Produto Cartesiano (A × B): {{{prod_str}}}")
    print(f"   Total de pares: {len(prod_cartesiano)} (|A| × |B| = {len(A)} × {len(B)})")

    # 9. Verificação de Inclusão (A ⊆ B e B ⊆ A)
    print("\n9. Relações de Inclusão:")
    # A está contido em B?
    a_em_b = True
    for x in A:
        if x not in B:
            a_em_b = False
            break

    if a_em_b:
        print("   A ⊆ B: Sim, todos os elementos de A pertencem a B.")
    else:
        print("   A ⊆ B: Não, existem elementos de A que não pertencem a B.")

    # B está contido em A?
    b_em_a = True
    for x in B:
        if x not in A:
            b_em_a = False
            break

    if b_em_a:
        print("   B ⊆ A: Sim, todos os elementos de B pertencem a A.")
    else:
        print("   B ⊆ A: Não, existem elementos de B que não pertencem a A.")

    print("\n" + "=" * 46)
    print("FIM DA EXECUÇÃO")
    print("=" * 46 + "\n")


if __name__ == "__main__":
    main()
