# Laboratorio 2 Convolución y Correlación:

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

