import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, butter, filtfilt
from scipy.signal import welch


x_n = np.array([5, 6, 0, 0, 4, 7, 7])  
h_n = np.array([1, 0, 0, 3, 5, 2, 7, 0, 4, 8])  

# Convolución de las señales
y_n = np.convolve(x_n, h_n)

# Gráfico de x[n]
plt.figure(figsize=(8, 5))
plt.stem(range(len(x_n)), x_n, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Señal x[n]')
plt.grid()
plt.show()

# Gráfico de h[n]
plt.figure(figsize=(8, 5))
plt.stem(range(len(h_n)), h_n, basefmt=" ")
plt.xlabel('n')
plt.ylabel('h(n)')
plt.title('Señal h[n]')
plt.grid()
plt.show()

# Gráfico de y[n] 
plt.figure(figsize=(8, 5))
plt.stem(range(len(y_n)), y_n, basefmt=" ")
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Convolución y[n]')
plt.grid()
plt.show()

# Señales dadas en la imagen
x_n = [5, 6, 0, 0, 4, 7, 7]
h_n = [1, 0, 0, 3, 5, 2, 7, 0, 4, 8]

# Convolución de las señales
y_n = np.convolve(x_n, h_n)

# Mostrar la ecuación resultante
ecuacion = "y(n) = " + " + ".join(f"{y_n[i]}x^{i}" for i in range(len(y_n)))
print(ecuacion)



# Parámetros de la señal
Fs = 1 / 1.25e-3  # Frecuencia de muestreo (1 / Ts)
n = np.arange(0, 9, 1)  # Vector de tiempo discreto
Ts = 1.25e-3  # Período de muestreo

# Señales dadas
x1 = np.cos(2 * np.pi * 100 * n * Ts)  # x1[nTs] = cos(2π100nTs)
x2 = np.sin(2 * np.pi * 100 * n * Ts)  # x2[nTs] = sin(2π100nTs)

# Correlación entre las señales
corr_x1_x2 = np.correlate(x1, x2, mode='full')

# Representación gráfica
plt.figure(figsize=(12, 6))

# Gráfica de las señales x1 y x2
plt.subplot(2, 1, 1)
plt.stem(n, x1, linefmt='c-', markerfmt='go', basefmt='c-', label="x1[n]")  # Línea azul, marcadores verdes
plt.stem(n, x2, linefmt='r-', markerfmt='yo', basefmt='b-', label="x2[n]")  # Línea roja, marcadores amarillos
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.title("Señales x1[n] y x2[n]")
plt.legend()
plt.grid()

# Gráfica de la correlación
plt.subplot(2, 1, 2)
lags = np.arange(-len(n) + 1, len(n))  # Definir los lags
plt.stem(lags, corr_x1_x2, linefmt='g-', markerfmt='ro', basefmt='b-')  # Línea verde, marcadores rojos
plt.xlabel("Desplazamiento (lag)")
plt.ylabel("Correlación")
plt.title("Correlación entre x1[n] y x2[n]")
plt.grid()

plt.tight_layout()
plt.show()

# Representación secuencial
print("Secuencia de correlación:", corr_x1_x2.tolist())



senal = wfdb.rdrecord("slp02a") 
informacion = senal.p_signal[:, 0] 

# Frecuencia de muestreo de la señal 
fs = senal.fs
print(f"Frecuencia de muestreo: {fs} Hz")

# Señal completa
plt.figure(figsize=(12, 5))
plt.plot(informacion, label="Señal completa", color='b')
plt.title('Señal EEG')
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [uV]')
plt.legend()
plt.show()


inicio = 10000
fin = 15000
datos_ampliados = informacion[inicio:fin]

# Señal fragmentada
plt.figure(figsize=(12, 5))
plt.plot(range(inicio, fin), datos_ampliados, label="Fragmento ampliado", color='r')
plt.title('Fragmento de la señal EEG')
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [uV]')
plt.legend()
plt.show()

        #FUNCIÓN DE TIEMPO#
# Estadísticos descriptivos: 
def analizar_frecuencia(signal, fs):
    # Picos en la señal
    picos, _ = find_peaks(signal)
    
    # Frecuencia media: número de picos por segundo
    num_picos = len(picos)
    duracion_segmento = len(signal) / fs
    frecuencia_media = num_picos / duracion_segmento

    # Calcular la frecuencia mediana
    distancias = np.diff(picos) / fs  # Distancias entre picos en segundos
    frecuencia_mediana = np.median(1 / distancias)  

    # Calcular la desviación estándar
    desviacion_estandar = np.std(1 / distancias)
    
    return frecuencia_media, frecuencia_mediana, desviacion_estandar

frecuencia_media, frecuencia_mediana, desviacion_estandar = analizar_frecuencia(datos_ampliados, fs)


print(f"Frecuencia media (Función de tiempo): {frecuencia_media:.2f} Hz")
print(f"Frecuencia mediana (Función de tiempo): {frecuencia_mediana:.2f} Hz")
print(f"Desviación estándar (Función de tiempo): {desviacion_estandar:.2f} Hz")

# Filtración de la señal (delta, theta, alpha, beta, gamma)
def filtro_pasabanda(datos, corte_bajo, corte_alto, fs, orden=4):
    nyquist = 0.5 * fs
    bajo = corte_bajo / nyquist
    alto = corte_alto / nyquist
    b, a = butter(orden, [bajo, alto], btype='band')
    y = filtfilt(b, a, datos)
    return y
delta = filtro_pasabanda(datos_ampliados, 0.5, 4, fs)
theta = filtro_pasabanda(datos_ampliados, 4, 8, fs)
alpha = filtro_pasabanda(datos_ampliados, 8, 13, fs)
beta = filtro_pasabanda(datos_ampliados, 13, 30, fs)
gamma = filtro_pasabanda(datos_ampliados, 30, 100, fs)
plt.figure(figsize=(12, 8))
plt.subplot(5, 1, 1)
plt.plot(delta, color='blue')
plt.title('Señal filtrada en Delta (0.5-4 Hz)')

plt.subplot(5, 1, 2)
plt.plot(theta, color='green')
plt.title('Señal filtrada en Theta (4-8 Hz)')

plt.subplot(5, 1, 3)
plt.plot(alpha, color='orange')
plt.title('Señal filtrada en Alpha (8-13 Hz)')

plt.subplot(5, 1, 4)
plt.plot(beta, color='red')
plt.title('Señal filtrada en Beta (13-30 Hz)')

plt.subplot(5, 1, 5)
plt.plot(gamma, color='purple')
plt.title('Señal filtrada en Gamma (30-100 Hz)')

plt.tight_layout()
plt.show()


# Calcular la Transformada de Fourier (FFT)
fft_signal = np.fft.fft(datos_ampliados)
frecuencias = np.fft.fftfreq(len(datos_ampliados), 1/fs)

# Filtrar las frecuencias positivas
indice_freq_positiva = np.where(frecuencias >= 0)[0]

# Magnitud del espectro
magnitud = np.abs(fft_signal[indice_freq_positiva])

# Graficar la transformada de Fourier (Espectro de magnitud)
plt.figure(figsize=(12, 5))
plt.plot(frecuencias[indice_freq_positiva], magnitud, label="")
plt.title("Transformada de Fourier de la Señal EEG")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.legend()
plt.grid(True)
plt.show()

frecuencias_psd, psd = welch(datos_ampliados, fs, nperseg=2048)

# Graficar la densidad espectral de potencia (PSD)
plt.figure(figsize=(12, 5))
plt.semilogy(frecuencias_psd, psd, color='r')  # Usamos semilog en el eje Y para mejor visualización
plt.title("Densidad espectral de potencia del fragmento de señal EEG")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad espectral (V²/Hz)")
plt.grid(True)
plt.show()


    #FUNCION DE LA FRECUENCIA
# 1. Función de filtrado pasa-banda
def filtro_pasabanda(datos, corte_bajo, corte_alto, fs, orden=4):
    nyquist = 0.5 * fs  # Frecuencia de Nyquist
    bajo = corte_bajo / nyquist
    alto = corte_alto / nyquist
    b, a = butter(orden, [bajo, alto], btype='band')  
    y = filtfilt(b, a, datos)
    return y

# Frecuencia de la señal EEG
def analizar_frecuencia(signal, fs):
   
    # Eliminación de ruidos de alta frecuencia
    señal_filtrada = filtro_pasabanda(signal, 0.5, 30, fs)  # Filtrado entre 0.5 Hz y 30 Hz
    
    señal_filtrada = (señal_filtrada - np.mean(señal_filtrada)) / np.std(señal_filtrada)

    # Picos en la señal filtrada
    picos, _ = find_peaks(señal_filtrada, distance=fs / 2)  # Asegura que los picos estén separados por al menos 0.5 segundos
    
    # Si no se encuentran picos, mostrar un mensaje y retornar None
    if len(picos) == 0:
        print("No se encontraron picos en la señal filtrada.")
        return None, None, None

    # Calcular la frecuencia media
    num_picos = len(picos)
    duracion_segmento = len(signal) / fs  # Duración de la señal en segundos
    frecuencia_media = num_picos / duracion_segmento  # Número de picos por segundo
    
    # Frecuencia mediana
    distancias = np.diff(picos) / fs  # Distancias entre picos en segundos
    frecuencias = 1 / distancias  # Convertir distancias a frecuencias (Hz)
    frecuencia_mediana = np.median(frecuencias)  # Mediana de las frecuencias
    
    # Desviación estándar
    desviacion_estandar = np.std(frecuencias)
    
    # Histograma 
       # Histograma 
    plt.figure(figsize=(10, 6))
    plt.hist(signal, bins=50, density=True, color='orange', alpha=0.6, label="Histograma")
    plt.title("Histograma de la señal EEG")
    plt.xlabel("Voltios (mV)")
    plt.ylabel("Frecuencia relativa")
    plt.legend()
    plt.grid()
    plt.show()
    
    return frecuencia_media, frecuencia_mediana, desviacion_estandar

frecuencia_media, frecuencia_mediana, desviacion_estandar = analizar_frecuencia(datos_ampliados, fs)

if frecuencia_media is not None:
    print(f"Frecuencia media (Función de la frecuencia): {frecuencia_media:.2f} Hz")
    print(f"Frecuencia mediana (Función de la frecuencia): {frecuencia_mediana:.2f} Hz")
    print(f"Desviación estándar (Función de la frecuencia): {desviacion_estandar:.2f} Hz")
