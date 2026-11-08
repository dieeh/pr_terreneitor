# Terreneitor

Firmware para un vehículo robótico autónomo seguidor de línea, desarrollado con ESP32 y MicroPython. El proyecto integra cinco sensores infrarrojos para detectar la trayectoria, cuatro motores DC para la tracción y un servomotor para la dirección.

## Descripción

El objetivo del proyecto es construir un vehículo capaz de seguir una línea mediante la lectura de un arreglo de sensores infrarrojos y el ajuste de su movimiento en función de la posición detectada.

El desarrollo comenzó utilizando un ESP8266. Debido a la disponibilidad limitada de GPIO, esa versión incorporó un registro de desplazamiento 74HC595 para ampliar las salidas y controlar los cuatro motores. Después de que la placa ESP8266 sufriera daños por una sobretensión, el proyecto migró a ESP32, que permitió controlar los periféricos directamente desde sus GPIO y simplificó el diseño.

El nombre **Terreneitor** es una referencia a un automóvil a control remoto recordado de comerciales de la infancia.

## Hardware

- ESP32 (versión final).
- Cinco sensores infrarrojos para detección de línea.
- Cuatro motores DC.
- Un servomotor para el mecanismo de dirección.
- Etapa de potencia para accionar los motores.

La implementación inicial con ESP8266 utilizaba un 74HC595 como expansor de salidas. El módulo `register.py` conserva esa parte del desarrollo.

## Software

- MicroPython.
- Control de motores mediante PWM y señales GPIO.
- Abstracciones de control de motores y servomotor implementadas en `motor.py`.

## Organización del repositorio

- `main.py`: implementación principal más reciente del control sobre ESP32.
- `main2.py`, `main3.py`, `main4.py`: iteraciones y pruebas de desarrollo.
- `motor.py`: clases y funciones para controlar motores DC y servomotor.
- `register.py`: implementación de comunicación con el registro de desplazamiento 74HC595, correspondiente a la etapa con ESP8266.
- `temps/`: pruebas y experimentos realizados durante el desarrollo.
- `sensor.txt`: notas relacionadas con los sensores.

## Puesta en marcha

1. Instala MicroPython en la placa ESP32.
2. Revisa las asignaciones de pines y parámetros eléctricos definidos en `main.py` y `motor.py`.
3. Copia los archivos necesarios a la placa.
4. Ejecuta `main.py` desde el entorno compatible con MicroPython.

> **Importante:** verifica las conexiones, alimentación y compatibilidad de los módulos antes de energizar el circuito. Los motores deben alimentarse mediante una etapa de potencia adecuada; no deben conectarse directamente a los GPIO del microcontrolador.

## Estado

Repositorio de un proyecto académico de robótica, con el historial de iteraciones y la migración desde ESP8266 a ESP32.
