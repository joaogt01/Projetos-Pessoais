import random


def menu():
    print('''
YU-GI-OH! TERMINAL DUEL
1 - Configurar Duelo
2 - iniciar Duelo
0 - Sair''')
cartas = [{'id': 'M1', 'tipo': 'monstro', 'atk' : 2000, 'def' : 1500},
          {'id': 'M2', 'tipo': 'monstro', 'atk' : 1500, 'def' : 2000},
          {'id': 'M3', 'tipo': 'monstro', 'atk' : 1800, 'def' : 1200},
          {'id': 'M4', 'tipo': 'monstro', 'atk' : 1700, 'def' : 1500},
          {'id': 'M5', 'tipo': 'monstro', 'atk' : 3500, 'def' : 500},
          {'id': 'M6', 'tipo': 'monstro', 'atk' : 2000, 'def' : 1800},
          {'id': 'S1', 'tipo': 'magia', 'efeito': '500 defesa'},
          {'id': 'S2', 'tipo': 'magia', 'efeito': 'destruir carta inimiga'},
          {'id': 'S3', 'tipo': 'magia', 'efeito': 'recuperar 500 hp'},
          {'id': 'S4', 'tipo': 'magia', 'efeito': '500 dano'},
          {'id': 'S5', 'tipo': 'magia', 'efeito': '500 dano'},
          {'id': 'S6', 'tipo': 'magia', 'efeito': '500 dano'}]
deck1 = [random.sample(cartas, k=6)]
deck2 = [random.sample(cartas, k=6)]
jogador1 = []
jogador2 = []
print(deck1)
laco_jogo = True
while laco_jogo == True:
    menu()
    opcao_menu = int(input())
    if opcao_menu == 0:
        laco_jogo = False
    elif opcao_menu == 1:
        nick1 = input("Digite o nome do Jogador 1: ")
        nick2 = input("Digite o nome do Jogador 2: ")
        player1 = {
            'nick': nick1,
            'hp': 4000,
            'mao': deck1
        }
        player2 = {
            'nick': nick2,
            'hp': 4000,
            'mao': deck2
        }
        jogador1 = player1
        jogador2 = player2
    elif opcao_menu == 2:
        turno = random.choice([jogador1, jogador2])
        outro = jogador2 if turno == jogador1 else jogador1
        print(f'{turno['nick']} começa o duelo')
        while jogador1['hp'] > 0 and jogador2['hp'] > 0:
            print(f"é a vez de {turno['nick']}")
            print(f"{jogador1['nick']} HP: {jogador1['hp']} | {jogador2['nick']} HP: {jogador2['hp']}")
            print("1 - Atacar\n2 - Passar turno")
            escolha = input("Escolha: ")
            if escolha == 1:
                print(deck1)
                print(deck2)

