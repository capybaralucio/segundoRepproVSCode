class Participante:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email
    
    def emitirCertificado(self):
        return f"\nCertificado genérico para o aluno {self._nome}.\n"


class Aluno(Participante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.__curso = curso

    def get_curso(self):
        return self.__curso
    
    def emitirCertificado(self):
        return f"\nCertificado de conclusão do aluno {self._nome} do curso {self.__curso} com sucesso.\n"


class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.__especialidade = especialidade

    def get_especialidade(self):
        return self.__especialidade
    
    def emitirCertificado(self):
        return f"\nCertificado de participação do instrutor {self.get_nome()} como palestrante do curso {self.__especialidade}.\n"
    

def main():

    participantes = []    
    
    while True:
        print("\n=== PLATAFORMA DO CURSINHO ===\n")
        print("1. Efetuar Cadastro")
        print("2. Listar Participantes do Cursinho")
        print("3. Emitir Certificado")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")


        if opcao == "1":
            print("\nCadastrar: ")
            print("\n1. = Aluno ")
            print("\n2. = Instrutor ")
            tipo = input("\nEscolha o tipo de participante a ser cadastrado: ")

            if tipo == "1":
                nome = input("\nNome: ")
                email = input("\nE-MAIL: ")
                curso = input("\nCurso: ")
                participantes.append(Aluno(nome, email, curso))
                print("\nAluno cadastrado com sucesso!\n")

            elif tipo == "2":
                nome = input("\nNome: ")
                email = input("\nE-MAIL: ")
                especialidade = input("\nEspecialidade: ")
                participantes.append(Instrutor(nome, email, especialidade))
                print("\nInstrutor cadastrado com sucesso!\n")
            else:
                print("\nOpção Inválida! Digite um número de 1 - 4 \n") 


        elif opcao == "2":
            if not participantes:
                print("\nNenhum participante cadastrado.\n")
            else:
                print("\n--- Participantes Cadastrados ---\n")
                for p in participantes:
                    if isinstance(p, Aluno):
                        print(f"Tipo: Aluno")
                        print(f"Nome: {p._nome}")
                        print(f"E-MAIL: {p._email}")
                        print(f"Curso: {p.get.__curso()}\n")
                    else:
                        print(f"Tipo: Instrutor")
                        print(f"Nome: {p._nome}")
                        print(f"E-MAIL: {p._email}")
                        print(f"Especialidade: {p.get_especialidade()}\n")


        elif opcao == "3":
            if not participantes:
                print("\nNenhum participante cadastrado.\n")
            else:
                print("\n=== Certificados ===\n")
                for p in participantes:
                    print(p.emitirCertificados())
        

        elif opcao == "4":
            print("\nEncerrando Programa. . .\n")
            break 

        else:
            print("\nOpção Inválida! Digite um número de 1 - 4 \n") 

if __name__ == "__main__":
    main()