---
marp: true
theme: beam
css: beam.css
---

<!-- _class: title -->

# **Algoritmos de Otimização**

<br><br><br><br><br>

## Prof. Sérgio Nery Simões
### IFES - Campus Serra

<br>

Boa noite!

Começaremos em alguns minutos...

---

# **Busca Adversarial - Objetivo do Módulo**

  - Introduzir o conceito de **busca em cenários competitivos**.
  - Explorar o **algoritmo Minimax** (cega), como Busca em Largura (BFS) e Busca em Profundidade (DFS).
  - Estudar **Heurísticas e Profundidade Limitada**.
  - Entender o que é a **Poda Alfa-Beta**, 
  - **Aplicar** esses algoritmos em problemas contexto de jogos. 
  
---

# **O que é busca adversarial?**

Busca adversarial é uma técnica usada em inteligência artificial para resolver problemas onde há competição entre dois ou mais agentes, com objetivos que confiltam entre si. Exemplos clássicos incluem jogos como xadrez, damas e Jogo da Velha.
<br>
Diferente de uma busca tradicional (como encontrar o menor caminho em um grafo), aqui os agentes têm interesses opostos.
Um agente busca maximizar sua pontuação, enquanto o outro busca minimizá-la. Este conceito é denominado de busca competitiva. 


---

# **Teoria de Jogos**

A teoria de jogos se baseia no estudo de ambientes multiagentes, em cenários que podem ser tanto competitivos como colaborativos. 
<br>
Imagine dois jogadores jogando damas. Cada movimento que você faz não apenas afeta o tabuleiro, mas também as opções do oponente. Seu objetivo é tomar decisões que dificultem a vitória do adversário.

---

# **Teoria de Jogos**

Outro conceito importante é o conceito de **Soma Zero**, em jogos está relacionado ao fato de que se em um jogo uma pessoa ganha, automaticamente, outra pessoa precisa perder. 

Mais teoricamente falando: soma zero é aquele que o **valor utilidade** ao final do
jogo para os dois jogadores é igual e de sinal oposto.
<br>
Valor utilidade é a pontuação final do agente.

---

# **Teoria de Jogos**

Em IA, estudamos esses jogos, por serem determininísticos, de jogacdas alternadas, com dois jogadeores ou equipes, de **soma zero** e **informação perfeita.**

Exemplos: 

- **Pedra, papel e tesoura:** com dois agentes temos as seguintes possibilidades de resultado:

$$
\renewcommand{\arraystretch}{1.5} 
\begin{array}{c|c}
\text{\textsf{\textbf{Jogador 1}}} & \text{\textsf{\textbf{Jogador 2}}} \\ \hline
\textsf{1} & \textsf{-1} \\
\textsf{0} & \textsf{0} \\
\textsf{-1} & \textsf{1} \\
\end{array}
$$


<!-- | Jogador 1 | Jogador 2 |
    |-----------|-----------|
    |     1     |     -1    |
    |     0     |     0     |
    |     -1    |     1     | -->



---
# **Características de Problemas Adversariais** 

### Ambiente de jogo:
**Determinístico:** Não há elementos de sorte. As ações produzem resultados previsíveis (ex.: xadrez, jogo da Velha).
**Turnos alternados:** Os jogadores se revezam nas jogadas.
**Informação perfeita:** Ambos os jogadores têm acesso completo ao estado atual do jogo.
### Requisitos para um problema ser adversarial:
- Dois ou mais agentes (jogadores).
- Objetivos conflitantes: um ganha e o outro perde.
- Estados de jogo e ações bem definidos.