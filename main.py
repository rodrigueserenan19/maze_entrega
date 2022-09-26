from pymaze import maze, agent
from random import randint



def teste_objetivo(celulaAtual, objetivo):
    if celulaAtual == objetivo:
        return True
    else:
        return False

def teste_sucessor(m, celulaAtual, j):
    filha = []
    if m.maze_map[celulaAtual][j] == True:
        if j == 'E':
            filha = (celulaAtual[0], celulaAtual[1] + 1)
        if j == 'W':
            filha = (celulaAtual[0], celulaAtual[1] - 1)
        if j == 'N':
            filha = (celulaAtual[0] - 1, celulaAtual[1])
        if j == 'S':
            filha = (celulaAtual[0] + 1, celulaAtual[1])
        return filha

def DFS(m, goal):
    comeco = (m.rows, m.cols)
    visitada = [comeco]
    vizinhanca = [comeco]
    dfsPath = {}
    while len(vizinhanca) > 0:
        currCell = vizinhanca.pop()
        if (teste_objetivo(currCell, goal)==True):
            break
        for d in 'ESNW':
            child = teste_sucessor(m, currCell, d)
            if child in visitada:
                continue
            visitada.append(child)
            vizinhanca.append(child)
            dfsPath[child] = currCell
    fwdPath = {}
    cell = goal
    while cell != comeco:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath



#definicao da dimensao do labirinto
labirinto = maze(10, 10)

#sorteio do objetivo do labirinto
x = randint(0, 10)
y = randint(0, 10)
obj = (x, y)
labirinto.CreateMaze(x, y, loopPercent=50)
path = DFS(labirinto, obj)
a = agent(labirinto, footprints=True, filled=True)
labirinto.tracePath({a: path}, delay=120)
labirinto.run()

#o codigo pode nao rodar na primeira execucao por razoes caoticas. Por favor, tente mais vezes.