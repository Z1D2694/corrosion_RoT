# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:02:23 2023

@author: RY27388

HEX colors: https://htmlcolorcodes.com/es/
video: https://www.youtube.com/watch?v=5qOnzF7RsNA&t=178s

"""

import tkinter as tk
from PIL import ImageTk

# Atributos
w_frame1 = 500
h_frame1 = 500
h_frame2 = 200

bg_col = '#5D6D7E' 


def load_frame2():
    print("Prueba")
    
    
def pp_co2(pres_max,concentracion_co2):
    pp = pres_max*concentracion_co2 / 100
    
    if pp>30:
        comentario = 'Alto riesgo de corrosión por CO2'
        color = '#EC7063'
    elif pp < 7:
        comentario = 'Corrosión por CO2 poco probable'
        color = 'white'
    else:
        comentario = 'Riesgo medio de corrosión por CO2'
        color = '#F7DC6F'
    
    res = 'Presión parcial de CO2 [psi]: ' + str(round(pp,2)) +'\n'+ comentario
        
    return res, color

def pp_h2s(pres_max,concentracion_h2s):
    pp = pres_max*(concentracion_h2s/10000) / 100
    
    if pp > 0.05:
        comentario = 'Posible riesgo, chequear con integridad'
        color = '#EC7063'
    else:
        comentario = 'Corrosión por H2S poco probable'
        color = 'white'
    
    res = 'Presión parcial de H2S [psi]: ' + str(round(pp,2)) +'\n'+ comentario
        
    return res, color

def borrar():
    entry.delete(0, 'end')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')

def output_lb(pres_max,concentracion_co2,concentracion_h2s,label_out):
    
    borrar()
    for widgets in frame2.winfo_children():
        widgets.destroy()
   
    try:
        pres_max = float(pres_max)
        concentracion_co2 = float(concentracion_co2)
        concentracion_h2s = float(concentracion_h2s)
        
        comentario1, color1 = pp_co2(float(pres_max),float(concentracion_co2))
        comentario2, color2 = pp_h2s(float(pres_max),float(concentracion_h2s))
        
    except:
        comentario1, color1 = 'Los valores deben ser numéricos', '#D7BDE2'
        comentario2, color2 = '', '#D7BDE2'
   
    label_out = tk.Label(frame2,
                        text = comentario1,
                        bg = bg_col,
                        fg = color1,
                        font = ("TkMenuFont",12))
    label_out.pack(ipady=10)
    label_out2 = tk.Label(frame2,
                        text = comentario2,
                        bg = bg_col,
                        fg = color2,
                        font = ("TkMenuFont",12))
    label_out2.pack(ipady=10)

    

    
    
    
# inicializa la app
root = tk.Tk()
root.title("Corrosión")
root.iconbitmap("leaking.ico")
root.resizable(0,0) # fija el tamaño de la pantalla.

# Habilita escribir comandos en el lenguaje Tcl

root.eval("tk::PlaceWindow . center") # la ventana se abre en el centro de la pantalla.
#x = (root.winfo_screenwidth()-w_frame1) // 2                # ancho total de la pantalla y lo divido por 2 para centrar la pantalla.
#y = int(root.winfo_screenheight() * 0.1)                    # altura total para ubicar la pantalla 10% del límite superior de la pantalla.
#root.geometry('500x600+' + str(x) + '+' + str(y))


# Propiedades de la pantalla
# Se crea un frame widget
# bg: background color
frame1 = tk.Frame(root, width=w_frame1, height=h_frame1, bg=bg_col)
frame1.pack(fill = 'both')
frame1.pack_propagate(False) # Previene que el elmento hijo modifique al padre
frame2 = tk.Frame(root, width=w_frame1, height=h_frame2, bg=bg_col)
frame2.pack(fill = 'both')

# frame1 widgets
logo_img = ImageTk.PhotoImage(file="leaking_2.png")
logo_widget = tk.Label(frame1, image=logo_img, bg=bg_col)
logo_widget.image = logo_img
logo_widget.pack()

tk.Label(frame1,
         text="SEVERIDAD CORROSIVA POR CO2 y H2S",
         bg=bg_col,
         fg="white",
         font=("TkMenuFont",14)
         ).pack(pady=20)

# entrada0
label_entry = tk.Label(frame1,
                        text="Presión máxima esperada [psi]:",
                        bg = bg_col,
                        fg="white",
                        font=("TkMenuFont",12))
label_entry.pack(ipady=10)

entry = tk.Entry(frame1,
                  bg="#D6DBDF"
                  )
entry.pack()


# entrada1
label_entry1 = tk.Label(frame1,
                        text="CO2 [%vol]:",
                        bg = bg_col,
                        fg="white",
                        font=("TkMenuFont",12))
label_entry1.pack(ipady=10)

entry1 = tk.Entry(frame1,
                  bg="#D6DBDF"
                  )
entry1.pack()

# entrada2
label_entry2 = tk.Label(frame1,
                        text="H2S [ppm]:",
                        bg = bg_col,
                        fg="white",
                        font=("TkMenuFont",12))
label_entry2.pack(ipady=10)

entry2 = tk.Entry(frame1,
                  bg="#D6DBDF"
                  )
entry2.pack()


label_out = tk.Label(frame1,
                    text = "",
                    bg = bg_col,
                    font = ("TkMenuFont",12))
label_out.pack(ipady=10)


# botón widget
tk.Button(
        frame1,
        text="Calcular",
        font=("TkHeadingFont",14),
        bg = "#2E4053",
        fg = "white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command = lambda:output_lb(entry.get(),entry1.get(),entry2.get(),label_out)
        ).pack()




# corre la app
root.mainloop()