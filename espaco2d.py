#Autor: Isaque Copque
import numpy as np
np.seterr(invalid='ignore',divide='ignore') #ignora divisão por zero, campo no próprio ponto
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

#Escolha do sistema
sisOp = int ( input('''
Escolha o sistema de carga: 
(1)Carga Isolada
(2)Dipolo 
(3)Circulo Condutor
(4)Circulo Isolante
(5)Semiplano Infinito condutor 
(6)Semiplano Infinito isolante
--> ''') )
#-----------------------------

#-------------------------Variáveis Globais-------------------------------------------
q = 0.0023 #Carga total pode ser mudada
cargas = [] #cargas do sistema
tamanho = 51 #Tamanho do espaço, no mínimo 7, para algumas figuras serem visíveis, pode ser mudado
const_k0 = 1/4*np.pi*8.85e-12
espaco = np.full((tamanho,tamanho),const_k0)
raio = 3 #raio para os circulos, pode ser mudado
#------------------------------------------------------------------------------------

#-----------------------Configuracoes de plot----------------------------------------
#criacão dos eixos
eixoX, eixoY = np.meshgrid(np.arange(tamanho),np.arange(tamanho)) #usado nos plots
pontos = list( zip( eixoX.flatten(), eixoY.flatten() ) ) #obtém pontos dos eixos

#Cor da carga
if q < 0:
  cor = 'red'
else:
  cor = 'blue'

#Plot1
fig1, ax1 = plt.subplots(figsize = (10,10))
ax1.set_title("Campo elétrico")

#Plot2
fig2,ax2 = plt.subplots(figsize=(10,10))
ax2.set_title("Linhas de força")

#Plot3
fig3,ax3 = plt.subplots(figsize=(10,10))
ax3.set_title("Potencial elétrico") 
#-------------------------------------------------------------------------------

#-----------------Configuracao do sistema--------------------------------------

#Carga isolada 
if sisOp == 1: 
    cargas.append((q, (int(tamanho/2),int(tamanho/2)) )) #posição da carga, meio do espaco
    ax1.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=0.5,fill=True,color=cor))
    ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=0.5,fill=True,color=cor))
    ax3.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=0.5,fill=True,color=cor))
    #Linhas equipotênciais
    for i in range(tamanho-2):
        ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=i*0.5,fill=False))

#Dipolo
elif sisOp == 2:
    cargas.append((q, (int(tamanho/2)+3,int(tamanho/2)))) #Carga Positiva
    cargas.append((-q, (int(tamanho/2)-3,int(tamanho/2)))) #Carga Negativa
    
    ax1.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)+3),radius=0.5,fill=True,color='blue'))
    ax1.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)-3),radius=0.5,fill=True,color='red'))
    ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)+3),radius=0.5,fill=True,color='blue'))
    ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)-3),radius=0.5,fill=True,color='red'))
    ax3.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)+3),radius=0.5,fill=True,color='blue'))
    ax3.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)-3),radius=0.5,fill=True,color='red'))
    #Linhas equipotênciais
    ax2.axhline(y= ((int(tamanho/2)+3)/2) + ((int(tamanho/2)-3)/2), linestyle='-',color='black')
    for i in range(2,tamanho-2):
        # ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)+3),radius=i*0.25,fill=False))
        # ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)-3),radius=i*0.25,fill=False,color='gray'))
        ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)-3-(i/2)),radius=(i+1)*0.5,fill=False,color='gray'))
        ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)+3+(i/2)),radius=(i+1)*0.5,fill=False))

#Circulo Condutor
elif sisOp == 3:
    dq = q/2*np.pi*raio
    centro = int(tamanho/2)

    #Posições onde há a circunferência com permisividade relativa de 3.5 Silício
    const_k = 1/4*np.pi*3.5

    #borda de cima e de baixo
    for i in range(1-raio,raio):
        espaco[centro+i][centro+raio] = const_k
        espaco[centro+i][centro-raio] = const_k
        cargas.append( (dq, (centro+i,centro+raio) ) )
        cargas.append( (dq, (centro+i,centro-raio) ) )

    #borda da esquerda e da direita
    for i in range(1-raio,raio):
        espaco[centro-raio][centro+i] = const_k
        espaco[centro+raio][centro+i] = const_k
        cargas.append( (dq, (centro-raio,centro+i) ) )
        cargas.append( (dq, (centro+raio,centro+i) ) )

    #parte interna, não há cargas
    for i in range(1-raio,raio):
        for j in range(1-raio,raio):
            espaco[centro+i][centro+j] = const_k
    
    #O circulo possui raio 2.5, partindo do meio da célula de centro até a borda de duas celulas após
    #porém na visualização ele deve ter raio 2.0 pois a flecha de campo sai do centro da celula
    ax1.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=raio,fill=False,color=cor))
    ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=raio,fill=False,color=cor))
    ax3.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=raio,fill=False,color=cor))
    #Equipotenciais
    ax2.add_artist(plt.Circle((centro,centro),radius=0.5,fill=False,color='gray'))
    ax2.add_artist(plt.Circle((centro,centro),radius=1,fill=False,color='gray'))
    for i in range(1,tamanho-2):
        ax2.add_artist(plt.Circle((centro,centro),radius=2.0+(i/2),fill=False,color='gray'))

#Circulo Isolante 
elif sisOp == 4:
    dq = q/np.pi*raio**2
    centro = int(tamanho/2)
    
    #Posições onde há a circunferência com permisividade relativa de 5.7 Mica
    const_k = 1/4*np.pi*5.7

    #borda de cima e de baixo
    for i in range(1-raio,raio):
        espaco[centro+i][centro+raio] = const_k
        espaco[centro+i][centro-raio] = const_k
        cargas.append( (dq, (centro+i,centro+raio) ) )
        cargas.append( (dq, (centro+i,centro-raio) ) )

    #borda da esquerda e da direita
    for i in range(1-raio,raio):
        espaco[centro-raio][centro+i] = const_k
        espaco[centro+raio][centro+i] = const_k
        cargas.append( (dq, (centro-raio,centro+i) ) )
        cargas.append( (dq, (centro+raio,centro+i) ) )

    #parte interna, não há cargas
    for i in range(1-raio,raio):
        for j in range(1-raio,raio):
            espaco[centro+i][centro+j] = const_k
            cargas.append( (dq, (centro+i,centro+j) ) )

    #O circulo possui raio 2.5, partindo do meio da célula de centro até a borda de duas celulas após
    #porém na visualização ele deve ter raio 2.0 pois o flecha de campo sai do centro da celula
    ax1.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=raio,fill=False,color=cor))
    ax2.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=raio,fill=False,color=cor))
    ax3.add_artist(plt.Circle((int(tamanho/2),int(tamanho/2)),radius=raio,fill=False,color=cor))

    #Linhas equipotênciais
    for i in range(1,tamanho-2,2):
        ax2.add_artist(plt.Circle((centro,centro),radius=(i*0.5),fill=False,color='gray'))

#Semiplano condutor
elif sisOp == 5:
    dq = q/5*tamanho
    centro = int(tamanho/2)

    #Posições onde há o plano com permisividade relativa de 3.5 Silício
    const_k = 1/4*np.pi*3.5

    for i in range(centro-2,centro+3):
        for j in range(tamanho):
            espaco[j][i] = const_k
            cargas.append( (dq, (j,i) ) )
    
    ax1.add_artist(plt.Rectangle((centro-2,-1), 4, tamanho+1, color=cor,zorder=0))
    ax2.add_artist(plt.Rectangle((centro-2,-1), 4, tamanho+1, color = cor,zorder=0))
    

    #Linhas equipotênciais
    for i in range(0,centro-2):
       ax2.axvline(i,color='gray')
       ax2.axvline(i+0.5,color='gray')
    for i in range(centro+2,tamanho-1):
       ax2.axvline(i,color='gray')
       ax2.axvline(i+0.5,color='gray')
    #Elipses equipotênciais
    ax2.add_patch(Ellipse(xy=(centro,centro),width=2,height=(tamanho-2)/2,color='gray',fill=False))
    ax2.add_patch(Ellipse(xy=(centro,centro),width=4,height=tamanho-2,color='gray',fill=False))

#Semiplano Isolante
elif sisOp == 6:
    dq = q/5*tamanho
    centro = int(tamanho/2)

    #Posições onde há o plano com permisividade relativa de 5.7 Mica
    const_k = 1/4*np.pi*5.7

    for i in range(centro-2,centro+3):
        for j in range(tamanho):
            espaco[j][i] = 5.7
            cargas.append( (dq, (j,i) ) )
    
    ax1.add_artist(plt.Rectangle((centro-2,-1), 4, tamanho+1, color=cor, zorder=0))
    ax2.add_artist(plt.Rectangle((centro-2,-1), 4, tamanho+1, color = cor,zorder=0))

    #Linhas equipotênciais
    for i in range(0,centro-2):
       ax2.axvline(i,color='gray')
       ax2.axvline(i+0.5,color='gray')
    for i in range(centro+2,tamanho-1):
       ax2.axvline(i,color='gray')
       ax2.axvline(i+0.5,color='gray')
    #Elipses equipotênciais
    ax2.add_patch(Ellipse(xy=(centro,centro),width=2,height=(tamanho-2)/2,color='gray',fill=False))
    ax2.add_patch(Ellipse(xy=(centro,centro),width=4,height=tamanho-2,color='gray',fill=False))
   
else:
    print("Sistema escolhido inválido!")
    quit()

#----------------------------------------------------------------------------------

#----------------------Cálculos Campo e Potencial-------------------------------
#Estruturas para calcular o campo
Ex = np.zeros((tamanho, tamanho))
Ey = np.zeros((tamanho, tamanho))

#----------------Cálculo do campo elétrico ---------------------
#Calcula as componentes do vetor campo elétrico gerado em todos os pontos
#e usa o princípio da superposição para obter o campo devido todas as cargas

for carga in cargas:  #para cada carga
    qc = carga[0] # o dq da carga em questão
    cp = carga[1] #posição da carga em questão
    for p in pontos: #para cada ponto
        x = p[0]
        y = p[1]
        r = np.hypot(x-cp[0], y-cp[1],out=None)**3 #distância ao cubo da carga
        if r != 0: #evita divisão por zero, o ponto não é a própria carga
            Ey[x][y] += ( qc*espaco[x][y]*(x-cp[0]) )/r
            Ex[x][y] += ( qc*espaco[x][y]*(y-cp[1]) )/r

# #Para mostrar os valores de campo obtido, descomente este trecho de código :
# print("Ex: ")
# for i,linha in enumerate(Ex):
#     print("\nLinha ",i,": ",linha)      
# print("\nEy: ")
# for i,linha in enumerate(Ey):
#     print("\nLinha ",i,": ",linha)  

#-----------------------------------------------------------------

#----------------Cálculo do potencial elétrico---------------------
#Calcula o potencial elétrico gerado em todos os pontos
#e usa o princípio da superposição para obter o potencial devido todas as cargas

V = np.zeros((tamanho,tamanho))
for carga in cargas:
    qc = carga[0] # o dq da carga em questão
    cp = carga[1] #posição da carga em questão
    for p in pontos:
        x = p[0]
        y = p[1]
        r = np.hypot(x-cp[0], y-cp[1])
        if r != 0: #evita divisão por zero, o ponto não é a própria carga
            V[x][y] += qc*espaco[x][y]/r    
   
# #Para mostrar os valores de potencial obtido, descomente este trecho de código :     
# print("Potencial: ")
# for i,linha in enumerate(V):
#     print("\nLinha ",i,": ",linha)  


# #----------------Plotagem-----------------------------------------------

# Quiver do campo elétrico
norma = np.hypot(Ex,Ey) #normaliza os vetores de campo elétrico, serve também para as cores
# norma =  np.where(np.hypot(Ex,Ey) != 0, np.hypot(Ex,Ey), 1)

fig1 = ax1.quiver(eixoX,eixoY,Ex/norma,Ey/norma,norma,pivot='middle',cmap=plt.cm.magma) #plota o quiver
plt.colorbar(fig1,ax=ax1)#mapa de cores

# #Linhas de força
ax2.streamplot(eixoX,eixoY,Ex,Ey,color=norma,cmap=plt.cm.magma,density=2)

# #Potencial elétrico
fig3 = ax3.imshow(V,cmap="magma", origin="lower")
plt.colorbar(fig3,ax=ax3)#mapa de cores

plt.show()
#-------------------------------------------------------------------------------