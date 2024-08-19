# keyBlocker

## Descripción

Este proyecto consiste en un script en Python que desactiva la tecla `BloqNum` en tu teclado, con el objetivo de resolver un problema común en teclados de notebooks donde la tecla `BloqNum` queda atascada y actúa como si estuviera constantemente presionada. Este comportamiento puede causar varios problemas al escribir, ya que afecta la función de los teclados numéricos y otras teclas.

## ¿Por qué estoy haciendo esto?

Tengo una notebook en la que la tecla `BloqNum` queda presionada de manera continua, lo que hace que sea difícil utilizar el teclado de manera normal. Aunque existen algunos programas que prometen solucionar este problema, no me parecen lo suficientemente seguros o confiables. Por lo tanto, decidí crear mi propio script para desactivar o bloquear la tecla `BloqNum` y recuperar el control sobre mi teclado.

## Características

- **Bloqueo de la tecla `BloqNum`:** El script intercepta las pulsaciones de la tecla `BloqNum` y, si está desactivada, revertirá su estado inmediatamente, haciendo que la tecla no tenga efecto en el sistema.
- **Interfaz gráfica:** Se incluye una simple interfaz gráfica creada con `tkinter` que permite habilitar o deshabilitar la tecla `BloqNum` de manera sencilla.
- **Ejecución en segundo plano:** El script se ejecuta en segundo plano y monitorea las pulsaciones de la tecla en todo momento.
- **Seleccion de tecla en la interfaz grafica**
- 
