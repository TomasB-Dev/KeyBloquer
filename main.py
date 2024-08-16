import keyboard
import tkinter as tk

#estado de la tecla BloqNum 
bloqnum_desactivado = False

# Función para bloquear BloqNum
def bloquear_bloqnum():
    global bloqnum_desactivado
    bloqnum_desactivado = True
    estado_label.config(text="BloqNum deshabilitado")

# Función para desbloquear BloqNum
def desbloquear_bloqnum():
    global bloqnum_desactivado
    bloqnum_desactivado = False
    estado_label.config(text="BloqNum habilitado")

# Función que se ejecuta al presionar BloqNum
def manejar_pulsacion(event):
    if bloqnum_desactivado and event.name == 'num lock':
        # Si BloqNum está deshabilitado, revertir el estado presionando BloqNum de nuevo
        keyboard.press('num lock')
        keyboard.release('num lock')
        return False

# Intercepta todos los eventos de teclado
keyboard.hook(manejar_pulsacion)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Controlador de BloqNum")

# mostrar el estado de BloqNum
estado_label = tk.Label(root, text="BloqNum habilitado", font=("Arial", 14))
estado_label.pack(pady=10)

# Botones para bloquear y desbloquear BloqNum
bloquear_btn = tk.Button(root, text="Bloquear BloqNum", command=bloquear_bloqnum, font=("Arial", 12))
bloquear_btn.pack(pady=5)

desbloquear_btn = tk.Button(root, text="Desbloquear BloqNum", command=desbloquear_bloqnum, font=("Arial", 12))
desbloquear_btn.pack(pady=5)


root.mainloop()
