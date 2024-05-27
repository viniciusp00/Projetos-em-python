def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."


if __name__ == "__main__":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print(f"Soma: {adicao(num1, num2)}")
    print(f"Subtração: {subtracao(num1, num2)}")
    print(f"Multiplicação: {multiplicacao(num1, num2)}")
    print(f"Divisão: {divisao(num1, num2)}")