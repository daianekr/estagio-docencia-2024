---
marp: true
theme: beam
---

<!-- _class: title -->

# Resolução de Problemas por meio de Busca


<br><br><br><br><br>

## Prof. Sérgio Nery Simões
### IFES - Campus Serra

<br>

Boa noite!

Começaremos em alguns minutos...

---

# Algoritmos de Busca - Objetivo do Módulo
  <br>

  - Compreender os **fundamentos de busca** em Inteligência Artificial.
  - Explorar **algoritmos de busca não informada** (cega), como Busca em Largura (BFS) e Busca em Profundidade (DFS).
  - Estudar **algoritmos de busca informada** (heurística), como a Busca Gulosa e o Algoritmo A*.
  - **Aplicar** esses algoritmos em problemas práticos para melhor entendimento. 
  
---

## **O que são Algoritmos de Busca?**

<br>

- **Algoritmos de busca** são técnicas utilizadas em IA para encontrar soluções em um espaço de **estados**, que representa todos os possíveis estados de um problema. Por meio de **ações**, é possivel encontrar um estado que satisfaça uma condição de solução. 
<br>
- Existem dois tipos principais de busca: a **busca não-informada**, que não utiliza nenhuma informação adicional além da estrutura do problema (como BFS e DFS), e **busca informada**, que emprega heurísticas para guiar a busca de maneira mais eficiente, como nos algoritmos A* e Busca Gulosa. Esses algoritmos são fundamentais para resolver problemas como planejamento, jogos, e navegação.

---

## **Espaço de Estados**:
<br>

  - Um **espaço de estados** é a representação de todos os estados possíveis de um problema e das transições que podem ocorrer entre esses estados.

  - No problema do labirinto, cada posição no labirinto é um 
  **estado**, e cada movimento (para cima, para baixo, para a esquerda, para a direita) representa uma **transição entre estados**.

 ![width:200px, bg right](labirinto.avif "Jogo do Labirinto")

---

 ## **Problemas de Busca**:
 <br>

  - Em IA, **problemas de busca** envolvem a navegação por um espaço de estados para encontrar um caminho do estado inicial até o estado objetivo.
  <br>
  - **Elementos principais de um problema de busca**:
    - **Estado Inicial**: Ponto de partida da busca.
    - **Ações**: Movimentos ou decisões possíveis em cada estado.
    - **Estado Objetivo**: Estado que queremos alcançar.
    - **Custo do Caminho**: Soma dos custos das ações para chegar ao estado objetivo.
---

# **Mapa da Romenia**

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

![w:800 h:500 bg](arad.png "Jogo do Labirinto")

---
<br>

# **Problema de Busca - Chegar em Bucharest**

<br>

  - **Estado Inicial**: Ponto de partida da busca: Em(Arad).
  - **Ações**: Movimentos ou decisões possíveis em cada estado: Ir(Cidade, PróximaCidade).
  - **Estado Objetivo**: Estado que queremos alcançar: Em(Bucharest)
  - **Custo do Caminho**: Custo numérico de cada caminho: Distância em KM entre as cidades.
  - **Espaço de Estados**: Conjunto de estados que podem ser atingidos a partir do
estado inicial: Mapa da Romênia

---
<br>

## **Qual Estado inicial, Ações, Estado objetivo, Custo e Espaço de Estados?**

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

![w:700 h:500 bg](labirinto2.png "Jogo do Labirinto")

---

### **Busca Não Informada (Cega)**

 A **busca não informada** é uma técnica onde o algoritmo explora o espaço de estados sem informações adicionais sobre a proximidade do objetivo. Não utiliza nenhuma **heurística** para guiar a busca.

**Características**:
  - **Completude**: A busca é completa se for garantido que ela encontrará uma solução se existir uma.
  - **Complexidade de Tempo e Espaço**: Refere-se à quantidade de memória e tempo necessários.
  - **Otimalidade**: A busca é ótima se encontrar a solução com o menor custo.

**Aplicações**:
  - Usada quando não há informações sobre o espaço de estados ou heurísticas confiáveis.
--- 
- **Sugestão de Figura**: Diagrama mostrando um labirinto com estados sendo visitados de maneira aleatória, sem seguir uma direção específica em relação ao objetivo.

---

### **Algoritmo de Busca em Largura (BFS)**

 O Algoritmo de **Busca em Largura (BFS)** explora todos os nós em um nível antes de avançar para o próximo nível. Ele é usado para encontrar o caminho mais curto em termos de número de passos.

**Exemplo de pseudocódigo:**

- **Passos do Algoritmo**:
  1. Colocar o **estado inicial** na fila.
  2. Repetir até a fila estar vazia:
     - Remover o primeiro estado da fila e verificar se é o objetivo.
     - Se não for o objetivo, adicionar todos os estados filhos à fila.
---

  ### **Vantagens e Desvantagens BFS**:

  - **Vantagens**: Completo (se há solução, ele encontra) e ótimo (encontra a solução com menos passos).
  - **Desvantagens**: Requer muita memória e tempo para espaços de estados grandes.
     
- **Exemplo**:
  - Encontrar o caminho mais curto em um labirinto.
---
- **Sugestão de Figura**: Diagrama de uma árvore onde o BFS expande todos os nós de um nível antes de passar ao próximo.
---
**Exemplo de Pseudocódigo**:
  ```plaintext
  BFS(Estado_Inicial):
      Fila = [Estado_Inicial]
      Enquanto Fila não estiver vazia:
          Nó_Atual = Fila.desenfileirar()
          Se Nó_Atual for o Objetivo:
              Retornar Caminho
          Para cada Nó_Filho de Nó_Atual:
              Fila.enfileirar(Nó_Filho)
  ```

---

### **Algoritmo de Busca em Profundidade (DFS)**
  A **Busca em Profundidade (DFS)** explora o caminho completo em direção a um estado folha antes de retornar e explorar caminhos alternativos.Utiliza uma **pilha** para armazenar estados não explorados.

**Exemplo de pseudocódigo:**

- **Passos do Algoritmo**:
  1. Colocar o **estado inicial** na pilha.
  2. Repetir até a pilha estar vazia:
     - Remover o estado do topo da pilha e verificar se é o objetivo.
     - Se não for o objetivo, adicionar os estados filhos ao topo da pilha.
---
 ### **Vantagens e Desvantagens DFS** :

  - **Vantagens**: Menor uso de memória em comparação com BFS.
  - **Desvantagens**: Não é ótimo (não encontra o caminho mais curto) e pode entrar em ciclos infinitos. 
  
- **Exemplo**:
  - Exploração de uma rede de pastas e arquivos.
---
- **Sugestão de Figura**: Diagrama de uma árvore onde o DFS explora completamente um caminho antes de retroceder e explorar o próximo.
---
- **Pseudocódigo**:
  ```plaintext
  DFS(Estado_Inicial):
      Pilha = [Estado_Inicial]
      Enquanto Pilha não estiver vazia:
          Nó_Atual = Pilha.desempilhar()
          Se Nó_Atual for o Objetivo:
              Retornar Caminho
          Para cada Nó_Filho de Nó_Atual:
              Pilha.empilhar(Nó_Filho)
  ```

---

### **Comparação entre BFS e DFS**
- **Tabela Comparativa**:
  - **Completude**:
    - BFS: Completo (se uma solução existe, será encontrada).
    - DFS: Incompleto em grafos infinitos ou com ciclos.
  - **Otimalidade**:
    - BFS: Ótimo (encontra o menor caminho em termos de passos).
    - DFS: Não é ótimo.
---
  - **Complexidade de Tempo**:
    - BFS: $O(b^d)$, onde $b$ é o fator de ramificação e \(d\) a profundidade da solução.
    - DFS: $O(b^m)$, onde $m$ é a profundidade máxima do espaço de busca.
  - **Complexidade de Espaço**:
    - BFS: $O(b^d)$, elevado para espaços grandes.
    - DFS: $O(b \cdot m)$, menor consumo de memória.
  
- **Quando Utilizar**:
  - **BFS** é indicado para problemas onde o objetivo é encontrar o menor número de passos.
  - **DFS** é mais apropriado para problemas onde o espaço de memória é limitado ou a profundidade máxima é conhecida.
---
  - **Sugestão de Figura**: Tabela comparativa e um gráfico que ilustra a expansão da busca BFS em comparação com a DFS.


---

### **Algoritmo A*** 

O **algoritmo A*** (ou **A-Star**) é um dos algoritmos mais eficientes e amplamente usados para encontrar o caminho mais curto em grafos. Ele é uma técnica de busca informada, ou seja, utiliza conhecimento adicional sobre o problema (por meio de uma heurística) para tomar decisões mais inteligentes durante a busca. 

---

#### **Como funciona o A***?

O algoritmo combina as ideias de:
- **Busca em largura (BFS)**: que explora os nós em níveis, garantindo a descoberta do caminho mais curto em grafos não ponderados.
- **Busca em profundidade (DFS)**: que busca um caminho até a meta explorando o máximo possível os ramos antes de retroceder.
  
A principal inovação do A* está na função de avaliação usada para priorizar os nós a serem explorados:
$$
f(n) = g(n) + h(n)
$$
Onde:
- $ f(n) $: custo total estimado para chegar ao objetivo a partir do nó $ n $; 
- $ g(n) $: custo real acumulado para chegar ao nó $ n $ a partir do início.
- $ h(n) $: estimativa heurística do custo para ir do nó $n$ até o objetivo.

Se a heurística $ h(n) $ for **admissível** (ou seja, nunca superestima o custo real para chegar ao objetivo), o A* garante encontrar o caminho mais curto.

---

### **Relação com os algoritmos BFS e DFS?**

1. **Busca em largura (BFS)**:
   - Explora todos os caminhos de custo igual antes de avançar para caminhos de custo maior.
   - Sem heurística: equivalente a A* com $ h(n) = 0 $.
   - Muito eficiente para grafos não ponderados, mas não considera o custo futuro.

2. **Busca em profundidade (DFS)**:
   - Explora um caminho até o final antes de retroceder.
   - Pode ser mais rápido para encontrar um caminho, mas não necessariamente o mais curto.
   - Diferentemente do A*, não utiliza heurísticas e pode explorar áreas irrelevantes.

3. **A***:
   - Adiciona inteligência à exploração, combinando o custo acumulado $ g(n) $ com uma previsão informada $ h(n) $.
   - Equilibra a força bruta do BFS com a orientação do DFS.

---

### **Exemplo: planejamento de rotas**

Imagine que você está projetando um sistema GPS para calcular a rota mais curta entre duas cidades. O mapa pode ser representado como um grafo onde:
- Os **nós** representam cidades.
- As **arestas** têm pesos que indicam a distância entre cidades.

#### **Passo a Passo com A***:
1. Defina a cidade de partida A e a cidade de destino G.
2. Use a distância percorrida $ g(n) $ para calcular o custo até o nó atual.
3. Use a distância "em linha reta" até o destino $ h(n) $ como heurística.
4. Calcule $ f(n) = g(n) + h(n) $ para cada nó adjacente.
5. Escolha o nó com menor valor de $ f(n)$ e continue o processo.

---

#### **Comparação com BFS e DFS no Exemplo**:
- **DFS** pode escolher um caminho muito longo sem perceber que há atalhos.
- **BFS** consideraria todas as rotas possíveis em ordem crescente de custo, gastando tempo explorando nós desnecessários.
- **A***, ao usar a heurística, evitaria nós irrelevantes, indo mais rapidamente ao destino.

---

### **Aplicação Método Manhattan no Algoritmo A\***

Considere a seguinte imagem: 

 ![width:200px, bg right](manhattan_distance.png)

Uma abordagem comum para calcular a heurística $ h(n) $ no algoritmo A\* é chamada de **método Manhattan**. Esse método calcula o número total de movimentos necessários, somando as distâncias horizontais e verticais entre o nó atual e o nó objetivo, ignorando movimentos diagonais e quaisquer obstáculos no caminho.

A fórmula para o cálculo da heurística é:

$$
h = |x_{\text{inicial}} - x_{\text{destino}}| + |y_{\text{inicial}} - y_{\text{destino}}|
$$

Onde:
- $ x_{\text{inicial}} $ e $ y_{\text{inicial}} $: coordenadas do ponto inicial.
- $ x_{\text{destino}} $ e $ y_{\text{destino}} $: coordenadas do ponto objetivo.

Essa heurística é exata sempre que o caminho segue linhas retas, ou seja, quando o A\* encontra caminhos que são combinações de movimentos horizontais e verticais. No entanto, em algumas situações, pode ser preferível usar uma heurística que favoreça movimentos mais diretamente alinhados ao destino.

### **Referência**

O exemplo foi adaptado do artigo "[A-Star Search Algorithm](https://brilliant.org/wiki/a-star-search/)" no site Brilliant.org.

### **Exemplo de Aplicação**

Imagine um tabuleiro de jogo onde o objetivo é mover-se de uma posição inicial para uma posição final sem passar por obstáculos. O método Manhattan calcularia o custo baseado no número de células necessárias para alcançar o destino, ignorando diagonais.

---



# Lista de Exercicios Módulo 2 - Algoritmos de Busca


## Exercício 1: Definição de Espaço de Estados
**Pergunta**: Defina o que é um **espaço de estados** e forneça um exemplo prático de como ele pode ser representado para um problema de navegação em um labirinto.

**Objetivo**: Verificar se os alunos compreendem o conceito de espaço de estados e como ele pode ser aplicado a problemas práticos.

---

## Exercício 2: Busca em Largura (BFS)
**Pergunta**: Dado o grafo abaixo, simule passo a passo a execução do algoritmo **BFS** começando do nó A e indique a ordem em que os nós serão visitados.

<!-- melhorar a visualização do grafo abaixo  -->
::: mermaid
graph TD
    A --> B
    A --> C
    B --> D
    B --> E
    C --> F

:::




**Objetivo**: Testar a compreensão da lógica de busca em largura e a sua aplicação em grafos.

---

## Exercício 3: Busca em Profundidade (DFS)
**Pergunta**: Usando o mesmo grafo do exercício anterior, aplique o algoritmo **DFS** a partir do nó A. Indique a ordem em que os nós são visitados.

**Objetivo**: Avaliar a habilidade de aplicar busca em profundidade e entender como o algoritmo explora os nós.

---

## Exercício 4: Busca A*
**Pergunta**: Considere o problema de navegação em um mapa, onde cada nó representa uma cidade e as arestas representam a distância entre elas. A seguir estão as distâncias reais e heurísticas estimadas (distância em linha reta até o destino).

| Cidade  | Distância Real (km) | Heurística (km até o objetivo) |
|---------|---------------------|-------------------------------|
| A -> B  | 2                   | 6                             |
| B -> C  | 2                   | 4                             |
| C -> D  | 3                   | 0 (Objetivo)                   |
| A -> E  | 5                   | 7                             |
| E -> D  | 4                   | 0 (Objetivo)                   |

Aplique o algoritmo **A*** para encontrar o caminho mais curto de A até D e mostre passo a passo a ordem de expansão dos nós.

**Objetivo**: Verificar o entendimento sobre busca informada e o uso de heurísticas no A*.

---

## Exercício 5: Heurísticas
**Pergunta**: Para o problema do 8-puzzle (quebra-cabeça deslizante), descreva duas funções heurísticas possíveis para ajudar a resolver o problema. Qual delas você acha que levaria a uma solução mais eficiente?

**Objetivo**: Avaliar a compreensão sobre o conceito de heurística e a capacidade de pensar em funções heurísticas úteis.
