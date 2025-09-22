
# CLASSE BASE

class Personagem:
    def __init__(self, nome, nivel):
        self._nome = nome
        self._nivel = nivel

    def atacar(self):
        print(f"{self._nome} (nível {self._nivel}) dá um ataque básico.")

# SUB-CLASSE GUERREIRO

class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.__forca = forca

    def atacar(self):
        print(f"{self._nome} (nível {self._nivel}) faz uma investida com sua espada. (Força: {self.__forca})")
        

# SUB-CLASSE MAGO

class Mago(Personagem):
    def __init__(self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.__mana = mana

    def atacar(self):
        print(f"{self._nome} (nível {self._nivel}) conjura uma bola de fogo. (Mana: {self.__mana})")


def main():
    
# PERSONAGENS

    soldado = Personagem("Ragnar", 7)

    guerreiro = Guerreiro("Krastos", 8, forca=78)
    
    mago = Mago("Vilkran", 10, mana=96)

    personagens = [soldado, guerreiro, mago]

# ATAQUES

    print("=== Ações dos personagens ===")
    for p in personagens:
        p.atacar()

if __name__ == "__main__":
    main()