from scipy import stats 
import matplotlib.pyplot as plt 
import numpy as np 


np.random.seed(0)
plt.rcParams["font.size"]=18 

def datos_sesgados(sesgos, cantidad, maximo):
    aleatorios=stats.skewnorm.rvs(sesgos, size=cantidad, random_state=1)
    aleatorios=aleatorios+abs(aleatorios.min())
    aleatorios=aleatorios/aleatorios.max() * maximo 
    return aleatorios 

def TeoremaLimiteCentral(tamanio_muestra, num_muestra, edades):
    for tamanio in tamanio_muestra: 
        promedio=np.array([])
        for i in range(num_muestra): 
            promedio=np.append(promedio, np.random.choice(edades, tamanio).mean())
        
        plt.title("Tamaño de la muestra: "+str(tamanio))
        plt.hist(promedio, bins=1000, alpha=0.5, color="blue")
        plt.show()




tamano_muestras = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000]
num_muestras = 10000
mayores=datos_sesgados(-10, 100000, 100) ##Edades de personas mayores 
plt.hist(mayores, bins=1000, alpha=0.5, label="Mayores", color="blue")
jovenes=datos_sesgados(10,100000, 100) ## Edades de personas jovenes
plt.hist(jovenes, bins=1000, alpha=0.5, label="Jóvenes", color="orange")
normales=datos_sesgados(0, 10000, 100) ## Edades normales 
plt.hist(normales, bins=1000, alpha=0.5, label="Normales", color="red")


TeoremaLimiteCentral(tamanio_muestra=tamano_muestras, num_muestra=num_muestras, mayores=mayores) #Edades mayores 
TeoremaLimiteCentral(tamanio_muestra=tamano_muestras, num_muestra=num_muestras, edades=jovenes) #Edades jovens
TeoremaLimiteCentral(tamanio_muestra=tamano_muestras, num_muestra=num_muestras, edades=normales) #Edades normales

plt.ylim([0,400])
plt.xlim([0,100])
plt.legend(bbox_to_anchor=(1,0.5))
plt.show()


