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

2️⃣ Formar la tabla de convolución discreta:

- Se desplaza ℎ(𝑛) y se multiplica por cada valor de 𝑥(𝑛).
  
- Se suman los valores en diagonal para obtener 𝑦(𝑛), la señal de salida.

![Imagen de WhatsApp 2025-02-12 a las 23 32 57_07a2decb](https://github.com/user-attachments/assets/436178d4-2bcf-4ee5-a97f-961fb2110720)

Fig 1. Calculo manual.

3️⃣ Representar la señal resultante 𝑦(𝑛) en un gráfico de líneas o puntos.

![Imagen de WhatsApp 2025-02-12 a las 23 33 08_b1da985d](https://github.com/user-attachments/assets/2e8593fc-8907-4c53-996d-453d0594740d)


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

![Imagen de WhatsApp 2025-02-12 a las 22 06 26_7ae8af89](https://github.com/user-attachments/assets/74a2719b-1fb7-42fa-ba77-854c4e9bcbb4)

Fig 4. Señal x(n)

![Imagen de WhatsApp 2025-02-13 a las 00 34 20_00960ea8](https://github.com/user-attachments/assets/a6abc278-b3eb-44cf-935b-f4e4d6ea43ea)

Fig 5. Señal h(n)

B. 

![Imagen de WhatsApp 2025-02-12 a las 19 29 25_635d54bf](https://github.com/user-attachments/assets/0039e8be-62b2-425b-9468-cc9ac68470cc)

Fig 6. Correlación de ambas señales.

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

Fig 7. Señal EEG.

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

Fig 8. Fragmento de la señal EEG.

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

4️⃣ Transformada de Fourier (FFT) y análisis espectral

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

Fig 9. Transformada de Fourier de la señal EEG.

✔️ Grafica la Transformada de Fourier, mostrando el espectro de frecuencias.

✔️ Se pueden identificar las frecuencias dominantes en la señal EEG.

✔️ Si hay artefactos o ruido, se verán componentes de alta frecuencia no relacionadas con la actividad cerebral.

✔️ Un EEG normal mostrará la mayor parte de su potencia en frecuencias bajas.

✔️ Si la señal ha sido filtrada, se verá una reducción de las frecuencias fuera del rango de interés.

5️⃣Densidad Espectral de Potencia (PSD)

        plt.figure(figsize=(12, 5))
        plt.specgram(datos_ampliados, Fs=fs, NFFT=2048, noverlap=1024, cmap='plasma')
        plt.title("Densidad Espectral de Potencia (PSD) de la Señal EEG")
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Frecuencia [Hz]")
        plt.colorbar(label="Intensidad")
        plt.show()

![Imagen de WhatsApp 2025-02-12 a las 23 06 36_3672addb](https://github.com/user-attachments/assets/957e20e1-7c76-4050-94dd-13ed44d90b13)


Fig 10. Densidad espectral de potencia (PSD) de la señal EEG.

✔️ Calcula y grafica la PSD, mostrando cómo varía la energía en el tiempo.

✔️ Picos en ciertas bandas de frecuencia que corresponden a ondas cerebrales específicas (delta, theta, alpha, beta y gamma).
✔️ La clasificación de las señales se puede ver en la densidad espectral porque en el eje x están la frecuencias

✔️ Está nos puede ayudar a ver la potencia que tienen las muestras, cuando es una potencia muy alta espectral

✔️ La mayor parte de la energía suele concentrarse en frecuencias bajas (por debajo de 30 Hz).

✔️ Dependiendo del estado del paciente, se pueden ver diferencias en la actividad en cada banda:

Ondas delta (0.5 - 4 Hz) → Estado de sueño profundo.

Ondas theta (4 - 8 Hz) → Relajación, somnolencia.

Ondas alpha (8 - 13 Hz) → Estado de calma, relajación con ojos cerrados.

Ondas beta (13 - 30 Hz) → Atención y concentración.

Ondas gamma (>30 Hz) → Procesamiento cognitivo elevado.

6️⃣ Análisis estadístico en el dominio de la frecuencia

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

        plt.figure(figsize=(8, 5))
        plt.hist(frecuencias, bins=30, density=True, color="orange", edgecolor="black", alpha=0.75)
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Frecuencia relativa")
        plt.title("Histograma de las frecuencias dominantes de la señal EEG")
        plt.grid(axis="y", linestyle="--", alpha=0.7)


![Imagen de WhatsApp 2025-02-13 a las 00 34 21_4505d8e5](https://github.com/user-attachments/assets/d2067135-baba-45f4-a5bf-24a7985319f6)


Fig 11. Histograma

✔ Para graficar el histogrma

![Imagen de WhatsApp 2025-02-12 a las 19 26 39_1e3a0b7f](https://github.com/user-attachments/assets/0a412245-033d-4061-882d-faa7aadcef4a)

Fig 12. Valores de consola.

![Imagen de WhatsApp 2025-02-12 a las 19 27 02_aff1761e](https://github.com/user-attachments/assets/7be78774-a282-4b57-b160-2ee34127b245)

Fig 13. Valores de consola.

✔ Muestra los valores finales en consola.


