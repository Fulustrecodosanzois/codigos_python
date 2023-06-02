from rpg import Personagem, Jogador

pers= Personagem("Fulustreco", 1)
jog= Jogador("Fulustreco", 3, "Bárbaro")

pers.atacar()
pers.life()

jog.usar_habilidade("Descer a porrada")
