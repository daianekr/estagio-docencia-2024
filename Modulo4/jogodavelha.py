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

tabuleiro = np.array([[' ' for _ in range(3)] for _ in range(3)])

tamanho_celula = largura_tela // 3

def criar_tabuleiro():
  return np.array([[' ' for _ in range(3)] for _ in range(3)])

def imprimir_tabuleiro(tabuleiro):
  for linha in tabuleiro:
    print('|', end='')
    for celula in linha:
      print(f" {celula} |", end='')
    print('\n')
    print('-' * 11)

def desenhar_linha(y):
  pygame.draw.line(tela, preto, (0, y), (largura_tela, y), 2)

def desenhar_coluna(x):
  pygame.draw.line(tela, preto, (x, 0), (x, altura_tela), 2)

def desenhar_peca(x, y, jogador):
  centro_x = x * tamanho_celula + tamanho_celula // 2
  centro_y = y * tamanho_celula + tamanho_celula // 2
  raio = tamanho_celula // 4

  if jogador == 'X':
    pygame.draw.line(tela, branco, (centro_x - raio, centro_y - raio), (centro_x + raio, centro_y + raio), 2)
    pygame.draw.line(tela, branco, (centro_x - raio, centro_y + raio), (centro_x + raio, centro_y - raio), 2)
  else:
    pygame.draw.circle(tela, branco, (centro_x, centro_y), raio, 2)

def game_over(state):
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
    return board[row][col] == ' '

def alternate_player(player):
    return 'O' if player == 'X' else 'X'

def score(state):
    if game_over(state) == 'O':
        return 10
    elif game_over(state) == 'X':
        return -10
    else:
        return 0

def minimax(state, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or game_over(state):
        return score(state)

    if maximizingPlayer:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'O'
                    eval = minimax(state, depth - 1, alpha, beta, False)
                    state[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'X'
                    eval = minimax(state, depth - 1, alpha, beta, True)
                    state[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(state):
    best_val = -float("inf")
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                state[i][j] = 'O'
                move_val = minimax(state, 0, -float("inf"), float("inf"), False)
                state[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

def get_player_move():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x, y = pygame.mouse.get_pos()
                row = y // tamanho_celula
                col = x // tamanho_celula 

                if is_valid_move(tabuleiro, row, col):
                    return row, col

def play_game():
    board = np.array([[' ' for _ in range(3)] for _ in range(3)])
    player = 'X'  
    while not game_over(board):
        imprimir_tabuleiro(board)
        pygame.display.update()
        if player == 'X':
            row, col = get_player_move()
            if is_valid_move(board, row, col):
                board[row][col] = 'X'
        else:
            row, col = best_move(board)
            board[row][col] = 'O'

        player = alternate_player(player)


    winner = game_over(board)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    play_game()

pygame.quit()
           

