import keyboard
import tkinter as tk
from pystray import Icon, MenuItem as item, Menu
from PIL import Image, ImageDraw
#Estado de la key presionada
Estado_de_key = False
tecla_a_bloquear = None

def Desbloquear_Key():
    global Estado_de_key
    Estado_de_key = True


def Bloquear_Key():
    global Estado_de_key
    Estado_de_key = False

def quit_app(icon):
    icon.stop()  # Detener el icono 
    root.quit()

#funcion que se ejecute al presion la tecla seleccionada
def Tecla_Pulsada(event):
    global tecla_a_bloquear
    if Estado_de_key == False and tecla_a_bloquear and event.name == tecla_a_bloquear:
        keyboard.press(tecla_a_bloquear)
        keyboard.release(tecla_a_bloquear)
        return False
def seleccionar_tecla(tecla):
    global tecla_a_bloquear
    tecla_a_bloquear = tecla
    etiqueta_tecla.config(text=f"TECLA SELECCIONADA: {tecla}")
def minimize_to_tray():
    root.withdraw()  # oculto la ventna
    icon.run()

def show_window(icon):
    icon.stop()
    root.after(0, root.deiconify)  # muestro la ventana
    icon.stop()
    root.quit()
def create_tray_icon():
    #icono de secondplane
    image = Image.new('RGB', (20, 20), color=(21, 114, 226))
    d = ImageDraw.Draw(image)
    d.text((4,4), "KB", fill=(249, 249, 249))

    menu = Menu(
        item('Mostrar', show_window),
        item('Salir', quit_app)
    )
    
    return Icon("KeyBlocker", image, "KeyBlocker", menu)
#capta los eventos del teclado
keyboard.hook(Tecla_Pulsada)
root = tk.Tk()
root.title("KeyBlocker")
root.config(bg="#272623")





etiqueta_tecla = tk.Label(root, text="TECLA SELECCIONADA: Ninguna", font=("Arial", 14))
etiqueta_tecla.grid(row=0, column=0, columnspan=14, pady=10)
teclas = [
    'Escape', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6','F7','F8','F9','F10','F11','F12', 'num lock',
    '|','1','2','3','4','5','6','7','8','9','0',"'",'¿','delete','tab','q','w','e','r','t',
    'y','u','i','o','p','´','+','enter','caps lock','a','s','d','f','g','h','j','k','l','ñ','{','}',
    'shift','<','z','x','c','v','b','n','m',',','.','-','shif left','ctrl','command','alt','spacebar','alt gr','Function',
    'Insert','print screen',


]
Cantidad_De_Teclas = 0
for tecla in teclas:
    row = (Cantidad_De_Teclas // 14) + 1  
    column = Cantidad_De_Teclas % 14  
    boton = tk.Button(root, text=f"{tecla.upper()}", command=lambda t=tecla: seleccionar_tecla(t))
    boton.grid(row=row + 1, column=column, padx=5, pady=5)  #
    
    Cantidad_De_Teclas += 1

boton_bloquear = tk.Button(root, text="Bloquear tecla", command=Bloquear_Key, bg="red")  
boton_bloquear.grid(row=1, column=0, columnspan=7, pady=20, sticky="we")


boton_desbloquear = tk.Button(root, text="Desbloquear tecla", command=Desbloquear_Key, bg="green")  
boton_desbloquear.grid(row=1, column=7, columnspan=7, pady=10, sticky="we")
icon = create_tray_icon()
root.protocol("WM_DELETE_WINDOW", minimize_to_tray)

root.mainloop()
