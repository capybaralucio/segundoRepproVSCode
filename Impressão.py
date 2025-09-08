class Documento:
    def __init__ (self, titulo, conteudo):
        self.__titulo = titulo
        self.__conteudo = conteudo

    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_conteudo(self, conteudo):
        self.__conteudo = conteudo


class Impressora:
    def imprimir(self, documento):
        print("\n====Impressão do Documento====\n")
        print(f" - Título: {documento.get_titulo()}")
        print(f" - Conteúdo: {documento.get_conteudo()}")
        print("----------------------------------------")


def main():
    documentos = []
    impressora = Impressora()

    while True:
        print ("\n---IMPRESSORA FODONA---\n")
        print ("\n1. Criar novo documento\n")
        print ("\n2. Listar documento\n")
        print ("\n3. Imprimir documento\n")
        print ("\n3. Sair \n")

        opcao = input("\nEscolha uma opção. . .\n")
        if opcao == "1":
            titulo = input("\nDigite o título do documento:\n")
            conteudo = input("Digite o conteúdo do documento:")
            doc = Documento(titulo,conteudo)
            documentos.append(doc)
            print("\nDocumento criado com sucesso!\n")

        elif opcao == "2":
            if not documentos:
                print("\nNenhum documento criado ainda.\n")
            else:
                print("\n---Lista de Documentos---\n")
                for i, doc in enumerate(documentos):
                    print(f"\n{i + 1}, {doc.get_titulo()}\n")

        elif opcao == "3":
            if not documentos:
                print("\nNenhum documento disponível para impressão.\n")
            else:
                print("\nEscolha o Número do documento a ser impresso. . .\n")
                for i, doc in enumerate(documentos):
                    print(f"\n{i + 1}, {doc.get_titulo()}\n")

                escolha = input("Nº")
                if escolha.isdigit():
                    escolha = int(escolha)
                    if 1 <= escolha <= len(documentos):
                        impressora.imprimir(documentos[escolha -1])
                    else:
                        print("\nNúmero Inválido.\n")
                else:
                    print("\nEntrada Inválida. Digite um número. . .\n")

        elif opcao == "4":
            print("\nEncerrando Impressora. . .")
            break

        else:
            print("Opção inválida! Coloque um número válido.")

if __name__ == "__main__":
    main()
