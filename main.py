from pymaze import maze,agent,COLOR
from collections import deque
from random import randint


def Teste_objetivo(celula_atual, fim):
    if celula_atual != fim:
        return False
    else:
        return True

def Teste_sucessor(m,celula_atual, i):
    celulaFilha = celula_atual
    if m.maze_map[celula_atual][i] == True:
        if i == 'E':
            celulaFilha = (celula_atual[0], celula_atual[1] + 1)
        elif i == 'W':
            celulaFilha = (celula_atual[0], celula_atual[1] - 1)
        elif i == 'S':
            celulaFilha = (celula_atual[0] + 1, celula_atual[1])
        elif i == 'N':
            celulaFilha = (celula_atual[0] - 1, celula_atual[1])
    return celulaFilha

def BFS(m, start=None):
    if start is None:
        start=(m.rows,m.cols)
    vizinha = deque()
    vizinha.append(start)
    bfsRota = {}
    visitada = [start]
    bSearch=[]

    while len(vizinha)>0:
        currCell=vizinha.popleft()
        if Teste_objetivo(currCell, m._goal)==True:
            break
        for d in 'ESNW':
            filha = Teste_sucessor(m, currCell, d)
            if filha in visitada:
                continue
            vizinha.append(filha)
            visitada.append(filha)
            bfsRota[filha] = currCell
            bSearch.append(filha)
    invRota={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        invRota[bfsRota[cell]]=cell
        cell=bfsRota[cell]
    return bSearch,bfsRota,invRota


#a posicao de inicio esta fixada na posicao mais distante na porcao inferior direita do labirinto
#pela biblioteca pymaze

# definicao das dimensoes do labirinto - troque por qualquer valor
labirinto = maze(10,10)

#sorteio da posicao de objetivo do labirinto - troque por qualquer valor
x = randint(0,10)
y = randint(0,10)
#loopPercent representa a quantidade de possibilidades de caminho ate o objetivo, se 0, será
#um labirinto com solucao unica

labirinto.CreateMaze(x, y, loopPercent=50)
buscaBfs, bfsRota, RotaInv=BFS(labirinto)
a=agent(labirinto,footprints=True,color=COLOR.red,shape='square',filled=True)
b=agent(labirinto,footprints=True,color=COLOR.yellow,shape='square',filled=False)
c=agent(labirinto,x,y,footprints=True,color=COLOR.green,shape='square',filled=True,goal=(labirinto.rows,labirinto.cols))
labirinto.tracePath({a:buscaBfs}, delay=120)
labirinto.tracePath({c:bfsRota}, delay=120)
labirinto.tracePath({b:RotaInv}, delay=120)

labirinto.run()
