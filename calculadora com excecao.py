class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            raise ZeroDivisionError("\nNão é possível dividir por zero.")
        return a / b


class Interface:
    def __init__(self):
        self.calc = Calculadora()

    def menu(self):
        while True:
            print("\n===  CALCULADORA-SIMPLES ===\n")
            print("1. SOMA")
            print("2. SUBTRAÇÃO")
            print("3. MULTIPLICAÇÃO")
            print("4. DIVISÃO")
            print("5. SAIR")

            opcao = input("\nEscolha uma opção de calculo: ").strip()

            if opcao == "5":
                print("\nEncerrando Calculadora. . .")  
                break

            if opcao not in {"1", "2", "3", "4", "5"}:
                print("\nOpção Inválida! Digite um número de 1 - 4\n")
                continue

            try:
                a = float(input("\nDigite o primeiro valor: "))
                b = float(input("\nDigite o segundo valor: "))

                if opcao == "1":
                    resultado = self.calc.soma(a,b)

                if opcao == "2":
                    resultado = self.calc.subtracao(a,b)

                if opcao == "3":
                    resultado = self.calc.multiplicacao(a,b)

                if opcao == "4":
                    resultado = self.calc.divisao(a,b)

                print(f"\nResultado: {resultado}\n")
            
            except ValueError:
                print("\nERRO! Por favor, digite um número válido.")
            except ZeroDivisionError as e:
                print(f"\nERRO! {e}")


if __name__ == "__main__":
    interface = Interface()
    interface.menu()