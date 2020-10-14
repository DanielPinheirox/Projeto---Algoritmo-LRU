# Universidade Paulista - UNIP
# Disciplina: Sistemas Operacionais Aberto
# Aluno: Daniel Pinheiro MATRICULA: D414496

# ALGORITMO DE SUBSTITUIÇÂO DE PÁGINA - LRU (Least Recently Used)
  
# Declaração dos Parametros a serem utilizados
# Slot da Memoria
quantidadeM = 4 

# Leitura dos Dados no Array 
parametroList = [ 4, 2, 3, 0, 3, 2, 7, 
                0, 1, 2, 0, 3, 0] 
                  
# Lista das páginas atuais na memória

Array = []  
  
faltadPagina = 0
 
  
print("ALGORITMO DE SUBSTITUIÇAO DE PAGINA - LRU")


for i in parametroList: 
  
    # Se i não estiver presente na lista de páginas atual

    if i not in Array: 
  
        # Verifique se a lista pode conter páginas iguais - Sim incrementar na memoria / Não alocar novo espaço
        if(len(Array) == quantidadeM): 
            Array.remove(Array[0]) 
            Array.append(i) 
  
        else: 
            Array.append(i) 
  
        # Incrementar falhas de páginas 
        faltadPagina +=1
   
    else: 
          
        # Remove o indice anterior da página atual 
        Array.remove(i) 
  
        # Apresenta  ultimo indice
        Array.append(i) 
      
print("Total de Paginas Falhadas: {} ".format(faltadPagina)) 
  