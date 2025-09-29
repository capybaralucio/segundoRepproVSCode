class Personagem:
    def __init__(self, nome, constelacao):
        self.nome = nome
        self.constelacao = constelacao

    def apresentar(self):
        print(f"\n- {self.nome}, cavaleiro da constelação de {self.constelacao}.")

        
class CavaleiroDeBronze(Personagem):
    def __init__(self, nome, constelacao, poder_de_luta):
        super().__init__(nome, constelacao)
        self.poder_de_luta = poder_de_luta

    def golpe_especial(self):
        print(f"\n- {self.nome} executou um golpe especial com o poder de luta {self.poder_de_luta} !")
    

class CavaleiroDeOuro(Personagem):
    def __init__(self, nome, constelacao, casa_do_zodiaco):
        super().__init__(nome, constelacao)
        self.casa_do_zodiaco = casa_do_zodiaco

    def defender_casa(self):
        print(f"- {self.nome} defende a casa de {self.casa_do_zodiaco}.")


class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro):
    def __init__(self, nome, constelacao, poder_de_luta, casa_do_zodiaco):
        CavaleiroDeOuro.__init__(self, nome, constelacao, casa_do_zodiaco)
        self.poder_de_luta = poder_de_luta

    def golpe_especial(self):
        print(f"\n- {self.nome} realiza um golpe híbrido com poder de luta {self.poder_de_luta} !")

    def defender_casa(self):
        print(f"\n- {self.nome} protege a casa de {self.casa_do_zodiaco}.")

def main():
    
    personagens = []

    while True:
        print("\n=== ! CAVALEIROS DO ZODÍACO ! ===\n")
        print("1. Cadastrar Cavaleiro")
        print("2. Listar todos os Cavaleiros")
        print("3. Executar Habilidades")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
                
                print("\nTipo de cavaleiro: ")
                print("\n1. Cavaleiro de Bronze: ")
                print("\n2. Cavaleiro de Ouro: ")
                print("\n3. Cavaleiro Híbrido: ")

                tipo = input("\nTipo: ")
                if tipo == "1":
                    nome = input("\nNome do Cavaleiro: ")
                    constelacao = input("Constelação pertencente: ")
                    poder = input("Poder de luta: ")
                    personagem = CavaleiroDeBronze(nome, constelacao, poder)

                elif tipo == "2":
                    nome = input("\nNome do Cavaleiro: ")
                    constelacao = input("Constelação pertencente: ")
                    casa = input("Casa do Zodiaco: ")
                    personagem = CavaleiroDeOuro(nome, constelacao, casa)
                    
                elif tipo == "3":
                    nome = input("\nNome do Cavaleiro: ")
                    constelacao = input("Constelação pertencente: ")
                    poder = input("Poder de luta: ")
                    casa = input("Casa do Zodiaco: ")
                    personagem = CavaleiroHibrido(nome, constelacao, poder, casa)

                else:
                    print("\nTipo inválido.\n")
                    continue

                personagens.append(personagem)
                print("\nCavaleiro cadastrado com sucesso !\n")


        elif opcao == "2":

            if not personagens:
                print("\nNenhum Cavaleiro cadastrado.\n")

            else:
                print("\n--- CAVALEIROS CADASTRADOS ---\n")
                for p in personagens:
                    p.apresentar()
        

        elif opcao == "3":

            if not personagens:
                print("\nNenhum Cavaleiro cadastrado.\n")

            else:
                print("\n--- HABILIDADES ---\n")
                for p in personagens:
                    print(f"\n- {p.nome}: ")
                    if isinstance(p, CavaleiroDeBronze):
                        p.golpe_especial()
                    
                    if isinstance(p, CavaleiroDeOuro):
                        p.defender_casa()
                        

        elif opcao == "4":

            print("\nEncerrando Cavaleiro dos Zodíaco. . .\n")
            break 

        else:
        
            print("\nOpção Inválida! Digite um número de 1 - 4 \n") 


if __name__ == "__main__":
    main()