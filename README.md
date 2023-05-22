# Projeto---Algoritmo-LRU
Algoritmo desenvolvido para disciplina (Sistemas Operacionais Abertos) - UNIP

O algoritmo de substituição de página LRU (Least Recently Used - Menos Recentemente Utilizado) é um algoritmo utilizado para gerenciar a memória em sistemas de memória virtual. Ele garante que as páginas menos recentemente usadas sejam substituídas quando ocorrer uma falta de página.

O código fornecido implementa um exemplo simples do algoritmo LRU em Python. Vamos analisar o código em detalhes:

css
Copy code
quantidadeM = 4  
parametroList = [4, 2, 3, 0, 3, 2, 7, 0, 1, 2, 0, 3, 0] 
Array = []  
faltadPagina = 0
print("ALGORITMO DE SUBSTITUIÇAO DE PÁGINA - LRU")

for i in parametroList: 
    if i not in Array:
        if len(Array) == quantidadeM:
            Array.remove(Array[0])
            Array.append(i)
        else:
            Array.append(i)
        faltadPagina += 1
    else:
        Array.remove(i)
        Array.append(i)

print("Total de Páginas Falhadas: {}".format(faltadPagina))
quantidadeM: É a quantidade máxima de páginas que podem estar na memória simultaneamente. Neste exemplo, é definida como 4.

parametroList: É uma lista que contém a sequência de páginas acessadas. Cada número representa uma página que é acessada.

Array: É uma lista que representa a memória, onde as páginas estão armazenadas.

faltadPagina: É uma variável que registra o número total de faltas de página.

O loop for i in parametroList itera sobre cada página na sequência.

O primeiro if i not in Array verifica se a página não está presente na memória.

Se a página não estiver presente, o código verifica se a memória está cheia (if len(Array) == quantidadeM).

Se a memória estiver cheia, a página menos recentemente usada é removida (Array.remove(Array[0]) e a nova página é adicionada no final da memória (Array.append(i)).
Se a memória não estiver cheia, a nova página é simplesmente adicionada à memória (Array.append(i)).
A variável faltadPagina é incrementada em 1 para indicar uma falta de página.

Se a página estiver presente na memória, ela é removida (Array.remove(i)) e adicionada novamente no final da memória (Array.append(i)). Essa ação atualiza o carimbo de tempo da página, indicando que ela foi a mais recentemente usada.

Por fim, é exibido o total de páginas falhadas, ou seja, o valor final da variável faltadPagina.

Em resumo, o algoritmo LRU implementado nesse código mantém uma lista (Array) que representa a memória e acompanha a ordem de uso das páginas. Sempre que uma falta de página ocorre, a página menos recentemente usada é substituída. O código conta o número total de faltas de página e o exibe ao final.
