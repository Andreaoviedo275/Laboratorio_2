# Laboratorio 2 Convolución y Correlación:

💫Descripción:

Este laboratorio tiene como objetivo analizar señales EEG descargadas de PhysioNet, aplicando herramientas de procesamiento digital de señales como:

✅ Caracterización en el dominio del tiempo.

✅ Análisis de frecuencia con la Transformada de Fourier (FFT).

✅ Filtrado por bandas de frecuencia EEG (delta, theta, alpha, beta, gamma).

✅ Representación espectral mediante Densidad Espectral de Potencia (PSD).

✅ Aplicación de la convolución y la correlación en señales.

- Este laboratorio analiza una señal de electroencefalografía (EEG) obtenida de la base de datos PhysioNet, específicamente del registro slp02a. Esta señal EEG pertenece a un estudio de polisomnografía, utilizado para analizar la actividad cerebral durante el sueño.

📌 ¿Qué es la señal EEG?

La electroencefalografía (EEG) es una técnica de monitoreo que registra la actividad eléctrica del cerebro a través de electrodos colocados en el cuero cabelludo. Se usa para detectar anomalías en la actividad cerebral, analizar estados de conciencia y estudiar trastornos neurológicos.

📌 Aplicaciones de esta señal EEG

✅ Análisis de ciclos del sueño: Identificación de fases REM y no REM.

✅ Detección de anomalías: Diagnóstico de epilepsia y otros trastornos.

✅ Procesamiento digital de señales: Extracción de características en EEG.

✅ Interfaz cerebro-computador (BCI): Uso de señales EEG para controlar dispositivos.

- La polisomnografía (PSG) es un estudio que monitorea diversas señales fisiológicas mientras una persona duerme. Se usa principalmente en el diagnóstico de trastornos del sueño, como la apnea del sueño, el insomnio, el síndrome de piernas inquietas, y otros problemas neurológicos.

  Dentro de la polisomnografía, una de las señales más importantes es la electroencefalografía (EEG), que mide la actividad eléctrica del cerebro y permite identificar las diferentes fases del sueño.

📌 ¿Cómo se usa el EEG en la polisomnografía?

El EEG en la polisomnografía ayuda a clasificar el sueño en sus diferentes etapas:

1️⃣ Sueño No REM

🟢 Fase 1 (Adormecimiento):

- Dura pocos minutos.
  
- Aparecen ondas Theta (4-8 Hz).
  
🟢 Fase 2 (Sueño ligero):

- Se reduce la actividad cerebral.
  
- Se observan husos del sueño (12-16 Hz en la banda Alpha-Beta) y complejos K (ondas grandes y aisladas).
  
🟢 Fase 3 (Sueño profundo o de ondas lentas):

- Ondas Delta (0.5-4 Hz) dominan la actividad.
  
- Fase crucial para la recuperación física y la consolidación de la memoria.

2️⃣ Sueño REM (Rapid Eye Movement)

🔴 Sueño REM:

- Aparecen ondas Beta (13-30 Hz) y Gamma (>30 Hz).

- Se producen los sueños más vívidos.

- Se da la parálisis temporal del cuerpo para evitar movimientos bruscos.

📌 Importancia del EEG en estudios de sueño

🛌 Diagnóstico de trastornos del sueño:

- Identificación de apnea del sueño, insomnio y narcolepsia.
  
- Evaluación de sueño fragmentado y despertares nocturnos.
  
📈 Análisis de calidad del sueño:

- Cantidad de tiempo en cada fase del sueño.
  
- Detección de sueño profundo insuficiente (Fase 3).
  
🧠 Neurociencia y aprendizaje automático:

- Modelos de inteligencia artificial pueden predecir fases del sueño.
  
- Uso de EEG para interfaces cerebro-computador (BCI).

💫Requisitos:

Para utilizar el spyder: Asegurarse de tener bien instaladas las siguientes librerias en tu programa:

  * Wfdb (Para leer archivos de señales fisiológicas)
    
  * Matplotlib (Para visualizar la señal)
    
  * Numpy (Para cálculos numéricos)
    
  * Scipy (Para estadísticas avanzadas)

💫Instalación:

Si no tienes alguna de las anteriores librerias mencionadas, puedes hacerlo manualmente de la siguiente manera:
  
  Ej: pip install wfdb

💫Uso: 

A.

La convolución de dos señales discretas 𝑥(𝑛) y ℎ(𝑛) se puede realizar manualmente siguiendo estos pasos:

1️⃣ Escribir las señales:

𝑥(𝑛)=[5,6,0,0,4,7,7]
ℎ(𝑛)=[1,0,0,3,5,2,7,4,8]

2️⃣ Formar la tabla de convolución:

- Se desplaza ℎ(𝑛) y se multiplica por cada valor de 𝑥(𝑛).
  
- Se suman los valores en diagonal para obtener 𝑦(𝑛), la señal de salida.

![Imagen de WhatsApp 2025-02-11 a las 19 45 05_e72da937](https://github.com/user-attachments/assets/6d03d69a-9e3f-4792-ad69-e2903ac3caaa)

Fig 1. Calculo manual.

3️⃣ Representar la señal resultante 𝑦(𝑛) en un gráfico de líneas o puntos.

![Imagen de WhatsApp 2025-02-11 a las 19 45 16_ca83ae20](https://github.com/user-attachments/assets/f8c77a78-3bc8-4a4b-87c2-7add80e95189)

Fig 2. Gráfico

Este código ejecuta la convolución de las señales definidas y grafica el resultado:

        import numpy as np
        import matplotlib.pyplot as plt
        
        Definir las señales
        x = np.array([5, 6, 0, 0, 4, 7])
        h = np.array([0, 0.3, 5, 2, 0, 4, 8])
        
        Calcular la convolución
        y = np.convolve(x, h, mode='full')
        
        Graficar el resultado
        plt.stem(range(len(y)), y, use_line_collection=True)
        plt.xlabel('n')
        plt.ylabel('y(n)')
        plt.title('Convolución de Señales')
        plt.grid()
        plt.show()

![Imagen de WhatsApp 2025-02-12 a las 19 29 24_1eb4b083](https://github.com/user-attachments/assets/1b224011-0ca0-42df-8dd7-57592a22fed2)

Fig 3. Convolución del código.

B. 

![Imagen de WhatsApp 2025-02-12 a las 19 29 25_635d54bf](https://github.com/user-attachments/assets/0039e8be-62b2-425b-9468-cc9ac68470cc)

Fig 4. Correlación de ambas señales.

C.

1️⃣ Descargar la señal EEG

- Asegúrate de tener el archivo "slp02a" de PhysioNet en la misma carpeta que el script.

2️⃣ Ejecutar el script

- Guarda el código en un archivo Python (lab2_eeg.py).
  
- Luego, ejecútalo con:

        python lab2_eeg.py

3️⃣ Interpreta los resultados

- Se generarán gráficos de la señal en el dominio del tiempo y la frecuencia.
  
- Se imprimirán estadísticos y frecuencias características en la consola.

📖 Explicación del Código

1️⃣ Carga y visualización de la señal EEG

        import wfdb
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy.signal import find_peaks, butter, filtfilt

✔ Se importan las librerías necesarias:

- wfdb: Para leer archivos de PhysioNet.

- numpy: Para cálculos numéricos.

- matplotlib: Para graficar señales.

- scipy.signal: Para detección de picos y filtrado de señales.

        senal = wfdb.rdrecord("slp02a")  
        informacion = senal.p_signal[:, 0]  
        fs = senal.fs  
        print(f"Frecuencia de muestreo: {fs} Hz")

✔ Carga la señal EEG del archivo "slp02a" de PhysioNet.

✔ Se extrae la señal del primer canal (informacion) y la frecuencia de muestreo (fs).

        plt.figure(figsize=(12, 5))
        plt.plot(informacion, color='b')
        plt.title('Señal EEG')
        plt.xlabel('Tiempo [s]')
        plt.ylabel('Voltaje [uV]')
        plt.show()

![Imagen de WhatsApp 2025-02-12 a las 19 27 39_0981cde8](https://github.com/user-attachments/assets/0bda5fe8-c8b2-4b84-b8cb-c98e1ecdc571)

Fig 5. Señal EEG.

✔ Visualiza la señal EEG completa en un gráfico.

2️⃣ Segmentación de la señal EEG

        inicio = 10000
        fin = 15000
        datos_ampliados = informacion[inicio:fin]
        
✔ Extrae un fragmento de la señal entre las muestras 10,000 y 15,000.

        plt.figure(figsize=(12, 5))
        plt.plot(range(inicio, fin), datos_ampliados, color='r')
        plt.title('Fragmento de la señal EEG')
        plt.xlabel('Tiempo [s]')
        plt.ylabel('Voltaje [uV]')
        plt.show()

![Imagen de WhatsApp 2025-02-12 a las 19 27 39_30b96d7f](https://github.com/user-attachments/assets/b62104c9-8ce1-4b14-8907-7932a974e7c0)

Fig 6. Fragmento de la señal EEG.

✔ Grafica el segmento ampliado, útil para ver detalles de la señal.

3️⃣  Análisis de frecuencia en el dominio del tiempo

        def analizar_frecuencia(signal, fs):
            picos, _ = find_peaks(signal)  
            num_picos = len(picos)  
            duracion = len(signal) / fs  
            frecuencia_media = num_picos / duracion  
        
            distancias = np.diff(picos) / fs  
            frecuencia_mediana = np.median(1 / distancias)  
            desviacion_estandar = np.std(1 / distancias)  
            
            return frecuencia_media, frecuencia_mediana, desviacion_estandar

✔ Detecta los picos en la señal EEG.

✔ Calcula la frecuencia media (cantidad de picos por segundo).

✔ Calcula la frecuencia mediana y la desviación estándar de los intervalos entre picos.

        frecuencia_media, frecuencia_mediana, desviacion_estandar = analizar_frecuencia(datos_ampliados, fs)
        
        print(f"Frecuencia media (Función de tiempo): {frecuencia_media:.2f} Hz")
        print(f"Frecuencia mediana (Función de tiempo): {frecuencia_mediana:.2f} Hz")
        print(f"Desviación estándar (Función de tiempo): {desviacion_estandar:.2f} Hz")

✔ Imprime los valores calculados en consola.

4️⃣ Filtrado por bandas de frecuencia EEG

        def filtro_pasabanda(datos, corte_bajo, corte_alto, fs, orden=4):
            nyquist = 0.5 * fs  
            bajo = corte_bajo / nyquist
            alto = corte_alto / nyquist
            b, a = butter(orden, [bajo, alto], btype='band')  
            return filtfilt(b, a, datos)
        def filtro_pasabanda(datos, corte_bajo, corte_alto, fs, orden=4):
            nyquist = 0.5 * fs  
            bajo = corte_bajo / nyquist
            alto = corte_alto / nyquist
            b, a = butter(orden, [bajo, alto], btype='band')  
            return filtfilt(b, a, datos)

✔ Aplica un filtro pasa banda para aislar diferentes frecuencias EEG.

        delta = filtro_pasabanda(datos_ampliados, 0.5, 4, fs)
        theta = filtro_pasabanda(datos_ampliados, 4, 8, fs)
        alpha = filtro_pasabanda(datos_ampliados, 8, 13, fs)
        beta = filtro_pasabanda(datos_ampliados, 13, 30, fs)
        gamma = filtro_pasabanda(datos_ampliados, 30, 100, fs)

✔ Se aplican filtros para extraer las diferentes bandas de frecuencia EEG.

        plt.figure(figsize=(12, 8))
        plt.subplot(5, 1, 1)
        plt.plot(delta, color='blue')
        plt.title('Señal filtrada en Delta (0.5-4 Hz)')

![Imagen de WhatsApp 2025-02-12 a las 19 27 40_c61c1546](https://github.com/user-attachments/assets/57de0410-f936-4409-ad19-d4c3b1042edf)

Fig 7. Bandas de frecuencia.

✔ Grafica cada una de las bandas EEG, mostrando cómo varía su actividad.

5️⃣ Transformada de Fourier (FFT) y análisis espectral

        fft_signal = np.fft.fft(datos_ampliados)
        frecuencias = np.fft.fftfreq(len(datos_ampliados), 1/fs)
        indice_freq_positiva = np.where(frecuencias >= 0)[0]
        magnitud = np.abs(fft_signal[indice_freq_positiva])

✔ Calcula la FFT para convertir la señal al dominio de la frecuencia.

✔ Se extraen frecuencias positivas y su magnitud.

        plt.figure(figsize=(12, 5))
        plt.plot(frecuencias[indice_freq_positiva], magnitud)
        plt.title("Transformada de Fourier de la Señal EEG")
        plt.xlabel("Frecuencia [Hz]")
        plt.ylabel("Magnitud")
        plt.grid(True)
        plt.show()
![Imagen de WhatsApp 2025-02-12 a las 19 27 40_524a73e5](https://github.com/user-attachments/assets/1152113d-cd54-4717-80a4-c020e42f263b)

Fig 8. Transformada de Fourier de la señal EEG.

✔ Grafica la Transformada de Fourier, mostrando el espectro de frecuencias.

6️⃣ Densidad Espectral de Potencia (PSD)

        plt.figure(figsize=(12, 5))
        plt.specgram(datos_ampliados, Fs=fs, NFFT=2048, noverlap=1024, cmap='plasma')
        plt.title("Densidad Espectral de Potencia (PSD) de la Señal EEG")
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Frecuencia [Hz]")
        plt.colorbar(label="Intensidad")
        plt.show()

![Imagen de WhatsApp 2025-02-12 a las 19 27 40_b3f6b083](https://github.com/user-attachments/assets/4c59408d-46e0-4dbb-a5fe-0bfdd028d515)

Fig 9. Densidad espectral de potencia (PSD) de la señal EEG.

✔ Calcula y grafica la PSD, mostrando cómo varía la energía en el tiempo.

7️⃣ Análisis estadístico en el dominio de la frecuencia

        def analizar_frecuencia(signal, fs):
            señal_filtrada = filtro_pasabanda(signal, 0.5, 30, fs)  
            señal_filtrada = (señal_filtrada - np.mean(señal_filtrada)) / np.std(señal_filtrada)
            picos, _ = find_peaks(señal_filtrada, distance=fs / 2)  
            
            if len(picos) == 0:
                print("No se encontraron picos en la señal filtrada.")
                return None, None, None
        
            num_picos = len(picos)
            duracion = len(signal) / fs  
            frecuencia_media = num_picos / duracion  
            distancias = np.diff(picos) / fs  
            frecuencias = 1 / distancias  
            frecuencia_mediana = np.median(frecuencias)  
            desviacion_estandar = np.std(frecuencias)
            
            return frecuencia_media, frecuencia_mediana, desviacion_estandar

✔ Calcula la frecuencia media, mediana y desviación estándar tras filtrar la señal.

        frecuencia_media, frecuencia_mediana, desviacion_estandar = analizar_frecuencia(datos_ampliados, fs)
        print(f"Frecuencia media: {frecuencia_media:.2f} Hz")

![Imagen de WhatsApp 2025-02-12 a las 19 46 11_9147cd18](https://github.com/user-attachments/assets/30d6006e-ef3f-4648-ada2-e44ca9057e73)

Fig 10. Histograma

![Imagen de WhatsApp 2025-02-12 a las 19 26 39_1e3a0b7f](https://github.com/user-attachments/assets/0a412245-033d-4061-882d-faa7aadcef4a)

Fig 11. Valores de consola.

![Imagen de WhatsApp 2025-02-12 a las 19 27 02_aff1761e](https://github.com/user-attachments/assets/7be78774-a282-4b57-b160-2ee34127b245)

Fig 12. Valores de consola.

✔ Muestra los valores finales en consola.
