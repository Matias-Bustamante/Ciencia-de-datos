from scipy import stats 
import matplotlib.pyplot as plt 
import numpy as np 

np.random.seed(0)

# Detalle de visualización 
plt.rcParams["font.size"]=16 
plt.rcParams["axes.spines.top"]=False 
plt.rcParams["axes.spines.right"]=False 
plt.rcParams["axes.spines.left"]=False 



def datos_sesgados(sesgos, cantidad, maximo):
    aleatorios=stats.skewnorm.rvs(sesgos, size=cantidad, random_state=0)
    aleatorios=aleatorios+abs(aleatorios.min())
    aleatorios=np.round(aleatorios, 2)/aleatorios.max()*maximo
    return np.round(aleatorios,1)


##Extracción de una muestra
def extraccion_muestra(tamanio_muestra, calificaciones):
    muestra=np.random.choice(calificaciones,tamanio_muestra )
    return muestra 

def muestras_bootstrap(tamanio_muestra, calificacion):
    muestras=np.array([])
    total_muestras=1000 
    for i in range(total_muestras): 
        muestras=np.append(muestras, np.random.choice(calificacion, tamanio_muestra, replace=True))

    muestras=muestras.reshape(-1, tamanio_muestra)
    return muestras 

def intervalos_confianza(muestra):
    intervalo_confianza=np.quantile(muestra.mean(axis=1), [0.025, 0.975])
    x=np.linspace(intervalo_confianza[0], intervalo_confianza[1], 100)
    y=[10]*x.size
    return x,y,intervalo_confianza 

def graficos(calificacion, muestras, x, y, intervalo):
   
    disenio=[ 
        ["A", "B"], 
        ["C", "C"]
    ]
    fig, axs=plt.subplot_mosaic(disenio, figsize=(12,10))
    axs['A'].hist(calificacion, bins=11, color="blue", edgecolor="black")
    axs['A'].set_title("Población de estudiantes")
    axs['A'].set_xticks(range(0,11))
    axs['A'].set_xlabel("Calificaciones")
    axs['A'].set_ylabel("Frecuencia")

    axs['B'].hist(muestras.mean(axis=1), bins=100, color="red")
    axs['B'].set_title("Distribución de medias muestral")
    axs['B'].set_xlabel("Calificaciones promedio de las muestras")
    axs['B'].set_ylabel("Frecuencia")


    axs['C'].scatter(x,y,color="deeppink", s=100)

    axs['C'].axvline(intervalo[0], label="IC: Limite inferior", 
                color="deeppink",
                lw=4, 
                linestyle="--"
                )
    
    
    axs['C'].axvline(intervalo[1], label="IC: Limite superior", 
                color="deeppink",
                lw=4, 
                linestyle="--"
                )
    
    axs['C'].axvline(calificacion.mean(), 
                label="Media poblacional", 
                color="gold",
                lw=10, 
                linestyle=":")
    
    axs['C'].hist(muestras.mean(axis=1), bins=100, 
             alpha=0.5, 
             color="turquoise")
    
    axs['C'].set_title("Intervalos de confianza al 95%")
    axs['C'].set_xlabel("Calificaciones promedio de las muestras")
    axs['C'].set_ylabel("Frecuencia")
    axs['C'].legend(bbox_to_anchor=(1,0.5))
    
   
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.4, wspace=2)
    plt.show()

    



calificacion=datos_sesgados(-25.0, 100000, 10)

muestra_principal=extraccion_muestra(tamanio_muestra=100, calificaciones=calificacion)

muestras=muestras_bootstrap(tamanio_muestra=100, calificacion=calificacion)

puntos=intervalos_confianza(muestras)

graficos(calificacion=calificacion, muestras=muestras, x=puntos[0], y=puntos[1], intervalo=puntos[2])




