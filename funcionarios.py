class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario



class Departamento:
    def __init__(self, nome):
         self.nome = nome
         self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        if not self.funcionarios:
            print ("\nNenhum funcionário neste departamento.\n")
        else:
            for f in self.funcionarios:
                print(f" - {f.nome} - R$ {f.salario:.2f}")

    def media_salarial(self):
        soma = 0
        if not self.funcionarios:    
            return 0
        else:
            for f in self.funcionarios:
                soma += f.salario
            return soma/len(self.funcionarios)
   


def main():

    funcionarios = []
    departamentos = []

    while True:
        print("=====MENU=====")
        print("\n1. Cadastrar Funcionário.\n")
        print("\n2. Criar departamento\n")
        print("\n3. Adicionar funcionário ao departamento\n")
        print("\n4. Listar funcionários de um departamento\n")
        print("\n5. Mostrar média salarial do departamento\n")
        print("\n6. Sair\n")

        opcao = input("\nEscolha uma opção. . . ")

        if opcao == "1":
            nome = input("\n- Nome do funcionário: ")
            salario = float(input("\n- Salário: "))
            funcionarios.append(Funcionario(nome,salario))
            print("\nFuncionário cadastrado!\n")


        elif opcao == "2":
            nome = input("\n- Nome do departamento: ")
            departamentos.append(Departamento(nome))
            print("\nDepartamento criado!\n")            


        elif opcao == "3":
            if funcionarios and departamentos:
                print("\n- Funcionários: ")
                for i, f in enumerate(funcionarios):
                    print(f"\n{i + 1}. {f.nome}")
                i_func = int(input("\nEscolha o Nº do funcionário: ")) -1

                print("\n- Departamentos: ")
                for j, d in enumerate(departamentos):
                    print(f"\n{j + 1}. {d.nome}")
                j_dep = int(input("\nEscolha o Nº do Departamento: ")) -1

                departamentos[j_dep].adicionar_funcionario(funcionarios[i_func])
                print("\nFuncionário adicionado ao departamento!\n")

            else:
                print("\nCadastre um funcionário e crie um departamento primeiro.\n")


        elif opcao == "4":
                print("\n-Departamentos: ")
                for j, d in enumerate(departamentos):
                    print(f"\n{j + 1}. {d.nome}")
                j_dep = int(input("\nEscolha o Nº do Departamento: ")) -1

                departamentos[j_dep].listar_funcionarios()


        elif opcao == "5":
                print("\n- Departamentos: ")
                for j, d in enumerate(departamentos):
                    print(f"\n{j + 1}. {d.nome}")
                j_dep = int(input("\nEscolha o Nº do Departamento: ")) -1

                media = departamentos[j_dep].media_salarial()
                print(f"\nMédia salarial do departamento {departamentos[j_dep].nome}: R$ {media:.2f} \n")

        elif opcao == "6":
            print("\nEncerrando programa. . .\n")
            break

        else:
            print("\nOpção inválida. Digite um número válido (1-6) .\n")

if __name__ == "__main__":
    main()