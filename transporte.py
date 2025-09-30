
from abc import ABC, abstractmethod

class VeiculoTransporte(ABC):
    def __init__(self, placa, capacidade_passageiros):
        self.placa = placa
        self.capacidade_passageiros = capacidade_passageiros

    @abstractmethod
    def calcularCustoOperacional(self):
        pass


class Onibus(VeiculoTransporte):
    def __init__(self, placa, capacidade_passageiros, consumo_Km):
    super().__init__(placa, capacidade_passageiros)
    self.consumo_Km = consumoPorKm

    def calcularCustoOperacional(self):
        return self.consumo_Km * 6.0


class Metro(VeiculoTransporte):
    def __init__ (self, placa, capacidade_passageiros, consumo_energia_Km):
        super().__init__(placa, capacidade_passageiros)
        self.consumoEnergiaPorKm = consumoEnergiaPorKm

    def calcularCustoOperacional(self):
        return self.consumo_energia_Km * 0.8


def main():

    veiculos = []

    while True:
        print("\n====MENU====")
        print("1. Cadastrar Ônibus")
        print("2. Cadastrar Metrô")
        print("3. Mostrar custos operacionais")
        print("4. Sair")

        opcao = input("\nDigite uma opção: ") 

        if opcao == "1":
            print("\nCadastro de Ônibus")

            try: 
                placa = input("\nPlaca: ").strip()

                if placa == "":
                    raise ValueError("A placa não pode estar vazia.")
                
                capacidade = int(input("\nCapacidade de passageiros: "))

                if capacidade <= 0:
                    raise ValueError("A capacidade deve ser positiva.")
                
                consumo = float(input("\nConsumo por km (litros/km): "))

                if consumo <= 0: 
                    raise ValueError("O consumo deve ser positivo.")
                
                veiculos.append(Onibus(placa, capacidade, consumo))

                print("\nÔnibus cadastrado com sucesso!\n")
            
            except ValueError as e:
                print(f"\nErro: {e}")             

        elif opcao == "2":

            print("\nCadastro de Metrô")

            try:
                placa = input("\nIdentificação: ").strip()

                if placa == "":
                    raise ValueError("A identificação não pode estar vazia.")
                
                capacidade = int(input("\nCapacidade de passageiros: "))

                if capacidade <= 0:
                    raise ValueError("A capacidade deve ser positiva.")
                
                consumo = float(input("\nConsumo de energia por km (kWh/km): "))

                if consumo <= 0: 
                    raise ValueError("O consumo deve ser positivo.")
                
                veiculos.append(Metro(placa, capacidade, consumo))

                print("\nMetrô cadastrado com sucesso!\n")

            except ValueError as e:
                print(f"\nErro: {e}")
        

        elif opcao == "3":
            if not veiculos:
                print("\nNenhum veículo cadastrado.\n")
            else:
                print("\n--- Custos operacionais por Km ---\n")

                for v in veiculos:
                    tipo = "Ônibus" if isinstance(v, Onibus) else "Metrô"
                    custo = v.calcularCustoOperacional()
                    print(f"\n- {tipo} - {v.placa}: R$ {custo:.2f} por Km.")

        elif opcao == "4":
            print("Encerrando o Sistema. . .")
            break
        
        else:
            print("\nOpção inválida! Tente novamente.")
    

if __name__ == "__main__":
    main()