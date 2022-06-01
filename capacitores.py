#Autor: Isaque Copque
import numpy as np
import matplotlib.pyplot as plt

#Escolha do sistema
sisOp = int ( input('''
______________________________
|Escolha o sistema de carga: | 
|____________________________|
|Variação de distâncias      |
|(1) d = 10                  |
|(2) d = 8                   |
|(3) d = 6                   |
|(4) d = 1                   |
|____________________________|
|Variação de Sigma           |
|(5) Sigma/4                 |
|(6) Sigma/2                 |
|(7) Sigma*2                 |
|(8) Sigma*4                 |
|____________________________|
|Espaço preenchido           |
|(9) Papel 2.0               |
|(10) Fluorita 6.8           |
|(11) Calcita 8.3            |
|____________________________|
--> ''') )
#-----------------------------

#-------------------------Variáveis Globais-------------------------------------------
q = 0.0023 #Carga total
cargas = [] #cargas do sistema
tamanho = 5 #Planos tem tamanho 5x5
tamespaco = tamanho+3 # espaço tem tamanho+2 x tamanho+2
dq = q/tamanho**2 #dq = Q/Área do plano
const_k0 = 1/4*np.pi*8.85e-12
const_k = 1/4*np.pi*1 #Placas
espaco = np.full((tamespaco,tamespaco,13),const_k0) #eixo z vai de 0 até 13
posiz = None
#------------------------------------------------------------------------------------
#-----------------------Configuracoes de plot----------------------------------------

#criacão dos eixos
eixoX, eixoY, eixoZ = np.meshgrid(np.arange(tamespaco),np.arange(tamespaco),np.arange(13))
pontos = list( zip( eixoX.flatten(), eixoY.flatten(), eixoZ.flatten() ) ) #obtém pontos dos eixos

#Plot1
fig1 = plt.figure()
ax1 = fig1.add_subplot(projection ='3d')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z') 

#Plot2
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection ='3d')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z') 
#-------------------------------------------------------------------------------
#-----------------Configuracao do sistema--------------------------------------
#Variação de distância
#Distancia 10 
if sisOp == 1: 
    posiz = [0,10]

    planoX, planoY = np.meshgrid(np.arange(tamanho+1),np.arange(tamanho+1))
    ax1.plot_surface(planoX,planoY, posiz[1]+np.zeros_like(planoX),color='blue')
    ax1.plot_surface(planoX,planoY, posiz[0]+np.zeros_like(planoX), color='red')

    #preenche o espaço com a permisividade dos planos
    for x in range(0,tamanho+1):
        for y in range(0,tamanho+1):
            #Plano de cima
            espaco[x][y][posiz[1]] = const_k 
            cargas.append( (dq, (x,y,posiz[1]) ) )
            #Plano de baixo
            espaco[x][y][posiz[0]] = const_k
            cargas.append( (-dq, (x,y,posiz[0]) ) )

#Distancia 8 
elif sisOp == 2:

    posiz = [1,9]

    planoX, planoY = np.meshgrid(np.arange(tamanho+1),np.arange(tamanho+1))
    ax1.plot_surface(planoX,planoY, posiz[1]+np.zeros_like(planoX),color='blue')
    ax1.plot_surface(planoX,planoY, posiz[0]+np.zeros_like(planoX), color='red')

    #preenche o espaço com a permisividade dos planos
    for x in range(0,tamanho+1):
        for y in range(0,tamanho+1):
            #Plano de cima
            espaco[x][y][posiz[1]] = const_k 
            cargas.append( (dq, (x,y,posiz[1]) ) )
            #Plano de baixo
            espaco[x][y][posiz[0]] = const_k
            cargas.append( (-dq, (x,y,posiz[0]) ) )

#Distancia 6 
elif sisOp == 3:

    posiz = [2,8]

    planoX, planoY = np.meshgrid(np.arange(tamanho+1),np.arange(tamanho+1))
    ax1.plot_surface(planoX,planoY, posiz[1]+np.zeros_like(planoX),color='blue')
    ax1.plot_surface(planoX,planoY, posiz[0]+np.zeros_like(planoX), color='red')

    #preenche o espaço com a permisividade dos planos
    for x in range(0,tamanho+1):
        for y in range(0,tamanho+1):
            #Plano de cima
            espaco[x][y][posiz[1]] = const_k 
            cargas.append( (dq, (x,y,posiz[1]) ) )
            #Plano de baixo
            espaco[x][y][posiz[0]] = const_k
            cargas.append( (-dq, (x,y,posiz[0]) ) )

#Distancia 1 
elif sisOp == 4:

    posiz = [5,6]
    planoX, planoY = np.meshgrid(np.arange(tamanho+1),np.arange(tamanho+1))
    ax1.plot_surface(planoX,planoY, posiz[1]+np.zeros_like(planoX),color='blue')
    ax1.plot_surface(planoX,planoY, posiz[0]+np.zeros_like(planoX), color='red')

    #preenche o espaço com a permisividade dos planos
    for x in range(0,tamanho+1):
        for y in range(0,tamanho+1):
            #Plano de cima
            espaco[x][y][posiz[1]] = const_k 
            cargas.append( (dq, (x,y,posiz[1]) ) )
            #Plano de baixo
            espaco[x][y][posiz[0]] = const_k
            cargas.append( (-dq, (x,y,posiz[0]) ) )

#Variação de densidade
# sigma/2
elif sisOp >= 5 and sisOp <= 8:
    posiz = [0,10]

    if sisOp == 5:
        dq = dq/4
    elif sisOp == 6:
        dq = dq/2
    elif sisOp == 7:
        dq = dq*2
    elif sisOp == 8:
        dq = dq*4

    planoX, planoY = np.meshgrid(np.arange(tamanho+1),np.arange(tamanho+1))
    ax1.plot_surface(planoX,planoY, posiz[1]+np.zeros_like(planoX),color='blue')
    ax1.plot_surface(planoX,planoY, posiz[0]+np.zeros_like(planoX), color='red')

    #preenche o espaço com a permisividade dos planos
    for x in range(0,tamanho+1):
        for y in range(0,tamanho+1):
            #Plano de cima
            espaco[x][y][posiz[1]] = const_k 
            cargas.append( (dq, (x,y,posiz[1]) ) )
            #Plano de baixo
            espaco[x][y][posiz[0]] = const_k
            cargas.append( (-dq, (x,y,posiz[0]) ) )

#Espaço entre placas preenchido Papel 2.0, Fluorita 6.8 , Calcita 8.3, 
elif sisOp >= 9 and sisOp <= 11: 
    posiz = [0,10]

    er = 0
    if sisOp == 9:
        er = 2.0 #Papel 2.0
    elif sisOp == 10:
        er = 6.8 #Fluorita 6.8
    else:
        er = 8.3 #Calcita 8.3

    planoX, planoY = np.meshgrid(np.arange(tamanho+1),np.arange(tamanho+1))
    ax1.plot_surface(planoX,planoY, posiz[1]+np.zeros_like(planoX),color='blue')
    ax1.plot_surface(planoX,planoY, posiz[0]+np.zeros_like(planoX), color='red')

    #preenche o espaço com a permisividade dos planos
    for x in range(0,tamanho+1):
        for y in range(0,tamanho+1):
            #Plano de cima
            espaco[x][y][posiz[1]] = const_k 
            cargas.append( (dq, (x,y,posiz[1]) ) )
            #Plano de baixo
            espaco[x][y][posiz[0]] = const_k
            cargas.append( (-dq, (x,y,posiz[0]) ) )

    #Preenche o espaço com as constantes dieletricas
    const_k = 1/4*np.pi*er
        
    for z in range(1, 10): #z= 1,2,...,9
        for x in range(0,tamanho+1): #x = 0,...,5
            for y in range(0,tamanho+1):
                espaco[x][y][z] = const_k
                # ax1.scatter(x,y,z,c = "yellow")
    
else:
    print("Sistema escolhido inválido!")
    quit()
#-------------------------------------------------------------------------------

#----------------------Cálculos Campo e Potencial-------------------------------

Ex = np.zeros((tamespaco, tamespaco, 13))
Ey = np.zeros((tamespaco, tamespaco, 13))
Ez = np.zeros((tamespaco, tamespaco, 13))

#----------------Cálculo do campo elétrico ---------------------
#Calcula as componentes do vetor campo elétrico gerado em todos os pontos
#e usa o princípio da superposição para obter o campo devido todas as cargas

for carga in cargas:  #para cada carga
    qc = carga[0] # o dq da carga em questão
    cp = carga[1] #posição da carga em questão
    for p in pontos: #para cada ponto
        x = p[0]
        y = p[1]
        z = p[2]
        r = np.sqrt( (x-cp[0])**2 +  (y-cp[1])**2 + (z-cp[2])**2 )**3 #distância ao cubo da carga
        if r != 0: #evita divisão por zero, o ponto não é a própria carga
            Ey[x][y][z] += ( qc*espaco[x][y][z]*(x-cp[0]) )/r
            Ex[x][y][z] += ( qc*espaco[x][y][z]*(y-cp[1]) )/r
            Ez[x][y][z] += ( qc*espaco[x][y][z]*(z-cp[2]) )/r

# #Para mostrar os valores de campo obtido, descomente este trecho de código :
# print("Ex: ")
# for i,linha in enumerate(Ex):
#     print("\nLinha ",i,": ",linha)      
# print("\nEy: ")
# for i,linha in enumerate(Ey):
#     print("\nLinha ",i,": ",linha)  
# print("\nEz: ")
# for i,linha in enumerate(Ez):
#     print("\nLinha ",i,": ",linha)  

#-----------------------------------------------------------------

#----------------Cálculo do potencial elétrico---------------------
#Calcula o potencial elétrico gerado em todos os pontos
#e usa o princípio da superposição para obter o potencial devido todas as cargas

V = np.zeros((tamespaco,tamespaco,13))
for carga in cargas:
    qc = carga[0] # o dq da carga em questão
    cp = carga[1] #posição da carga em questão
    for p in pontos:
        x = p[0]
        y = p[1]
        z = p[2]
        r = np.sqrt( (x-cp[0])**2 +  (y-cp[1])**2 + (z-cp[2])**2 )
        if r != 0: #evita divisão por zero, o ponto não é a própria carga
            V[p[0]][p[1]][p[2]] += qc*espaco[p[0]][p[1]][p[2]]/r  

# #Para mostrar os valores de potencial obtido, descomente este trecho de código :     
# print("Potencial: ")
# for i,linha in enumerate(Ey):
#     print("\nLinha ",i,": ",linha)  

##Trecho de código que cria o gráfico que mostra o campo elétrico em função do eixo Z
fig4, ax4 = plt.subplots(figsize = (10,10))
centro = 2
modulos = []
for i in range(0,13):
    vetorCampo = (Ex[centro][centro][i],Ey[centro][centro][i],Ez[centro][centro][i])
    modulo = np.linalg.norm(vetorCampo)
    modulos.append(modulo)

ax4.plot(range(0,13),modulos)
ax4.text(posiz[0],0,"Placa Negativa",rotation=90)
ax4.text(posiz[1],0,"Placa Positiva", rotation=90)
ax4.set_xticks(range(0,13))
ax4.set_xlabel("Eixo z")
ax4.set_ylabel("Campo elétrico (V/m)")
ax4.set_title("Campo elétrico ao longo do eixo z")


## Cálculo da diferença de potencial na parte interna da placa
## Obtém a ddp somando todos os vetores de campo da placa negativa até a positiva
accE = np.array([0,0,0], dtype=float) #Acumula o campo elétrico
for z in range(posiz[0],posiz[1]+1):
    for x in range(0,tamanho):
        for y in range(0, tamanho):
            vet = np.array([Ex[x][y][z]*(z-posiz[0]), Ey[x][y][z]*(z-posiz[0]), Ez[x][y][z]*(z-posiz[0])]) #E*ds
            accE += vet
ddp = np.linalg.norm(accE)
print("V = ", ddp)
capacit = q/ddp
print("Capacitancia = ",capacit)
print("Energia potencial = ", (capacit*ddp**2)/2)

##Mostra o campo elétrico entre placas no eixo central das placas
# for z in range(11):
#     vet = np.array([Ex[3][3][z], Ey[3][3][z], Ez[3][3][z]])
#     print("Z = ",z," -> E = ",np.linalg.norm(vet))

#---------------------------------------------------------------------------

#-------------------------------------------------------------------------------

norma = np.sqrt(Ex**2 + Ey**2 + Ez**2)#normaliza os vetores de campo elétrico
fig1 = ax1.quiver(eixoX,eixoY,eixoZ,Ex/norma,Ey/norma,Ez/norma,pivot='middle') #plota o quiver

fig2 = ax2.scatter(eixoX,eixoY,eixoZ,cmap='magma',c=V)
plt.colorbar(fig2,ax=ax2)#mapa de cores

plt.show()