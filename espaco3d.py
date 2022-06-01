#Autor: Isaque Copque
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d

#Escolha do sistema
sisOp = int ( input('''
Escolha o sistema de carga: 
(1)Esfera condutora
(2)Casca esférica
(3)Esfera isolante
--> ''') )
#-----------------------------

#-------------------------Variáveis Globais-------------------------------------------
q = 0.0023 #Carga total, pode ser mudada
cargas = [] #cargas do sistema
tamanho = 9 #tamanho do espaço, pode ser mudado
meio = int(tamanho/2)
raio = 2 #raio das esferas, pode ser mudado
u = np.linspace(0, 2*np.pi, 30) #theta
v = np.linspace(0, np.pi, 30) #phi
const_k0 = 1/4*np.pi*8.85e-12
espaco = np.full((tamanho,tamanho,tamanho),const_k0)
#------------------------------------------------------------------------------------

#-----------------------Configuracoes de plot----------------------------------------

#criacão dos eixos
eixoX, eixoY, eixoZ = np.meshgrid(np.arange(tamanho),np.arange(tamanho),np.arange(tamanho))
pontos = list( zip( eixoX.flatten(), eixoY.flatten(), eixoZ.flatten() ) ) #obtém pontos dos eixos

x = meio + raio * np.outer(np.cos(u), np.sin(v))
y = meio + raio * np.outer(np.sin(u), np.sin(v))
z = meio + raio * np.outer(np.ones(np.size(u)), np.cos(v))

#Cores
if q < 0:
  coresf = 'red'
  corint = 'blue'
else:
  coresf = 'blue'
  corint = 'red'

#Plot1
fig1 = plt.figure()
ax1 = fig1.add_subplot(projection ='3d')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z') 
ax1.set_title("Campo elétrico")

#Plot2
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection ='3d')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z') 
ax2.set_title("Potencial elétrico")

#Plot3
fig3 = plt.figure()
ax3 = fig3.add_subplot(projection ='3d')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z') 
ax3.set_title("Equipotenciais")

#Configurações para as equipotênciais
planoX, planoY = np.meshgrid(np.arange(tamanho),np.arange(tamanho))

#-------------------------------------------------------------------------------

#-----------------Configuracao do sistema--------------------------------------

#Esfera condutora com carga na superfície 
if sisOp == 1: 
    dq = q/ (4*np.pi*raio**2) #Q/Área da superficie

    #Preenchimento da matriz com cargas na Superfície
    for zindex in range(meio-raio+1,meio+raio):
        for xyindex in range(meio-raio+1, meio+raio):
            #casca esquerda
            espaco[meio-raio][xyindex][zindex] = 3.5
            cargas.append( (dq,(meio-raio,xyindex,zindex) ) )
            #casca direita  
            espaco[meio+raio][xyindex][zindex] = 3.5
            cargas.append( (dq,(meio+raio,xyindex,zindex) ) )
            #casca de tras
            espaco[xyindex][meio-raio][zindex] = 3.5
            cargas.append( (dq,(xyindex,meio-raio,zindex) ) ) 
            #casca da frente
            espaco[xyindex][meio+raio][zindex] = 3.5
            cargas.append( (dq,(xyindex,meio+raio,zindex) ) ) 

            for axindex in range(meio-raio+1,meio+raio):
                #casca superior
                espaco[xyindex][axindex][meio+raio] = 3.5
                cargas.append( (dq,(xyindex,axindex,meio+raio) ) )
                #casca inferior
                espaco[xyindex][axindex][meio-raio] = 3.5
                cargas.append( (dq,(xyindex,axindex,meio-raio) ) )

    
    #Parte interna da esfera
    for zindex in range(meio-raio+1,raio+meio):
        for yindex in range(meio-raio+1,raio+meio):
            for iindex in range(meio-raio+1,raio+meio):
                espaco[iindex][yindex][zindex] = 3.5

    #Equipotenciais       
    for i in range(0,meio-raio):#Antes da esfera
        ax3.plot_surface(0*planoX +i,planoY,planoX,color='black')
    for i in range(meio+raio+1,tamanho):#Depois da esfera
        ax3.plot_surface(0*planoX +i,planoY,planoX,color='black')
    for i in range(meio-raio, meio+raio): #Na esfera
        circuloexterno = Circle((meio,meio),raio,color='orange',fill=False)
        ax3.add_patch(circuloexterno)
        art3d.pathpatch_2d_to_3d(circuloexterno,i)
        circulointerno = Circle((meio,meio),raio-1,color='yellow')
        ax3.add_patch(circulointerno)
        art3d.pathpatch_2d_to_3d(circulointerno,i)

    ax1.plot_surface(x,y,z,color=coresf) #Plota esfera

#Casca esférica condutora 3.5 Silício
elif sisOp == 2:
    dq = q/ (4*np.pi*raio**2) #Q/Área da superficie

   #Preenchimento da matriz com cargas na Superfície
    for zindex in range(meio-raio+1,meio+raio):
        for xyindex in range(meio-raio+1, meio+raio):
            #casca esquerda
            espaco[meio-raio][xyindex][zindex] = 3.5
            cargas.append( (dq,(meio-raio,xyindex,zindex) ) )
            #casca direita  
            espaco[meio+raio][xyindex][zindex] = 3.5
            cargas.append( (dq,(meio+raio,xyindex,zindex) ) )
            #casca de tras
            espaco[xyindex][meio-raio][zindex] = 3.5
            cargas.append( (dq,(xyindex,meio-raio,zindex) ) ) 
            #casca da frente
            espaco[xyindex][meio+raio][zindex] = 3.5
            cargas.append( (dq,(xyindex,meio+raio,zindex) ) ) 

            for axindex in range(meio-raio+1,meio+raio):
                #casca superior
                espaco[xyindex][axindex][meio+raio] = 3.5
                cargas.append( (dq,(xyindex,axindex,meio+raio) ) )
                #casca inferior
                espaco[xyindex][axindex][meio-raio] = 3.5
                cargas.append( (dq,(xyindex,axindex,meio-raio) ) )

    #Equipotenciais       
    for i in range(0,meio-raio):#Antes da esfera
        ax3.plot_surface(0*planoX +i,planoY,planoX,color='black')
    for i in range(meio+raio+1,tamanho):#Depois da esfera
        ax3.plot_surface(0*planoX +i,planoY,planoX,color='black')
    for i in range(meio-raio, meio+raio): #Na esfera
        circuloexterno = Circle((meio,meio),raio,color='orange',fill=False)
        ax3.add_patch(circuloexterno)
        art3d.pathpatch_2d_to_3d(circuloexterno,i)
    ax3.scatter(meio,meio,meio+raio,color='yellow')
    ax3.scatter(meio,meio,meio-raio,color='yellow')

    ax1.scatter(x,y,z,color=coresf) #Plota esfera

#Esfera isolante com carga no volume 5.7 Mica
elif sisOp == 3:
    dq = q/ ((4*np.pi*raio**3)/3) #Q/Volume da esfera

    #Preenchimento da matriz na casca
    for zindex in range(meio-raio+1,meio+raio):
        for xyindex in range(meio-raio+1, meio+raio):
            #casca esquerda
            espaco[meio-raio][xyindex][zindex] = 5.7
            #casca direita  
            espaco[meio+raio][xyindex][zindex] = 5.7
            #casca de tras
            espaco[xyindex][meio-raio][zindex] = 5.7 
            #casca da frente
            espaco[xyindex][meio+raio][zindex] = 5.7

            for axindex in range(meio-raio+1,meio+raio):
                #casca superior
                espaco[xyindex][axindex][meio+raio] = 5.7
                #casca inferior
                espaco[xyindex][axindex][meio-raio] = 5.7

    #Preenchimento da matriz com carga no volume
    for zindex in range(meio-raio+1,raio+meio):
        for yindex in range(meio-raio+1,raio+meio):
            for iindex in range(meio-raio+1,raio+meio):
                espaco[iindex][yindex][zindex] = 5.7
                cargas.append( (dq,(iindex,yindex,zindex) ) )

    #Equipotenciais       
    for i in range(0,meio-raio):#Antes da esfera
        ax3.plot_surface(0*planoX +i,planoY,planoX,color='black')
    for i in range(meio+raio+1,tamanho):#Depois da esfera
        ax3.plot_surface(0*planoX +i,planoY,planoX,color='black')
    for i in range(meio-raio, meio+raio+1): #Na esfera
        circuloexterno = Circle((meio,meio),raio,color='pink',fill=False)
        ax3.add_patch(circuloexterno)
        art3d.pathpatch_2d_to_3d(circuloexterno,i)
        circulointerno = Circle((meio,meio),raio-1,color='orange')
        ax3.add_patch(circulointerno)
        art3d.pathpatch_2d_to_3d(circulointerno,i)
    ax3.scatter(meio,meio,meio,s=50.0,color='red')

    ax1.plot_surface(x,y,z,color=coresf) #Plota esfera
    
else:
    print("Sistema escolhido inválido!")
    quit()

#----------------------------------------------------------------------------------

#----------------------Cálculos Campo e Potencial-------------------------------

Ex = np.zeros((tamanho, tamanho, tamanho))
Ey = np.zeros((tamanho, tamanho, tamanho))
Ez = np.zeros((tamanho, tamanho, tamanho))

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

V = np.zeros((tamanho,tamanho,tamanho))
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

##Este trecho de código gera o gráfico que mostra a intensidade do campo em função da distância
#Descomente este trecho de códgio para gerar o gráfiico
fig4,ax4 = plt.subplots(1,2)
E = []
dist = []

#Do centro para fora da esfera
for zindex in range(meio+raio,tamanho):
    vetorcampo = ( Ex[meio][meio][zindex], Ex[meio][meio][zindex], Ex[meio][meio][zindex])
    E.append(np.linalg.norm(vetorcampo))
    dist.append( zindex - (meio+raio) )
ax4[0].set_title("Campo elétrico em função da distância")
ax4[0].set_xlabel("Distância (m)")
ax4[0].text(meio+raio,0,"Borda da esfera",rotation=90)
ax4[0].plot(dist,E)

E = []
dist = []
##De uma borda a outra
for zindex in range(meio-raio,meio+raio+1):
    vetorcampo = ( Ex[meio][meio][zindex], Ex[meio][meio][zindex], Ex[meio][meio][zindex])
    E.append(np.linalg.norm(vetorcampo))
    dist.append( zindex )
ax4[1].set_title("Campo elétrico dentro da esfera")
ax4[1].set_xlabel("Eixo Z")
ax4[1].text(meio,0,"Centro Esfera",rotation=90)
ax4[1].text(meio-raio,0,"Casca",rotation=90)
ax4[1].text(meio+raio,0,"Casca",rotation=90)

ax4[1].plot(dist,E)
ax4[1].set_xticks(dist)
ax4[1].set_ylabel("Campo elétrico (V/m)")
ax4[0].set_ylabel("Campo elétrico (V/m)")

#-----------------------------------------------------------------

#----------------Plotagem-----------------------------------------------
# Quiver do campo elétrico
norma = np.sqrt(Ex**2 + Ey**2 + Ez**2)#normaliza os vetores de campo elétrico
fig1 = ax1.quiver(eixoX,eixoY,eixoZ,Ex/norma,Ey/norma,Ez/norma,pivot='middle') #plota o quiver

fig2 = ax2.scatter(eixoX,eixoY,eixoZ,cmap='magma',c=V)
plt.colorbar(fig2,ax=ax2)#mapa de cores

plt.show()