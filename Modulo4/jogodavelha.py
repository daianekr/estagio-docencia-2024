import pygame
import numpy as np
import sys

pygame.init()

largura_tela = 600
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da Velha")


branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)

tamanho_celula = largura_tela // 3

tabuleiro = np.array([[' ' for _ in range(3)] for _ in range(3)])


def desenhar_tabuleiro():
    """Desenha o tabuleiro na tela."""
    tela.fill(branco)  
    for i in range(1, 3):
        pygame.draw.line(tela, preto, (0, i * tamanho_celula), (largura_tela, i * tamanho_celula), 3)
        pygame.draw.line(tela, preto, (i * tamanho_celula, 0), (i * tamanho_celula, altura_tela), 3)


def desenhar_peca(x, y, jogador):
    """Desenha X ou O no tabuleiro."""
    centro_x = x * tamanho_celula + tamanho_celula // 2
    centro_y = y * tamanho_celula + tamanho_celula // 2
    raio = tamanho_celula // 4

    if jogador == 'X':
        pygame.draw.line(tela, azul, (centro_x - raio, centro_y - raio), (centro_x + raio, centro_y + raio), 5)
        pygame.draw.line(tela, azul, (centro_x - raio, centro_y + raio), (centro_x + raio, centro_y - raio), 5)
    elif jogador == 'O':
        pygame.draw.circle(tela, azul, (centro_x, centro_y), raio, 5)


def game_over(state):
    """Verifica se o jogo terminou e retorna o vencedor ou empate."""
    for row in range(3):
        if all(state[row] == state[row][0]) and state[row][0] != ' ':
            return state[row][0]

    for col in range(3):
        if all(state[:, col] == state[0][col]) and state[0][col] != ' ':
            return state[0][col]

    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != ' ':
        return state[0][0]

    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != ' ':
        return state[0][2]

    if np.all(state != ' '):
        return 'empate'

    return None


def is_valid_move(board, row, col):
    """Verifica se o movimento é válido."""
    return board[row][col] == ' '


def alternate_player(player):
    """Alterna entre os jogadores."""
    return 'O' if player == 'X' else 'X'


def get_player_move():
    """Captura o movimento do jogador."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // tamanho_celula
                col = x // tamanho_celula
                return row, col


def maquina_joga(tabuleiro):
    """Escolhe a primeira célula disponível para a jogada da máquina."""
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = 'O'
                return  


def play_game():
    """Lógica principal do jogo."""
    global tabuleiro
    player = 'X'
    running = True
    while running:
        desenhar_tabuleiro()


        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] != ' ':
                    desenhar_peca(j, i, tabuleiro[i][j])

        pygame.display.update()

        if player == 'X':
            row, col = get_player_move()
            if is_valid_move(tabuleiro, row, col):
                tabuleiro[row][col] = 'X'
        else:
            maquina_joga(tabuleiro)

        if game_over(tabuleiro):
            running = False

        player = alternate_player(player)

  
    desenhar_tabuleiro()
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] != ' ':
                desenhar_peca(j, i, tabuleiro[i][j])

    pygame.display.update()
    vencedor = game_over(tabuleiro)
    if vencedor == 'empate':
        print("O jogo terminou em empate!")
    else:
        print(f"O jogador {vencedor} venceu!")
    pygame.time.wait(3000)  


play_game()
pygame.quit()
