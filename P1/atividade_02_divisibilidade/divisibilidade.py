# ==================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA
# Disciplina: Estruturas Matemáticas para Computação
# Atividade 2 - Divisibilidade, MDC e MMC
# ==================================================

import sys

# Garante a correta exibição de caracteres especiais no terminal do Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def ler_inteiro_positivo(mensagem):
    """
    Lê um número inteiro positivo (> 0).
    Se o usuário tentar digitar letras, números negativos, zero ou quebrar o input,
    exibe uma mensagem de aviso e solicita novamente.
    """
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if valor <= 0:
                print("Hoje não Cristiane tenta outra coisa.\n")
                continue
            return valor
        except ValueError:
            print("Hoje não Cristiane tenta outra coisa.\n")


def calcular_mdc_euclides_com_passos(a, b):
    """
    Executa o Algoritmo de Euclides para encontrar o MDC,
    armazenando cada passo no formato: dividendo = divisor × quociente + resto.
    """
    passos = []
    dividendo = max(a, b)
    divisor = min(a, b)

    while divisor != 0:
        quociente = dividendo // divisor
        resto = dividendo % divisor
        passos.append((dividendo, divisor, quociente, resto))
        dividendo = divisor
        divisor = resto

    mdc = dividendo
    return mdc, passos


def processar_divisibilidade(a, b):
    """
    Executa os cálculos de divisibilidade, algoritmo de Euclides, MDC e MMC
    e retorna um dicionário estruturado com os resultados.
    """
    div_resultado = a // b
    mod_resultado = a % b
    mdc, passos = calcular_mdc_euclides_com_passos(a, b)
    mmc = (a * b) // mdc
    return {
        "a": a,
        "b": b,
        "div": div_resultado,
        "mod": mod_resultado,
        "passos": passos,
        "mdc": mdc,
        "mmc": mmc,
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
    print("Atividade 2 - Divisibilidade, MDC e MMC")
    print("=" * 46 + "\n")

    # Solicitação dos dois números inteiros positivos
    num1 = ler_inteiro_positivo("Digite o primeiro número: ")
    num2 = ler_inteiro_positivo("Digite o segundo número: ")

    print("\n" + "=" * 46)
    print("RESULTADOS E PROCEDIMENTOS")
    print("=" * 46)

    # 1 e 2: Divisão Inteira (DIV) e Resto (MOD)
    print("1. Divisão Inteira (DIV):")
    div_resultado = num1 // num2
    print(f"   {num1} // {num2} = {div_resultado}")

    print("\n2. Resto da Divisão (MOD):")
    mod_resultado = num1 % num2
    print(f"   {num1} % {num2} = {mod_resultado}")
    print(f"   Expressão: {num1} = {num2} × {div_resultado} + {mod_resultado}")

    # 3 e 4: Passo a passo do Algoritmo de Euclides e MDC
    print("\n3. Passo a Passo do Algoritmo de Euclides:")
    mdc, passos = calcular_mdc_euclides_com_passos(num1, num2)
    for p in passos:
        d_endo, d_sor, q, r = p
        print(f"   {d_endo} = {d_sor} × {q} + {r}")

    print("\n4. MDC (Maior Divisor Comum):")
    print(f"   MDC({num1}, {num2}) = {mdc}")

    # 5: MMC utilizando a relação estudada em aula: MMC(a, b) = (a * b) / MDC(a, b)
    print("\n5. MMC (Mínimo Múltiplo Comum):")
    print("   Procedimento utilizado: MMC(a, b) = (a × b) // MDC(a, b)")
    mmc = (num1 * num2) // mdc
    print(f"   MMC({num1}, {num2}) = ({num1} × {num2}) // {mdc} = {mmc}")

    print("\n" + "=" * 46)
    print("FIM DA EXECUÇÃO")
    print("=" * 46 + "\n")


if __name__ == "__main__":
    main()
